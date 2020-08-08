import keras.backend as K
from keras import layers, models
from keras.applications import vgg16, vgg19, inception_v3
from keras.models import Sequential
from keras.utils import plot_model


def create_base_network(input_shape):
    seq = Sequential()
    # CONV => RELU => POOL
    # 224, ==> ceil(224/1) == 224
    seq.add(layers.Conv2D(20, kernel_size=5, padding="same", input_shape=input_shape))
    seq.add(layers.Activation("relu"))
    # 45 ==> ceil((224-(2-1))/2) ==> 112
    seq.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    # CONV => RELU => POOL
    seq.add(layers.Conv2D(50, kernel_size=5, padding="same"))
    seq.add(layers.Activation("relu"))
    # (112-(2-1))/2 ==> 56
    seq.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    # Flatten => RELU
    seq.add(layers.Flatten())
    # (None, 500)
    seq.add(layers.Dense(500))

    return seq


def pretrained_network():
    pass


def cosine_distance(vecs, normalize=False):
    x, y = vecs
    if normalize:
        x = K.l2_normalize(x, axis=0)
        y = K.l2_normalize(y, axis=0)
    return K.prod(K.stack([x, y], axis=1), axis=1)


def cosine_distance_output_shape(shapes):
    return shapes[0]


def e2e_network(nn=create_base_network):
    input_shape = (224, 224, 3)
    base_network = nn(input_shape)

    image_left = layers.Input(shape=input_shape)
    image_right = layers.Input(shape=input_shape)

    left_vec = base_network(image_left)
    right_vec = base_network(image_right)

    dist = layers.Lambda(cosine_distance, output_shape=cosine_distance_output_shape)([left_vec, right_vec])

    fc1 = layers.Dense(128, kernel_initializer="glorot_uniform")(dist)
    fc1 = layers.Dropout(0.2)(fc1)
    fc1 = layers.Activation("relu")(fc1)

    pred = layers.Dense(2, kernel_initializer="glorot_uniform")(fc1)
    pred = layers.Activation("softmax")(pred)

    model = models.Model(inputs=[image_left, image_right], outputs=pred)

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def e2e_pretrained_network():
    vgg16_model = vgg16.VGG16(weights="imagenet", include_top=True)

    # vgg19_model = vgg19.VGG19(weights="imagenet", include_top=True)
    inception_model = inception_v3.InceptionV3(weights="imagenet", include_top=True)

    input_shape = (224, 224, 3)
    image_left = layers.Input(shape=input_shape)
    image_right = layers.Input(shape=input_shape)

    base_model = models.Model(input=vgg16_model.input, output=vgg16_model.get_layer('fc2').output)
    left_vec = base_model(image_left)
    right_vec = base_model(image_right)
    dist = layers.Lambda(cosine_distance, output_shape=cosine_distance_output_shape)([left_vec, right_vec])
    fc1 = layers.Dense(128, kernel_initializer="glorot_uniform")(dist)
    fc1 = layers.Dropout(0.2)(fc1)
    fc1 = layers.Activation("relu")(fc1)

    pred = layers.Dense(2, kernel_initializer="glorot_uniform")(fc1)
    pred = layers.Activation("softmax")(pred)

    model = models.Model(inputs=[image_left, image_right], outputs=pred)

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def concat_vectors(vector_size, ):
    input_1 = layers.Input(shape=(vector_size,))
    input_2 = layers.Input(shape=(vector_size,))
    layers.merge.Concatenate(input_1)


if __name__ == '__main__':
    vgg19_model = vgg19.VGG19(weights="imagenet", include_top=True)
    inception_model = inception_v3.InceptionV3(weights="imagenet", include_top=True)
    model = e2e_network()
    plot_model(inception_model, to_file='inception_model.png', show_layer_names=True, show_shapes=True)
