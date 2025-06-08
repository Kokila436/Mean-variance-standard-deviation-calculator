# Mean-variance-standard-deviation-calculator
import numpy as np

def calculate(input_list):
    # Check if input list has exactly 9 elements
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the input list to a 3x3 NumPy array
    matrix = np.array(input_list).reshape(3, 3)
    
    # Calculate mean
    mean_axis1 = matrix.mean(axis=0).tolist()
    mean_axis2 = matrix.mean(axis=1).tolist()
    mean_flattened = matrix.mean().tolist()

    # Calculate variance
    variance_axis1 = matrix.var(axis=0).tolist()
    variance_axis2 = matrix.var(axis=1).tolist()
    variance_flattened = matrix.var().tolist()

    # Calculate standard deviation
    std_axis1 = matrix.std(axis=0).tolist()
    std_axis2 = matrix.std(axis=1).tolist()
    std_flattened = matrix.std().tolist()

    # Calculate max
    max_axis1 = matrix.max(axis=0).tolist()
    max_axis2 = matrix.max(axis=1).tolist()
    max_flattened = matrix.max().tolist()

    # Calculate min
    min_axis1 = matrix.min(axis=0).tolist()
    min_axis2 = matrix.min(axis=1).tolist()
    min_flattened = matrix.min().tolist()

    # Calculate sum
    sum_axis1 = matrix.sum(axis=0).tolist()
    sum_axis2 = matrix.sum(axis=1).tolist()
    sum_flattened = matrix.sum().tolist()

    # Return the dictionary as specified
    return {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [variance_axis1, variance_axis2, variance_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

print("Mean:")
print("  Columns:", result['mean'][0])
print("  Rows:", result['mean'][1])
print("  Overall:", result['mean'][2])

print("\nVariance:")
print("  Columns:", result['variance'][0])
print("  Rows:", result['variance'][1])
print("  Overall:", result['variance'][2])

print("\nStandard Deviation:")
print("  Columns:", result['standard deviation'][0])
print("  Rows:", result['standard deviation'][1])
print("  Overall:", result['standard deviation'][2])

print("\nMax:")
print("  Columns:", result['max'][0])
print("  Rows:", result['max'][1])
print("  Overall:", result['max'][2])

print("\nMin:")
print("  Columns:", result['min'][0])
print("  Rows:", result['min'][1])
print("  Overall:", result['min'][2])

print("\nSum:")
print("  Columns:", result['sum'][0])
print("  Rows:", result['sum'][1])
print("  Overall:", result['sum'][2])
