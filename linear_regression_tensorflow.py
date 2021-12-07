import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

X, y = datasets.make_regression(
    n_samples=100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234)

fig = plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], y, color="b", marker="o", s=30)
plt.show()

print(X_train.shape)
print(y_train.shape)

n_samples, n_features = X_train.shape

# 1) model
model = keras.models.Sequential([
    layers.Dense(units=1)   # Linear Model
])

# 2) loss and optimizer
loss = keras.losses.MeanSquaredError()
optim = keras.optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=optim, loss=loss)

# 3) train the model
earlystopping = keras.callbacks.EarlyStopping(monitor='loss', patience=10)

history = model.fit(
    X_train, y_train, epochs=1000, verbose=1,
    # Calculate validation results on 20% of the training data
    # validation_split=0.2, callbacks=[earlystopping]
)


def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    # plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)
    plt.show()


plot_loss(history)

predicted = model.predict(X_test)
predicted = np.reshape(predicted, (predicted.shape[0],))
mse_value = np.mean((y_test - predicted)**2)
print(mse_value)

# 4) predict and plot
y_pred_line = model.predict(X)
cmap = plt.get_cmap('viridis')
fig = plt.figure(figsize=(8, 6))
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
plt.plot(X, y_pred_line, color='black', linewidth=2, label='Prediction')
plt.show()
