import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons, make_circles
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from matplotlib.colors import ListedColormap

def plot_decision_boundary(model, X, y, ax, title):
    h = .02  # step size in the mesh
    cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#0000FF'])

    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cmap_light)

    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])

# Generate non-linearly separable data (moons and circles)
X1, y1 = make_moons(n_samples=300, noise=0.2, random_state=0)
X2, y2 = make_circles(n_samples=300, noise=0.1, factor=0.5, random_state=1)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Linear model (Logistic Regression)
lr1 = LogisticRegression()
lr1.fit(X1, y1)
plot_decision_boundary(lr1, X1, y1, axs[0, 0], "Linear Model on Moons")

lr2 = LogisticRegression()
lr2.fit(X2, y2)
plot_decision_boundary(lr2, X2, y2, axs[1, 0], "Linear Model on Circles")

# Neural Network (MLP)
mlp1 = MLPClassifier(hidden_layer_sizes=(10,), max_iter=2000, random_state=0)
mlp1.fit(X1, y1)
plot_decision_boundary(mlp1, X1, y1, axs[0, 1], "MLP on Moons")

mlp2 = MLPClassifier(hidden_layer_sizes=(10,), max_iter=2000, random_state=1)
mlp2.fit(X2, y2)
plot_decision_boundary(mlp2, X2, y2, axs[1, 1], "MLP on Circles")

plt.tight_layout()
plt.show()

