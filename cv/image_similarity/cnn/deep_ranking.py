
import tensorflow as tf

from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications import Xception, ResNet50


from tensorflow.keras.utils import plot_model
from tensorflow.keras.layers import *
from tensorflow.keras import backend as K

from keras.applications.vgg16 import VGG16
from keras.applications import Xception

vgg_with_top = VGG16(include_top=True)
# plot_model(vgg_with_top, to_file='vgg16_with_top.png', show_shapes=True)

vgg_without_top = VGG16(include_top=False)
# plot_model(vgg_without_top, to_file='vgg16_without_top.png', show_shapes=True)

inception = InceptionV3()

# plot_model(inception, to_file='inception_v3_withtop.png', show_shapes=True)

xception = Xception()
# plot_model(xception, to_file='xception_with_top.png', show_shapes=True)
resnet = ResNet50()
plot_model(resnet, to_file='resnet_with_top.png', show_shapes=True)


# first_input = Input(shape=(224, 224, 3))
# first_conv = Conv2D(96, kernel_size=(8, 8), strides=(16, 16), padding='same')(first_input)
# print(first_conv)
# first_max = MaxPool2D(pool_size=(3, 3), strides=(4, 4), padding='same')(first_conv)
# print(first_max)
# first_max = Flatten()(first_max)
# first_max = Lambda(lambda x: K.l2_normalize(x, axis=1))(first_max)
#
# second_input = Input(shape=(224, 224, 3))
# second_conv = Conv2D(96, kernel_size=(8, 8), strides=(32, 32), padding='same')(second_input)
# print(second_conv)
# second_max = MaxPool2D(pool_size=(7, 7), strides=(2, 2), padding='same')(second_conv)
# print(second_max)
# second_max = Flatten()(second_max)
# second_max = Lambda(lambda x: K.l2_normalize(x, axis=1))(second_max)

# merge_one = concatenate([first_max, second_max])

# print(first_max)
# print(second_max)
# print(merge_one)