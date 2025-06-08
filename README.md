# 📊 Mean, Variance, and Standard Deviation Calculator

This project is a simple Python program that takes a list of 9 numbers and calculates the following:

- Mean
- Variance
- Standard Deviation
- Maximum
- Minimum
- Sum

Calculations are done:
- Across rows
- Across columns
- On the flattened array

---

### 🧮 How It Works

It uses the NumPy library to reshape the list into a 3x3 matrix and calculate the statistics:

```python
matrix = np.array(input_list).reshape(3, 3)

# Example:
mean_axis1 = matrix.mean(axis=0).tolist()
mean_axis2 = matrix.mean(axis=1).tolist()
mean_flattened = matrix.mean().tolist()
