from keras.applications import resnet50
from PIL import Image
from keras import models, callbacks
from keras.applications import imagenet_utils
from keras.applications import resnet50
from keras.preprocessing.image import ImageDataGenerator
from sklearn import model_selection

from cv.holiday_similarity.data_utils import *
from cv.holiday_similarity.vis_utils import *


def e2e_network():
    inception_1 = resnet50.ResNet50(weights="imagenet", include_top=True)
    inception_2 = resnet50.ResNet50(weights="imagenet", include_top=True)

    for layer in inception_1.layers:
        layer.trainable = False
        layer.name = layer.name + "_1"
    for layer in inception_2.layers:
        layer.trainable = False
        layer.name = layer.name + "_2"

    vector_1 = inception_1.get_layer("avg_pool_1").output
    vector_2 = inception_2.get_layer("avg_pool_2").output

    sim_head = models.load_model(os.path.join(DATA_DIR, "models", "resnet-dot-best.h5"))
    for layer in sim_head.layers:
        print(layer.name, layer.input_shape, layer.output_shape)

    prediction = sim_head([vector_1, vector_2])

    model = models.Model(inputs=[inception_1.input, inception_2.input], outputs=prediction)
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    return model


def load_image_cache(image_cache, image_filename):
    image = plt.imread(os.path.join(IMAGE_DIR, image_filename))
    image = np.asarray(Image.fromarray(image).resize((224, 224)))
    image = image.astype("float32")
    image = imagenet_utils.preprocess_input(image)
    image_cache[image_filename] = image


def generate_image_cache(triples_data):
    image_cache = {}
    num_pairs = len(triples_data)
    for i, (image_filename_l, image_filename_r, _) in enumerate(triples_data):
        if i % 1000 == 0:
            print("images from {:d}/{:d} pairs loaded to cache".format(i, num_pairs))
        if image_filename_l not in image_cache:
            load_image_cache(image_cache, image_filename_l)
        if image_filename_r not in image_cache:
            load_image_cache(image_cache, image_filename_r)
    return image_cache


if __name__ == '__main__':
    DATA_DIR = './data'
    IMAGE_DIR = '/Users/chunhuizhang/workspaces/00_datasets/images/INRIA Holidays dataset /jpg'

    BATCH_SIZE = 32
    NUM_EPOCHS = 5
    BEST_MODEL_FILE = os.path.join(DATA_DIR, "models", "resnet-ft-best.h5")
    FINAL_MODEL_FILE = os.path.join(DATA_DIR, "models", "resnet-ft-final.h5")

    triples_data = create_triples(IMAGE_DIR)
    triples_data_trainval, triples_data_test = model_selection.train_test_split(triples_data, train_size=0.8)
    triples_data_train, triples_data_val = model_selection.train_test_split(triples_data_trainval, train_size=0.9)
    print(len(triples_data_train), len(triples_data_val), len(triples_data_test))

    datagen_args = dict(rotation_range=10,
                        width_shift_range=0.2,
                        height_shift_range=0.2,
                        zoom_range=0.2)
    datagens = [ImageDataGenerator(**datagen_args),
                ImageDataGenerator(**datagen_args)]

    image_cache = generate_image_cache(triples_data)

    train_pair_gen = pair_generator(triples_data_train, image_cache, datagens, BATCH_SIZE)
    val_pair_gen = pair_generator(triples_data_val, image_cache, None, BATCH_SIZE)

    num_train_steps = len(triples_data_train) // BATCH_SIZE
    num_val_steps = len(triples_data_val) // BATCH_SIZE

    model = e2e_network()
    checkpoint = callbacks.ModelCheckpoint(filepath=BEST_MODEL_FILE, save_best_only=True)
    history = model.fit_generator(train_pair_gen,
                                  steps_per_epoch=num_train_steps,
                                  epochs=NUM_EPOCHS,
                                  validation_data=val_pair_gen,
                                  validation_steps=num_val_steps,
                                  callbacks=[checkpoint])

    plot_training_curve(history)
