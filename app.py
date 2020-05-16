# import tensorflow as tf
# from tesnorflow import keras
# import numpy as np
# import matplotlib.pyplot as plt

# data = keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = data.load_data()
Labels = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot"
}


def passByRef(aList):
    aList.append("Something")


aList = []
passByRef(aList)
print(aList)
