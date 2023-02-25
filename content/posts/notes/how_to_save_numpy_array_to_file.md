---
Title: How to save numpy array to file?
Slug: how-to-save-numpy-array-to-file
Date: 2023-02-24
Modified: 2023-02-24
Status: published
Tags: numpy, dataset, machine-learning 
Category: note
---

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Save/Load single array](#saveload-single-array)
- [Save/Load multiple arrays](#saveload-multiple-arrays)

<!-- /MarkdownTOC -->

<a id="saveload-single-array"></a>
## Save/Load single array
To save a NumPy array to a file, you can use the `np.save` function. The `np.save` function can save a NumPy array to a binary file with a `.npy` extension.

```python
import numpy as np

# Create a NumPy array
my_array = np.array([1, 2, 3, 4, 5])

# Save the array to a file
np.save('my_array.npy', my_array)

```

To load the saved array back into memory, you can use the `np.load` function:
```python
# Load the saved array from the file
loaded_array = np.load('my_array.npy')

# Print the loaded array
print(loaded_array)
```

> **Note:** you can also save multiple arrays to a single file using `np.savez`, which creates a compressed archive of the arrays with a `.npz` extension.

<a id="saveload-multiple-arrays"></a>
## Save/Load multiple arrays
```python
import numpy as np

# Create some example data
X = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([0, 1])

# Save the arrays to a file
np.savez('my_data.npz', X=X, y=y)

# Load the arrays from the file
loaded_data = np.load('my_data.npz')
X_loaded = loaded_data['X']
y_loaded = loaded_data['y']

# Print the loaded arrays
print('X:', X_loaded)
print('y:', y_loaded)

```