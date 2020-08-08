import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from keras.applications import imagenet_utils
from keras.applications import resnet50
from keras.models import Model

IMAGE_DIR = '/Users/chunhuizhang/workspaces/00_datasets/images/INRIA Holidays dataset /jpg'
DATA_DIR = './data'


def image_batch_generator(image_names, batch_size):
    num_batches = len(image_names) // batch_size
    for i in range(num_batches):
        batch = image_names[i * batch_size: (i + 1) * batch_size]
        yield batch
    batch = image_names[(i + 1) * batch_size:]
    yield batch


def vectorize_images(image_dir, image_size, preprocessor,
                     model, vector_file, batch_size=32):
    image_names = os.listdir(image_dir)
    num_vecs = 0
    fvec = open(vector_file, "w")
    for image_batch in image_batch_generator(image_names, batch_size):
        batched_images = []
        for image_name in image_batch:
            image = plt.imread(os.path.join(image_dir, image_name))
            # image = imresize(image, (image_size, image_size))
            image = np.asarray(Image.fromarray(image).resize((image_size, image_size)))
            batched_images.append(image)
        X = preprocessor(np.array(batched_images, dtype="float32"))
        vectors = model.predict(X)
        for i in range(vectors.shape[0]):
            if num_vecs % 100 == 0:
                print("{:d}/{:d} vectors generated".format(num_vecs, vectors.shape[0]))
            image_vector = ",".join(["{:.5e}".format(v) for v in vectors[i].tolist()])
            # print(image_batch[i], image_vector)
            # print(type(image_batch[i]), type(image_vector))
            fvec.write("{:s}\t{:s}\n".format(image_batch[i], image_vector))
            num_vecs += 1
    print("{:d} vectors generated".format(num_vecs))
    fvec.close()


def generate_features(model, image_size, vector_file):
    model = Model(input=model.input,
                  output=model.get_layer("avg_pool").output)
    preprocessor = imagenet_utils.preprocess_input

    vectorize_images(IMAGE_DIR, image_size, preprocessor, model, vector_file)


if __name__ == '__main__':
    IMAGE_SIZE = 224
    # vgg16_model = vgg16.VGG16(weights="imagenet", include_top=True)
    # VECTOR_FILE = os.path.join(DATA_DIR, "vgg19-vectors.tsv")
    # generate_features(vgg16_model, IMAGE_SIZE, VECTOR_FILE)

    VECTOR_FILE = os.path.join(DATA_DIR, "resnet-vectors.tsv")
    resnet_model = resnet50.ResNet50(weights="imagenet", include_top=True)
    generate_features(resnet_model, IMAGE_SIZE, VECTOR_FILE)
