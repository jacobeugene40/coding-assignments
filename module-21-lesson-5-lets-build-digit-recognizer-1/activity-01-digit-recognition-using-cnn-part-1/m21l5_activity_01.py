# M21 Lesson 5 - Activity 1: Digit Recognition using CNN - Part 1
# (data preprocessing + baseline model, MNIST)
# The MNIST dataset downloads automatically the first time you run this (needs internet).
# Needs: pip install tensorflow matplotlib --break-system-packages
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical, load_img, img_to_array
from tensorflow.keras.optimizers import SGD
from numpy import argmax
import matplotlib.pyplot as plt

# Step 2: load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print('Train Dataset (x):', x_train.shape)
print('Train Dataset (y):', y_train.shape)
print('Test Dataset (x):', x_test.shape)
print('Test Dataset (y):', y_test.shape)

for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))
plt.show()

# Step 3: preprocess the dataset
# The full MNIST set has 60,000 training images. That's more than a CPU needs to learn
# digits well, so this keeps a smaller slice to train faster. Raise these numbers if you
# have a GPU and more time.
train_size = 8000
test_size = 2000
x_train = x_train[:train_size]
y_train = y_train[:train_size]
x_test = x_test[:test_size]
y_test = y_test[:test_size]

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Step 4: build the baseline model
batch_size = 128
epochs = 10

model = Sequential()
model.add(Input(shape=input_shape))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

opt = SGD(learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.summary()
