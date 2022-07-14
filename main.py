# %% Resampled Importance Sampling
import utils
import numpy as np

print("Hello, RIS")
x, y = np.meshgrid(np.linspace(-2,2,200), np.linspace(-2,2,200))
x, y = x - x.mean(), y - y.mean()
z = x * np.exp(-x**2 - y**2)
utils.display2DArray(z)
# %%
