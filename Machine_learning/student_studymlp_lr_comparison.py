#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from matplotlib.colors import ListedColormap

# Simulate data: inputs are 'hours studied' and 'hours slept', output is pass (1) or fail (0)
np.random.seed(42)
n_samples = 200
study_hours = np.random.uniform(0, 10, n_samples)
sleep_hours = np.random.uniform(0, 10, n_samples)

# Simulated rule: optimal sleep is around 7 hours, study more than 5 helps, but nonlinear
labels = ((study_hours > 5) & (np.abs(sleep_hours - 7) < 2)).astype(int)

X = np.column_stack((study_hours, sleep_hours))
y = labels

# Train Logistic Regression and MLP
lr = LogisticRegression()
lr.fit(X, y)

mlp = MLPClassifier(hidden_layer_sizes=(20,), max_iter=3000, random_state=0)
mlp.fit(X, y)

# Plotting function
def plot_model(ax, model, X, y, title):
    h = .1
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    grid = np.c_[xx.ravel(), yy.ravel()]
    Z = model.predict(grid)
    Z = Z.reshape(xx.shape)

    cmap_light = ListedColormap(['#FFCCCC', '#CCE5FF'])
    cmap_bold = ListedColormap(['#FF0000', '#0000FF'])

    ax.contourf(xx, yy, Z, cmap=cmap_light, alpha=0.8)
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=30)
    ax.set_title(title)
    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Sleep Hours")
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.grid(True)

# Create plots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
plot_model(axs[0], lr, X, y, "Logistic Regression (Linear Boundary)")
plot_model(axs[1], mlp, X, y, "MLP (Non-linear Boundary)")

plt.tight_layout()
plt.show()

