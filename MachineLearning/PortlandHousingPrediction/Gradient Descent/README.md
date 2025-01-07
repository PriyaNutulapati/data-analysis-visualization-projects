# Gradient Descent for Simple Linear Regression

## **Project Description**
This project demonstrates the implementation of the **Gradient Descent algorithm** for simple linear regression using a dataset of housing prices and sizes. The program standardizes the data using **min-max normalization** and performs regression to estimate the relationship between the price of a house and its size.

## **Features**
- **Standardization of Data:** Min-max normalization to scale data between 0 and 1.
- **Gradient Descent Implementation:** Custom implementation for estimating the intercept and coefficient of the regression line.
- **Stop Criteria:** Stops iterations when the absolute step size for both parameters is smaller than 0.0001.
- **Dataset Handling:** Reads data directly from a CSV file.

## **Dataset**
The dataset used in this project is **`portland_housing_full.csv`**, which contains the following columns:
1. **Size:** Size of the house (column 0).
2. **Price:** Price of the house (column 2).

## **Usage**
### **Functions**
#### `read_column(filename, col)`
- Reads a specific column from the dataset.
- **Parameters:**
  - `filename`: The name of the CSV file.
  - `col`: The column index to be read.
- **Returns:** A list of integers from the specified column.

#### `standardize(data)`
- Applies min-max normalization to a list of numbers.
- **Parameters:**
  - `data`: List of numerical data.
- **Returns:** A list of normalized floating-point numbers between 0 and 1.

#### `gradient_descent(x, y, lr, a=0, b=0)`
- Implements the gradient descent algorithm for simple linear regression.
- **Parameters:**
  - `x`: List of input variable values.
  - `y`: List of target variable values.
  - `lr`: Learning rate for gradient descent.
  - `a`: Initial guess for intercept (default 0).
  - `b`: Initial guess for coefficient (default 0).
- **Returns:**
  - `a`: Final estimate of intercept.
  - `b`: Final estimate of coefficient.

### **Execution Steps**
1. Clone the repository and ensure the dataset **`portland_housing_full.csv`** is in the same folder as the script.
2. Run the program with the following command:
   ```bash
   python gradient_descent.py


### **Expected Output**
The GD estimate of regression of Price on Size is price = 0.0310 + 0.9180 * size.


### **File Structure**
 
```text
|-- gradient_descent.py      # Main script implementing the algorithm
|-- portland_housing_full.csv # Dataset file
|-- README.md                # Project documentation

