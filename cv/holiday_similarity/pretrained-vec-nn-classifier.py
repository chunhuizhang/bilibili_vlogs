from keras import backend as K
from keras import layers, models, callbacks, utils

from cv.holiday_similarity.data_utils import *
from cv.holiday_similarity.image_vectors_utils import *

DATA_DIR = "./data"
IMAGE_DIR = '/Users/chunhuizhang/workspaces/00_datasets/images/INRIA Holidays dataset /jpg'

BATCH_SIZE = 32
NUM_EPOCHS = 10


def e2e_model_concat(vec_size):
    input_1 = layers.Input(shape=(vec_size,))
    input_2 = layers.Input(shape=(vec_size,))

    merged = layers.merge.Concatenate(axis=-1)([input_1, input_2])

    fc1 = layers.Dense(512, kernel_initializer="glorot_uniform")(merged)
    fc1 = layers.Dropout(0.2)(fc1)
    fc1 = layers.Activation("relu")(fc1)

    fc2 = layers.Dense(128, kernel_initializer="glorot_uniform")(fc1)
    fc2 = layers.Dropout(0.2)(fc2)
    fc2 = layers.Activation("relu")(fc2)

    pred = layers.Dense(2, kernel_initializer="glorot_uniform")(fc2)
    pred = layers.Activation("softmax")(pred)
    model = models.Model(inputs=[input_1, input_2], outputs=pred)
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    utils.plot_model(model, to_file='./data/images/concat.png', show_shapes=True, show_layer_names=True)
    return model


def e2e_model_dot(vec_size):
    def cosine_distance(vecs, normalize=False):
        x, y = vecs
        if normalize:
            x = K.l2_normalize(x, axis=0)
            y = K.l2_normalize(x, axis=0)
        return K.prod(K.stack([x, y], axis=1), axis=1)

    def cosine_distance_output_shape(shapes):
        return shapes[0]

    input_1 = layers.Input(shape=(vec_size,))
    input_2 = layers.Input(shape=(vec_size,))

    merged = layers.Lambda(cosine_distance,
                           output_shape=cosine_distance_output_shape)([input_1, input_2])

    fc1 = layers.Dense(512, kernel_initializer="glorot_uniform")(merged)
    fc1 = layers.Dropout(0.2)(fc1)
    fc1 = layers.Activation("relu")(fc1)

    fc2 = layers.Dense(128, kernel_initializer="glorot_uniform")(fc1)
    fc2 = layers.Dropout(0.2)(fc2)
    fc2 = layers.Activation("relu")(fc2)

    pred = layers.Dense(2, kernel_initializer="glorot_uniform")(fc2)
    pred = layers.Activation("softmax")(pred)
    model = models.Model(inputs=[input_1, input_2], outputs=pred)
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    utils.plot_model(model, to_file='./data/images/dot.png', show_shapes=True, show_layer_names=True)
    return model


def e2e_model_l1(vec_size):
    def absdiff(vecs):
        x, y = vecs
        return K.abs(K.sum(K.stack([x, -y], axis=1), axis=1))

    def absdiff_output_shape(shapes):
        return shapes[0]

    input_1 = layers.Input(shape=(vec_size,))
    input_2 = layers.Input(shape=(vec_size,))
    merged = layers.Lambda(absdiff, output_shape=absdiff_output_shape)([input_1, input_2])

    fc1 = layers.Dense(512, kernel_initializer="glorot_uniform")(merged)
    fc1 = layers.Dropout(0.2)(fc1)
    fc1 = layers.Activation("relu")(fc1)

    fc2 = layers.Dense(128, kernel_initializer="glorot_uniform")(fc1)
    fc2 = layers.Dropout(0.2)(fc2)
    fc2 = layers.Activation("relu")(fc2)

    pred = layers.Dense(2, kernel_initializer="glorot_uniform")(fc2)
    pred = layers.Activation("softmax")(pred)
    model = models.Model(inputs=[input_1, input_2], outputs=pred)
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    utils.plot_model(model, to_file='./data/images/l1.png', show_shapes=True, show_layer_names=True)
    return model


