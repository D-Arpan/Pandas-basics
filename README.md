# Basic Pandas Operations

## Overview
This repository demonstrates the basic operations of the Pandas library using a sample employee dataset. The dataset contains 10 fictional employees with details such as their names, ages, cities, salaries, and performance scores. The project showcases fundamental Pandas operations like creating a DataFrame, saving data, retrieving specific rows/columns, filtering data, and obtaining descriptive statistics.

## Dataset
The dataset consists of the following columns:
- **Name**: Employee's full name
- **Age**: Employee's age
- **City**: Employee's city of residence
- **Salary**: Employee's monthly salary
- **Performance Score**: Employee's performance rating (out of 100)

Example of the dataset:

| Name                    | Age | City         | Salary | Performance Score |
|-------------------------|-----|-------------|--------|------------------|
| Jon Snow               | 25  | Westros     | 50000  | 99               |
| Ross Gellar            | 32  | New York    | 30000  | 70               |
| Ragnar Loathbroke      | 55  | Scandanavia | 40000  | 85               |
| Thomas Shelby         | 35  | London      | 25000  | 42               |
| Adil Qadri            | 50  | Maqsadnagar | 12000  | 51               |
| Chikni Chameli        | 18  | Sheelapur   | 52000  | 98               |
| Genduji Mahaprabhu    | 25  | Chakdaha    | 51000  | 95               |
| Linon Kumar Ghosh     | 15  | Shimurali   | 23000  | 90               |
| Panda Biswas          | 69  | Pompom land | 69000  | 58               |
| Tarini Charan Barujje | 69  | Dholakpur   | 70000  | 77               |

## Key Features & Operations

### 1️⃣ Creating and Saving Data
- The data is stored in a Pandas DataFrame.
- The DataFrame is exported in multiple formats:
  - **CSV** (`mydataframe.csv`)
  - **Excel** (`mydataframe.xlsx`)
  - **JSON** (`mydataframe.json`)

### 2️⃣ Data Exploration
- **Shape of Data**: Retrieves the number of rows and columns.
- **Column Names**: Displays all column names.
- **Data Information**: Provides an overview of data types and memory usage.
- **Descriptive Statistics**: Computes basic statistical measures like mean, standard deviation, min/max values, etc.

### 3️⃣ Retrieving Data
- Selecting specific columns as a **Series** or **DataFrame**.
- Examples:
  ```python
  df['Name']  # Selecting a single column
  df[['Name', 'Salary']]  # Selecting multiple columns
  ```

### 4️⃣ Filtering Data
- **Single Condition Filtering**: Selecting employees with a salary greater than 50,000.
  ```python
  df[df['Salary'] > 50000]
  ```
- **Multiple Conditions (AND)**: Employees with high salary and high performance.
  ```python
  df[(df['Salary'] > 35000) & (df['Performance Score'] > 25)]
  ```
- **Multiple Conditions (OR)**: Employees with either a high salary or young age.
  ```python
  df[(df['Salary'] > 50000) | (df['Age'] < 30)]
  ```

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Run the Jupyter Notebook or Python script to explore the dataset.

## Requirements
- Python 3.x
- Pandas Library

## Author
**Arpan Das**

---
Feel free to explore and modify the code as needed! 🚀

