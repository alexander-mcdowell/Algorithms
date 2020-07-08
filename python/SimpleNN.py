import math
import numpy as np
import random
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import time

def kfold_partition(data, k):
    if k == 1: return data, []
    shuffled_data = data[::]
    random.shuffle(shuffled_data)
    i = (k - 1) * (len(data) // k)
    training_data, validation_data = shuffled_data[:i], shuffled_data[i:]
    return training_data, validation_data

# Data Processing
# -----------------------------------------------------------------
file = open("iris.data")
# Data takes the form of [inputs, classification] for each datapoint
data = []
class_name_to_val = {}
class_val_to_name = {}
class_count = 0
while True:
    s = file.readline().strip()
    if s == "": break
    split_line = s.split(",")
    inputs = [float(x) for x in split_line[:-1]]
    class_name = split_line[-1]
    if class_name not in class_name_to_val:
        class_name_to_val[class_name] = class_count
        class_val_to_name[class_count] = class_name
        class_count += 1
    data.append([inputs, class_name_to_val[class_name]])
num_data = len(data)
num_classes = class_count
np.random.shuffle(data)
test_ratio = 1/5
i = math.floor(num_data * test_ratio)
test_data, left_over = data[:i], data[i:]
train_data, valid_data = kfold_partition(left_over, k = 5)

train_x, train_y = [], []
valid_x, valid_y = [], []
test_x, test_y = [], []
for train in train_data:
    train_x.append(np.asarray(train[0]))
    y = np.zeros(num_classes)
    y[train[1]] = 1.0
    train_y.append(y)
for valid in valid_data:
    valid_x.append(np.asarray(valid[0]))
    y = np.zeros(num_classes)
    y[valid[1]] = 1.0
    valid_y.append(np.asarray(y))
for test in test_data:
    test_x.append(np.asarray(test[0]))
    y = np.zeros(num_classes)
    y[test[1]] = 1.0
    test_y.append(y)
train_x, train_y = np.asarray(train_x), np.asarray(train_y)
valid_x, valid_y = np.asarray(valid_x), np.asarray(valid_y)
test_x, test_y = np.asarray(test_x), np.asarray(test_y)

# Model Construction
# -----------------------------------------------------------------
class SimpleNN(tf.keras.Model):
  def __init__(self, hiddens, num_outputs, activations, output_activation):
    super(SimpleNN, self).__init__()
    self.dense_layers = []
    for i in range(len(hiddens)):
        if activations[i] == "relu":
            self.dense_layers.append(keras.layers.Dense(hiddens[i], activation = tf.nn.relu))
        elif activations[i] == "sigmoid":
            self.dense_layers.append(keras.layers.Dense(hiddens[i], activation = tf.nn.sigmoid))
        elif activations[i] == "tanh":
            self.dense_layers.append(keras.layers.Dense(hiddens[i], activation = tf.nn.tanh))
    if output_activation == "relu":
        self.out_layer = keras.layers.Dense(num_outputs, activation = tf.nn.relu)
    elif output_activation == "sigmoid":
        self.out_layer = keras.layers.Dense(num_outputs, activation = tf.nn.sigmoid)
    elif output_activation == "tanh":
        self.out_layer = keras.layers.Dense(num_outputs, activation = tf.nn.tanh)
    elif output_activation == "softmax":
        self.out_layer = keras.layers.Dense(num_outputs, activation = tf.nn.softmax)
  def call(self, inputs):
    x = inputs
    for h in range(len(self.dense_layers)):
        x = self.dense_layers[h](x)
    return self.out_layer(x)

model = SimpleNN([5, 10], num_classes, ["relu", "relu"], "softmax")
model.compile(loss = keras.losses.CategoricalCrossentropy(from_logits = True),
              optimizer = keras.optimizers.Adam(),
              metrics = ['accuracy'])

# Training
# -----------------------------------------------------------------
batch_size = 5
num_epochs = 1000
start_time = time.time()
history = model.fit(train_x, train_y,
                    batch_size = batch_size,
                    epochs = num_epochs,
                    validation_data = (valid_x, valid_y),
                    verbose = 0)
end_time = time.time()
print("Training complete after %.2f minutes" % ((end_time - start_time) / 60.))
results = model.evaluate(test_x, test_y,
                         batch_size = batch_size,
                         verbose = 0)
print("Test loss and accuracy", results)
example_predictions = 5
x = list(range(len(test_data)))
random.shuffle(x)
indices = x[:example_predictions]
pred_x, pred_y = [], []
for i in indices:
    pred_x.append(test_data[i][0])
    pred_y.append(test_data[i][1])
predictions = model.predict(pred_x)
i = 0
for p in predictions:
    pred_out = class_val_to_name[np.argmax(p)]
    act_out = class_val_to_name[pred_y[i]]
    print("Prediction %d: Input = %s; Predicted Output = %s; Actual Output = %s" % (i, str(pred_x[i]), pred_out, act_out))
    i += 1

losses = history.history["loss"]
accuracies = history.history["accuracy"]
validation_accuracies = history.history["val_accuracy"]
fig, axes = plt.subplots(2, 1)
axes[0].plot(list(range(num_epochs)), losses)
axes[0].set_title("Loss vs. Epoch #")

axes[1].plot(list(range(num_epochs)), accuracies, label = "Accuracy")
axes[1].plot(list(range(num_epochs)), validation_accuracies, label = "Validation Accuracy")
axes[1].legend(loc = "upper left", title = "Legend")
axes[1].set_title("Accuracy vs. Epoch #")
plt.show()
