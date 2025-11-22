import numpy as np

# -------------------------
# 1. Basic Array Creation
# -------------------------
one_dimensional_arr = np.array([10, 12])
print(one_dimensional_arr)

a = np.array([1, 2, 3])
print(a)

b = np.arange(3)
print(b)

c = np.arange(1, 20, 3)
print(c)

# Linspace examples
lin_spaced_arr = np.linspace(0, 100, 5)
print(lin_spaced_arr)

lin_spaced_arr_int = np.linspace(0, 100, 5, dtype=int)
print(lin_spaced_arr_int)

c_int = np.arange(1, 20, 3, dtype=int)
print(c_int)

b_float = np.arange(3, dtype=float)
print(b_float)

char_arr = np.array(['Welcome to Math for ML!'])
print(char_arr)
print(char_arr.dtype)

# -------------------------
# 2. Special Arrays
# -------------------------
ones_arr = np.ones(3)
print(ones_arr)

zeros_arr = np.zeros(3)
print(zeros_arr)

empt_arr = np.empty(3)
print(empt_arr)

rand_arr = np.random.rand(3)
print(rand_arr)

# 2-D array
two_dim_arr = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim_arr)

# Reshaping
one_dim_arr = np.array([1, 2, 3, 4, 5, 6])
multi_dim_arr = np.reshape(one_dim_arr, (2, 3))
print(multi_dim_arr)
print(multi_dim_arr.ndim)
print(multi_dim_arr.shape)
print(multi_dim_arr.size)

# -------------------------
# 3. Array Math Operations
# -------------------------
arr_1 = np.array([2, 4, 6])
arr_2 = np.array([1, 3, 5])

print(arr_1 + arr_2)
print(arr_1 - arr_2)
print(arr_1 * arr_2)

# Broadcasting
vector = np.array([1, 2])
print(vector * 1.6)

# -------------------------
# 4. Indexing and Slicing
# -------------------------
a = [1, 2, 3, 4, 5]
print(a[2])  # third element
print(a[0])  # first element

two_dim = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(two_dim[2][1])  # element 8

# Slicing examples
print(a[1:4])
print(a[:3])
print(a[2:])
print(a[::2])
print(a == a[:] == a[::])

print(two_dim[0:2])
print(two_dim[1:3])
print(two_dim[:, 1])

# -------------------------
# 5. Stacking
# -------------------------
a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

print(a1)
print(a2)

print(np.vstack((a1, a2)))
print(np.hstack((a1, a2)))
