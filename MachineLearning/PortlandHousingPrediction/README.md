# **Ordinary Least Squares (OLS) Regression on Portland Housing Data**

## **Overview**
This project implements a simple linear regression model using the Ordinary Least Squares (OLS) method to estimate the relationship between house size and price. The dataset, `portland_housing_full.csv`, contains three columns: house price, number of bedrooms, and size. The main objectives are:

1. Reading specific columns from the dataset.
2. Implementing a simple linear regression model using OLS.
3. Interpreting the results of the regression analysis.

## **Problem Statement**
Given the dataset `portland_housing_full.csv`, the task is to:
- Extract a specific column from the CSV file.
- Understand and explain the functionality of the `read_column` function.
- Use the OLS method to calculate the intercept and coefficient for the regression model.
- Provide an interpretation of the results.

## **Functions**
### **`read_column(filename, col)`**
This function reads a specific column of data from a CSV file.
- **Input:**
  - `filename`: The path to the input CSV file.
  - `col`: The column index to be read.
- **Output:**
  - A list of integers representing the values in the specified column.
- **Assumptions:**
  - The file contains a header row, which is skipped.
  - All data in the specified column are integers.

### **`ordinary_least_squares(x, y)`**
This function calculates the OLS estimators for simple linear regression.
- **Input:**
  - `x`: A list of independent variable values (e.g., house size).
  - `y`: A list of dependent variable values (e.g., house price).
- **Output:**
  - `a`: The intercept of the regression line.
  - `b`: The coefficient (slope) of the regression line.



### **`Expected Output`**
When executed, the program outputs the following result:
The OLS estimate of regression of Price on Size is price = 71270.4924 + 134.5253 * size.
