# Basic Employee Data Analysis with Pandas

This repository contains a simple demonstration of how to create, manipulate, and analyze a dataset using **Pandas** in Python. The dataset consists of employee details such as **Name, Age, City, Salary, and Performance Score**.

## Dataset
The dataset includes the following employees:

| Name                  | Age | City          | Salary | Performance Score |
|----------------------|-----|--------------|--------|------------------|
| Jon Snow            | 25  | Westros      | 50000  | 99               |
| Ross Gellar         | 32  | New York     | 30000  | 70               |
| Ragnar Loathbroke   | 55  | Scandanavia  | 40000  | 85               |
| Thomas Shelby       | 35  | London       | 25000  | 42               |
| Adil Qadri          | 50  | Maqsadnagar  | 12000  | 51               |
| Chikni Chameli      | 18  | Sheelapur    | 52000  | 98               |
| Genduji Mahaprabhu  | 25  | Chakdaha     | 51000  | 95               |
| Linon Kumar Ghosh   | 15  | Shimurali    | 23000  | 90               |
| Panda Biswas        | 69  | Pompom land  | 69000  | 58               |
| Tarini Charan Barujje | 69 | Dholakpur   | 70000  | 77               |

## Features of the Project
- **Creating a DataFrame**: The employee data is stored in a Pandas DataFrame.
- **Saving the DataFrame**: The data is exported in multiple formats:
  - CSV (`mydataframe.csv`)
  - Excel (`mydataframe.xlsx`)
  - JSON (`mydataframe.json`)
- **Data Exploration**:
  - Displaying the shape of the data (number of rows and columns)
  - Listing column names
  - Viewing data information (`df.info()`)
  - Generating summary statistics (`df.describe()`)
- **Data Selection and Filtering**:
  - Selecting single or multiple columns
  - Filtering rows based on conditions (salary, performance score, age, etc.)

## Usage
To run this project, make sure you have Python and Pandas installed. You can install Pandas using:
```sh
pip install pandas
```
Then, run the script in Jupyter Notebook or any Python IDE to explore the dataset and filtering techniques.



