
def read_column(portland_housing_full, col):
    with open(portland_housing_full) as file:
        result = []
        next(file)
        for line in file:
            row = line.strip().split(',')
            result.append(int(row[col]))
        return result

def standardize(data):
    # Implemented min-max standardization
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def gradient_descent(x, y, lr, a=0, b=0):
    # Implemented gradient descent
    step_size_a = 1
    step_size_b = 1

    # Loop until both step sizes are smaller than the threshold
    while abs(step_size_a) >= 0.0001 or abs(step_size_b) >= 0.0001:
        gradient_a = -2 * sum([y_i - (a + b * x_i) for x_i, y_i in zip(x, y)])
        gradient_b = -2 * sum([(y_i - (a + b * x_i)) * x_i for x_i, y_i in zip(x, y)])

        step_size_a = gradient_a * lr
        step_size_b = gradient_b * lr

        a -= step_size_a
        b -= step_size_b

    return a, b

# Read data
sizes = read_column('portland_housing_full.csv', 0)
prices = read_column('portland_housing_full.csv', 2)

# Standardize data
prices_std = standardize(prices)
sizes_std = standardize(sizes)

# Perform gradient descent
a, b = gradient_descent(sizes_std, prices_std, 0.01)

# Print the result
print(f'The GD estimate of regression of Price on Size is price = {a:.4f} + {b:.4f} * size.')
