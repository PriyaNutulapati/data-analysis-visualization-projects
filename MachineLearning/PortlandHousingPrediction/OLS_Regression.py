
def read_column(portland_housing_full, col):
    result = []                                # initialize an empty list to store the column data
    with open(portland_housing_full) as f_in:  # open the file and assign the file handler as `f_in`
        next(f_in)                             # skip the header row
        for line in f_in:                      # iterates over each line in the file
            row = line.strip().split(',')      # split line into elements based on commas to get the columns
            result.append(int(row[col]))       # converts the column to integer and adds to result
    return result

def ordinary_least_squares(size, price):
    n = len(size)
    size_sum = sum(size)
    price_sum = sum(price)
    size_mean = size_sum / n
    price_mean = price_sum / n

    num = 0         # numerator
    den = 0         # denominator

    for i in range(n):
        size_diff = size[i] - size_mean
        price_diff = price[i] - price_mean
        num += size_diff * price_diff
        den += size_diff ** 2

    b = num / den
    a = price_mean - b * size_mean
    return a, b

sizes = read_column('portland_housing_full.csv', 0)
prices = read_column('portland_housing_full.csv', 2)

a, b = ordinary_least_squares(sizes, prices)

print(f'The OLS estimate of regression of Price on Size is price = {a:.4f} + {b:.4f} * size.')

# 1. 134.5253 is the coefficient for the variable size. It means that for every unit decrease in size, the price of the house will decrease by $134.5253.
# 2. The loss function used to derive the OLS estimators is the sum of squared residuals (errors). It minimizes the sum of the squared differences between the observed values (y) and the predicted values from the regression model.
