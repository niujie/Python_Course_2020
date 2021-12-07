import torch
import torch.nn as nn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

# 0) prepare data
X_numpy, y_numpy = datasets.make_regression(
    n_samples=100, n_features=1, noise=20, random_state=4)
X_train_numpy, X_test_numpy, y_train_numpy, y_test_numpy = train_test_split(
    X_numpy, y_numpy, test_size=0.2, random_state=1234)

fig = plt.figure(figsize=(8, 6))
plt.scatter(X_numpy[:, 0], y_numpy, color="b", marker="o", s=30)
plt.show()

print(X_train_numpy.shape)
print(y_train_numpy.shape)

X = torch.from_numpy(X_numpy.astype(np.float32))
y = torch.from_numpy(y_numpy.astype(np.float32))
y = y.view(y.shape[0], 1)

X_train = torch.from_numpy(X_train_numpy.astype(np.float32))
y_train = torch.from_numpy(y_train_numpy.astype(np.float32))
y_train = y_train.view(y_train.shape[0], 1)

X_test = torch.from_numpy(X_test_numpy.astype(np.float32))
y_test = torch.from_numpy(y_test_numpy.astype(np.float32))
y_test = y_test.view(y_test.shape[0], 1)

n_samples, n_features = X_train.shape

# 1) model
input_size = n_features
output_size = 1
model = nn.Linear(input_size, output_size)

# 2) loss and optimizer
learning_rate = 0.01
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# 3) training loop
num_epochs = 1000
for epoch in range(num_epochs):
    # forward pass
    y_predicted = model(X_train)
    loss = criterion(y_predicted, y_train)

    # backward pass
    loss.backward()

    # update
    optimizer.step()

    optimizer.zero_grad()

    if (epoch+1) % 10 == 0:
        print(f'epoch: {epoch+1}, loss = {loss.item():.4f}')

predicted = model(X_test)
mse_value = criterion(y_test, predicted)
print(mse_value.detach().numpy())

# plot
y_pred_line = model(X).detach().numpy()
cmap = plt.get_cmap('viridis')
fig = plt.figure(figsize=(8, 6))
m1 = plt.scatter(X_train_numpy, y_train_numpy, color=cmap(0.9), s=10)
m2 = plt.scatter(X_test_numpy, y_test_numpy, color=cmap(0.5), s=10)
plt.plot(X, y_pred_line, color='black', linewidth=2, label='Prediction')
plt.show()