def e2e_model_l2(vec_size):
    def euclidean_distance(vecs):
        x, y = vecs
        return K.sqrt(K.sum(K.stack([K.square(x), -K.square(y)], axis=1), axis=1))

    def euclidean_distance_output_shape(shapes):
        xshape, yshape = shapes
        return xshape

    input_1 = layers.Input(shape=(vec_size,))
    input_2 = layers.Input(shape=(vec_size,))
    merged = layers.Lambda(euclidean_distance,
                           output_shape=euclidean_distance_output_shape)([input_1, input_2])

    fc1 = layers.Dense(512, kernel_initializer="glorot_uniform")(merged)
    fc1 = layers.Dropout(0.2)(fc1)
    fc1 = layers.Activation("relu")(fc1)

    fc2 = layers.Dense(128, kernel_initializer="glorot_uniform")(fc1)
    fc2 = layers.Dropout(0.2)(fc2)
    fc2 = layers.Activation("relu")(fc2)

    pred = layers.Dense(2, kernel_initializer="glorot_uniform")(fc2)
    pred = layers.Activation("softmax")(pred)

    model = models.Model(inputs=[input_1, input_2], outputs=pred)
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    utils.plot_model(model, to_file='./data/images/l2.png', show_shapes=True, show_layer_names=True)
    return model


if __name__ == '__main__':
    image_triples = get_holiday_triples(IMAGE_DIR)
    train_triples, val_triples, test_triples = train_test_split(image_triples,
                                                                splits=[0.7, 0.1, 0.2])
    print(len(train_triples), len(val_triples), len(test_triples))

    VECTOR_SIZE = 2048
    VECTOR_FILE = os.path.join(DATA_DIR, "resnet-vectors.tsv")

    vec_dict = load_vectors(VECTOR_FILE)

    train_gen = data_generator(train_triples, VECTOR_SIZE, vec_dict, BATCH_SIZE)
    val_gen = data_generator(val_triples, VECTOR_SIZE, vec_dict, BATCH_SIZE)

    # model_name = get_model_file(DATA_DIR, 'resnet', 'dot', 'best')
    # model_name = get_model_file(DATA_DIR, 'resnet', 'concat', 'best')
    model_name = get_model_file(DATA_DIR, 'resnet', 'l2', 'best')

    checkpoint = callbacks.ModelCheckpoint(model_name, save_best_only=True)
    train_steps_per_epoch = len(train_triples) // BATCH_SIZE
    val_steps_per_epoch = len(val_triples) // BATCH_SIZE

    # model = e2e_model_concat(VECTOR_SIZE)
    # model = e2e_model_dot(VECTOR_SIZE)
    # model = e2e_model_l1(VECTOR_SIZE)
    e2e_model_l2(VECTOR_SIZE)

    # history = model.fit_generator(train_gen, steps_per_epoch=train_steps_per_epoch,
    #                               epochs=NUM_EPOCHS,
    #                               validation_data=val_gen, validation_steps=val_steps_per_epoch,
    #                               callbacks=[checkpoint])
    #
    # plot_training_curve(history)
    #
    # final_model_name = get_model_file(DATA_DIR, "resnet", "l2", 'final')
    # model.save(final_model_name)
    #
    # test_gen = data_generator(test_triples, VECTOR_SIZE, vec_dict, BATCH_SIZE)
    # final_accuracy = evaluate_model(models.load_model(final_model_name), test_gen, test_triples, BATCH_SIZE)
    #
    # test_gen = data_generator(test_triples, VECTOR_SIZE, vec_dict, BATCH_SIZE)
    # best_accuracy = evaluate_model(models.load_model(model_name), test_gen, test_triples, BATCH_SIZE)
    #
    # scores = best_accuracy if best_accuracy > final_accuracy else final_accuracy
