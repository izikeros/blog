# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.8.0
#   kernelspec:
#     display_name: crop_forecasting
#     language: python
#     name: crop_forecasting
# ---

# %%
import numpy as np

np.random.seed(42)
x = np.random.poisson(5, 1000)

# %%
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns

plt.style.use("bmh")
_ = plt.subplots(figsize=(5, 3))
sns.distplot(x, fit=norm);
plt.show()

# %%
from scipy.special import boxcox1p

xt = boxcox1p(1 + x,0)

_ = plt.subplots(figsize=(5, 3))
sns.distplot(xt, fit=norm);
plt.show()

# %%

# %%
import numpy as np

# Set seed for reproducibility
np.random.seed(123)

# Generate 1000 data points for each feature
lognormal_data = np.random.lognormal(mean=0, sigma=1, size=1000)
poisson_data = np.random.poisson(lam=5, size=1000)
# Combine the two features into a single dataset
X = np.column_stack((lognormal_data, poisson_data))

# Apply the Box-Cox transformation of 1 + x to both features
lognormal_transformed = boxcox1p(1 + lognormal_data, 0)
poisson_transformed = boxcox1p(1 + poisson_data, 0)

# Combine the two features into a single dataset
Xt = np.column_stack((lognormal_transformed, poisson_transformed))

# %%
plt.subplot(2, 2, 1)
sns.distplot(X[:, 0], fit=norm)
plt.title("Feature 0 (log-normal)")

plt.subplot(2, 2, 2)
sns.distplot(X[:, 1], fit=norm)
plt.title("Feature 1 (Poisson)")

plt.subplot(2, 2, 3)
# plt.hist(Xt[:,0], bins=20)
sns.distplot(Xt[:, 0], fit=norm)
plt.title("Transformed Feature 0")

plt.subplot(2, 2, 4)
sns.distplot(Xt[:, 1], fit=norm)
plt.title("Transformed Feature 1")

plt.tight_layout()
plt.show()

# %%
