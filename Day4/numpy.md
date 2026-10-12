# NumPy for Machine Learning — Complete Guide

A comprehensive guide to **NumPy (Numerical Python)**, covering the essential concepts, functions, and mathematical operations required for Machine Learning, Data Science, and Artificial Intelligence.

## 📌 Table of Contents

- [Introduction to NumPy](#-introduction-to-numpy)
- [Why NumPy for Machine Learning?](#-why-numpy-for-machine-learning)
- [Installation](#-installation)
- [Import NumPy](#-import-numpy)
- [Creating NumPy Arrays](#-creating-numpy-arrays)
- [Array Attributes](#-array-attributes)
- [Array Data Types](#-array-data-types)
- [Indexing and Slicing](#-indexing-and-slicing)
- [Array Reshaping](#-array-reshaping)
- [Array Operations](#-array-operations)
- [Mathematical Functions](#-mathematical-functions)
- [Statistical Functions](#-statistical-functions)
- [Broadcasting](#-broadcasting)
- [Boolean Indexing and Filtering](#-boolean-indexing-and-filtering)
- [Sorting and Searching](#-sorting-and-searching)
- [Random Number Generation](#-random-number-generation)
- [Linear Algebra](#-linear-algebra)
- [Handling Missing Values](#-handling-missing-values)
- [Copy vs View](#-copy-vs-view)
- [Saving and Loading Arrays](#-saving-and-loading-arrays)
- [NumPy for Machine Learning](#-numpy-for-machine-learning)
- [Common NumPy Functions](#-common-numpy-functions)
- [Practice Exercises](#-practice-exercises)
- [Best Practices](#-best-practices)
- [Learning Resources](#-learning-resources)

---

## 📖 Introduction to NumPy

**NumPy (Numerical Python)** is a fundamental Python library for numerical computing. It provides multidimensional arrays, mathematical functions, statistical operations, linear algebra, and random number generation.

NumPy is widely used in:

- Machine Learning
- Deep Learning
- Data Science
- Data Analysis
- Scientific Computing
- Artificial Intelligence
- Data Preprocessing

## 🚀 Why NumPy for Machine Learning?

NumPy is essential for understanding how machine learning algorithms process numerical data.

- Efficient storage and manipulation of numerical data.
- Fast vectorized mathematical operations.
- Matrix multiplication and linear algebra.
- Statistical analysis and feature transformations.
- Random number generation for simulations and model initialization.
- Foundation for libraries such as Pandas, SciPy, and many machine learning frameworks.

## 📦 Installation

Install NumPy using pip:

```bash
pip install numpy
```

Verify the installation:

```python
import numpy as np

print(np.__version__)
```

## 🔰 Import NumPy

The standard convention is to import NumPy using the alias `np`.

```python
import numpy as np
```

## 🧮 Creating NumPy Arrays

### 1. One-Dimensional Array

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr)
```

### 2. Two-Dimensional Array

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
```

### 3. Three-Dimensional Array

```python
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(arr)
```

### 4. Special Arrays

```python
np.zeros((2, 3))       # Array filled with zeros
np.ones((2, 3))        # Array filled with ones
np.full((2, 3), 7)     # Array filled with a specified value
np.eye(3)              # Identity matrix
np.empty((2, 3))       # Uninitialized array
```

### 5. Range-Based Arrays

```python
np.arange(0, 10, 2)    # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)   # Five equally spaced values
```

## 📊 Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ndim)    # Number of dimensions
print(arr.shape)   # Dimensions of the array
print(arr.size)    # Total number of elements
print(arr.dtype)   # Data type of elements
print(arr.itemsize) # Bytes used by each element
```

Understanding `shape` is especially important because machine learning algorithms typically expect features in a two-dimensional matrix.

## 🔢 Array Data Types

NumPy supports multiple numerical data types.

```python
a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1.5, 2.5, 3.5], dtype=np.float64)

print(a.dtype)
print(b.dtype)
```

Convert an array's data type:

```python
arr = np.array([1.2, 2.7, 3.9])

converted = arr.astype(np.int32)
print(converted)
```

Common types include:

- `int32`, `int64`
- `float32`, `float64`
- `bool_`
- `complex128`

## ✂️ Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])      # First element
print(arr[-1])     # Last element
print(arr[1:4])    # Elements from index 1 to 3
print(arr[::2])    # Every second element
```

### Two-Dimensional Indexing

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr[0, 1])   # 2
print(arr[1, 2])   # 6
print(arr[:, 0])   # First column
print(arr[1, :])   # Second row
```

## 🔄 Array Reshaping

Reshaping changes the dimensions of an array without changing its elements.

```python
arr = np.arange(1, 7)

print(arr.reshape(2, 3))
print(arr.reshape(3, 2))
print(arr.reshape(-1, 1))  # Column vector
print(arr.reshape(1, -1))  # Row vector
```

Other useful operations:

```python
arr = np.array([[1, 2], [3, 4]])

print(arr.flatten())        # Returns a copy
print(arr.ravel())          # Returns a flattened view when possible
print(arr.T)                # Transpose
print(np.expand_dims(arr, axis=0))
print(np.squeeze(np.array([[[1, 2, 3]]])))
```

## ➕ Array Operations

### Arithmetic Operations

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a % 3)
```

### Element-Wise Operations vs Matrix Multiplication

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a * b)   # Element-wise multiplication
print(a @ b)   # Matrix multiplication
print(np.dot(a, b))
```

### Aggregation Operations

```python
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.prod(arr))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
```

## 📐 Mathematical Functions

```python
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))
print(np.square(arr))
print(np.exp(arr))
print(np.log(arr))
print(np.log10(arr))
print(np.abs(np.array([-1, -2, 3])))
```

### Rounding Functions

```python
arr = np.array([1.234, 2.567, 3.891])

print(np.round(arr, 2))
print(np.floor(arr))
print(np.ceil(arr))
print(np.trunc(arr))
```

### Trigonometric Functions

```python
angles = np.array([0, np.pi / 2, np.pi])

print(np.sin(angles))
print(np.cos(angles))
print(np.tan(angles))
```

## 📈 Statistical Functions

Statistics are important for understanding datasets and preparing features for machine learning.

```python
data = np.array([10, 20, 30, 40, 50])

print(np.mean(data))       # Mean
print(np.median(data))     # Median
print(np.std(data))        # Standard deviation
print(np.var(data))        # Variance
print(np.min(data))        # Minimum
print(np.max(data))        # Maximum
print(np.percentile(data, 75))
print(np.quantile(data, 0.25))
```

### Axis-Based Operations

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.sum(data, axis=0))   # Column sums
print(np.sum(data, axis=1))   # Row sums

print(np.mean(data, axis=0))
print(np.std(data, axis=0))
```

**Remember:**

- `axis=0` operates down the rows, producing column-wise results.
- `axis=1` operates across the columns, producing row-wise results.

## 📡 Broadcasting

Broadcasting allows NumPy to perform operations on arrays of compatible shapes without manually repeating data.

```python
arr = np.array([10, 20, 30])

print(arr + 5)
print(arr * 2)
```

### Broadcasting with Matrices

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

print(matrix + vector)
```

Broadcasting is useful for feature scaling, normalization, and vectorized calculations.

## 🔍 Boolean Indexing and Filtering

```python
arr = np.array([10, 15, 20, 25, 30])

print(arr[arr > 20])
print(arr[arr % 2 == 0])
```

### Multiple Conditions

```python
arr = np.array([10, 15, 20, 25, 30])

filtered = arr[(arr >= 15) & (arr <= 25)]
print(filtered)
```

Use `&`, `|`, and `~` for element-wise logical conditions, with parentheses around each comparison.

### Replace Values Conditionally

```python
arr = np.array([10, 20, 30, 40])

result = np.where(arr > 20, 1, 0)
print(result)
```

## 🔎 Sorting and Searching

```python
arr = np.array([40, 10, 30, 20])

print(np.sort(arr))
print(np.argsort(arr))
print(np.argmax(arr))
print(np.argmin(arr))
print(np.where(arr > 20))
print(np.unique(np.array([1, 2, 2, 3, 3, 3])))
```

Useful for ranking, finding extrema, and analyzing class labels.

## 🎲 Random Number Generation

Random numbers are useful for simulations, sampling, and model initialization.

Use NumPy's recommended `default_rng` interface.

```python
rng = np.random.default_rng(42)

print(rng.random(5))
print(rng.integers(1, 10, size=5))
print(rng.normal(0, 1, size=5))
```

### Sampling and Shuffling

```python
rng = np.random.default_rng(42)

data = np.array([10, 20, 30, 40, 50])

print(rng.choice(data, size=3, replace=False))

shuffled = rng.permutation(data)
print(shuffled)
```

A fixed seed makes results reproducible when the same operations are performed in the same environment and sequence.

## 🧠 Linear Algebra

Linear algebra is fundamental to machine learning algorithms such as linear regression, neural networks, and dimensionality reduction.

### Matrix Multiplication

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)
```

### Dot Product

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))
```

### Transpose

```python
A = np.array([[1, 2, 3], [4, 5, 6]])

print(A.T)
```

### Determinant and Inverse

```python
A = np.array([[4.0, 7.0], [2.0, 6.0]])

print(np.linalg.det(A))
print(np.linalg.inv(A))
```

An inverse exists only for invertible square matrices. In practice, avoid explicitly computing matrix inverses when solving linear systems.

### Solve Linear Systems

```python
A = np.array([[3.0, 1.0], [1.0, 2.0]])
b = np.array([9.0, 8.0])

solution = np.linalg.solve(A, b)
print(solution)
```

### Norms and Eigenvalues

```python
A = np.array([[2.0, 0.0], [0.0, 3.0]])

print(np.linalg.norm(A))
print(np.linalg.eig(A))
```

### Singular Value Decomposition

```python
A = np.array([[1.0, 2.0], [3.0, 4.0]])

U, S, Vt = np.linalg.svd(A)

print(U)
print(S)
print(Vt)
```

SVD is an important mathematical foundation for dimensionality reduction techniques such as PCA.

## 🧹 Handling Missing Values

NumPy commonly represents missing numerical values with `np.nan`.

```python
data = np.array([10.0, 20.0, np.nan, 40.0])

print(np.isnan(data))
print(np.nanmean(data))
print(np.nanmedian(data))
```

### Remove Missing Values

```python
clean_data = data[~np.isnan(data)]
print(clean_data)
```

### Replace Missing Values

```python
mean_value = np.nanmean(data)
filled_data = np.where(np.isnan(data), mean_value, data)

print(filled_data)
```

In machine learning workflows, calculate imputation values using the training data only, then apply those learned values to validation and test data to prevent data leakage.

## 🔗 Copy vs View

A **view** shares the original array's data when possible, while a **copy** creates independent data.

```python
arr = np.array([10, 20, 30])

view = arr[1:]
view[0] = 99

print(arr)  # Original array changes

copy = arr.copy()
copy[0] = 100

print(arr)  # Original array remains unchanged
```

Understanding views and copies helps avoid unintended data modification during preprocessing.

## 💾 Saving and Loading Arrays

### Save as a Binary File

```python
arr = np.array([10, 20, 30, 40])

np.save("data.npy", arr)

loaded = np.load("data.npy")
print(loaded)
```

### Save Multiple Arrays

```python
np.savez("dataset.npz", features=np.array([1, 2, 3]), labels=np.array([0, 1, 0]))

data = np.load("dataset.npz")

print(data["features"])
print(data["labels"])
```

### Save as CSV-Compatible Text

```python
arr = np.array([[1, 2], [3, 4]])

np.savetxt("data.csv", arr, delimiter=",", fmt="%d")

loaded = np.loadtxt("data.csv", delimiter=",")
print(loaded)
```

Only load `.npy` or `.npz` files from trusted sources when object arrays or pickle loading are involved. Avoid enabling pickle loading for untrusted files.

## 🤖 NumPy for Machine Learning

### 1. Represent Features and Labels

```python
X = np.array([
    [1500, 3],
    [2000, 4],
    [2500, 4],
    [3000, 5]
], dtype=float)

y = np.array([30, 40, 50, 60])

print("Features:", X)
print("Labels:", y)
print("Feature shape:", X.shape)
print("Label shape:", y.shape)
```

Here, `X` contains two features per sample, while `y` contains one target value per sample.

### 2. Feature Scaling with Min-Max Scaling

```python
X = np.array([
    [10.0, 100.0],
    [20.0, 200.0],
    [30.0, 300.0]
])

minimum = X.min(axis=0)
maximum = X.max(axis=0)

X_scaled = (X - minimum) / (maximum - minimum)

print(X_scaled)
```

For a constant feature, the denominator is zero; handle that case explicitly in production code. Fit scaling parameters on training data only.

### 3. Standardization

```python
mean = X.mean(axis=0)
std = X.std(axis=0)

std = np.where(std == 0, 1, std)
X_standardized = (X - mean) / std

print(X_standardized)
```

This example uses the population standard deviation (`ddof=0`). In practical workflows, fit the mean and standard deviation on training data only.

### 4. Calculate Mean Squared Error

```python
actual = np.array([100, 150, 200, 250])
predicted = np.array([110, 140, 210, 240])

mse = np.mean((actual - predicted) ** 2)

print("Mean Squared Error:", mse)
```

Mean Squared Error (MSE) measures the average squared difference between actual and predicted values.

### 5. Implement Linear Regression Predictions

```python
X = np.array([
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0]
])

weights = np.array([2.0, 3.0])
bias = 1.0

predictions = X @ weights + bias

print(predictions)
```

The prediction equation is:

\[
\hat{y} = Xw + b
\]

Where:

- \(X\) represents the feature matrix.
- \(w\) represents model weights.
- \(b\) represents the bias.
- \(\hat{y}\) represents predicted values.

### 6. Calculate a Sigmoid Function

```python
z = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

sigmoid = 1 / (1 + np.exp(-z))

print(sigmoid)
```

The sigmoid function is commonly used to convert model scores into values between 0 and 1. For extreme inputs, use a numerically stable implementation.

### 7. One-Hot Encoding

```python
labels = np.array([0, 2, 1, 2])
num_classes = 3

one_hot = np.eye(num_classes)[labels]

print(one_hot)
```

One-hot encoding represents each class as a binary vector. Validate that class indices fall within the expected range.

### 8. Calculate Cosine Similarity

```python
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])

similarity = np.dot(a, b) / (
    np.linalg.norm(a) * np.linalg.norm(b)
)

print("Cosine Similarity:", similarity)
```

Cosine similarity measures the angle-based similarity between two nonzero vectors and is often used in text analysis and recommendation systems.

## 📚 Common NumPy Functions

| Function | Purpose |
|---|---|
| `np.array()` | Create an array |
| `np.arange()` | Generate evenly stepped values |
| `np.linspace()` | Generate equally spaced values |
| `np.zeros()` | Create an array of zeros |
| `np.ones()` | Create an array of ones |
| `np.reshape()` | Change array shape |
| `np.concatenate()` | Join arrays along an axis |
| `np.vstack()` | Stack arrays vertically |
| `np.hstack()` | Stack arrays horizontally |
| `np.mean()` | Calculate the mean |
| `np.median()` | Calculate the median |
| `np.std()` | Calculate standard deviation |
| `np.var()` | Calculate variance |
| `np.sum()` | Calculate the sum |
| `np.argmax()` | Index of the maximum |
| `np.argmin()` | Index of the minimum |
| `np.where()` | Select based on a condition |
| `np.unique()` | Find unique values |
| `np.dot()` | Dot product |
| `np.linalg.solve()` | Solve a linear system |
| `np.random.default_rng()` | Create a random generator |
| `np.isnan()` | Identify NaN values |

## 📝 Practice Exercises

Practice the following exercises to strengthen your NumPy skills for machine learning.

### Beginner Level

- [ ] Create one-dimensional, two-dimensional, and three-dimensional arrays.
- [ ] Explore array shape, size, dimensions, and data types.
- [ ] Perform arithmetic operations on arrays.
- [ ] Practice indexing, slicing, and reshaping.
- [ ] Calculate mean, median, standard deviation, and variance.

### Intermediate Level

- [ ] Filter an array using multiple Boolean conditions.
- [ ] Perform broadcasting operations.
- [ ] Combine arrays using `concatenate()`, `vstack()`, and `hstack()`.
- [ ] Generate random samples with a fixed seed.
- [ ] Handle missing values and duplicate values.
- [ ] Implement min-max scaling and standardization.
- [ ] Calculate Mean Squared Error.

### Advanced Level

- [ ] Implement linear regression predictions using matrix multiplication.
- [ ] Solve a system of linear equations.
- [ ] Implement one-hot encoding.
- [ ] Calculate cosine similarity.
- [ ] Implement a numerically stable sigmoid function.
- [ ] Build a simple gradient descent algorithm using NumPy.
- [ ] Implement a basic train-test split using random indices.

## ✅ Best Practices

- Use vectorized operations instead of unnecessary Python loops.
- Understand array shapes before performing matrix operations.
- Choose appropriate data types to balance precision and memory usage.
- Use `np.random.default_rng()` for modern random number generation.
- Avoid unnecessary array copies.
- Handle missing values and divide-by-zero cases explicitly.
- Prevent data leakage by fitting preprocessing parameters on training data only.
- Use `@` or `np.matmul()` for matrix multiplication.
- Prefer `np.linalg.solve()` over explicitly calculating a matrix inverse when solving linear systems.
- Validate dimensions and input values before applying machine learning algorithms.

## 🗺️ Recommended Learning Path

1. NumPy fundamentals and array creation.
2. Array attributes, data types, indexing, and slicing.
3. Mathematical, statistical, and aggregation functions.
4. Broadcasting, filtering, and reshaping.
5. Random number generation and linear algebra.
6. Missing-value handling and array manipulation.
7. Feature scaling and machine learning mathematics.
8. Implement basic machine learning algorithms from scratch.
9. Continue with Pandas, Matplotlib, Seaborn, and Scikit-learn.

## 📖 Learning Resources

- [Official NumPy Documentation](https://numpy.org/doc/stable/)
- [NumPy Beginner's Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy Reference](https://numpy.org/doc/stable/reference/index.html)

---

## 🎯 Conclusion

NumPy is one of the most important foundations for Machine Learning with Python. Mastering arrays, vectorized operations, broadcasting, statistics, linear algebra, and numerical computation will help you understand how machine learning algorithms manipulate and process data.

**Learn NumPy → Practice Data Analysis → Master Data Preprocessing → Build Machine Learning Models.**

⭐ If this guide helps you, consider starring the repository and contributing to its improvement.
