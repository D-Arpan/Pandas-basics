#creating a dataframe
import pandas as pd

employees = {
    "Name" : ['Jon Snow', 'Ross Gellar', 'Ragnar Loathbroke', 'Thomas Shelby','Adil Qadri','Chikni Chameli','Genduji Mahaprabhu','Linon Kumar Ghosh'],
    "Age" : [25,32,55,35,50,18,25,15],
    "City": ['Westros', 'New York', 'Scandanavia', 'London','Maqsadnagar','Sheelapur','Chakdaha','Shimurali'],
    "Salary" : [50000,30000,40000,25000,12000,52000,51000,23000],
    "Performance Score" : [25,30,26,10,30,26,29,26]
}

df = pd.DataFrame(employees)

df.to_csv('mydataframe.csv',index=False) ##saving the dataframe as csv file
df.to_excel('mydataframe.xlsx',index=False) ##saving the dataframe as excel file
df.to_json('mydataframe.json',index=False) ##saving the dataframe as json file


# shape of the data
print(f'\n\n NUMBER OF ROWS AND COLUMNS : {df.shape} \n')

# column names  
print(f'\n\n NAME OF THE COLUMNS : {df.columns}\n')


# data information
print('\n\n DATA INFORMATION \n')
print(df.info())

# descriptive statistics
print('\n DESCRIPTIVE STATISTICS \n')
print(df.describe())


'''
1 - select specific columns
2 - filter rows
3 - combine multiple conditions

SELECTING COLUMNS : square brackets
ROWS FILTERING : boolean conditions

Selecting columns :
a - a series 
b - dataframe ( with multiple columns of data)

column = df["column name"]
multi_column = df[["column1","column2",...,...]]

Filtering rowns :
a - boolean indexing

A. Based on a single condition : 
filtered_rows = df [df["Salary"] > 50000]

B. Based on multiple conditions :
filtered_rows = df [(df ["salary"] > 50000) & (df ["salary"] > 80000)]
'''

# selecting single column 
name = df['Name']
print("\n\n'NAME' COLUMN :")
print(name)

# selecting multiple columns
name_salary = df[['Name','Salary']]
print("\n\n'NAME' AND 'SALARY' COLUMNS :")
print(name_salary)


# filtering rows on the basis of single condition 
high_salary = df[df['Salary'] > 35000]
print("\n\nEMPLOYEES WITH HIGH SALARY")
print(high_salary)

#  filtering rows on the basis of multiple conditions (usidng AND)
high_salary_and_performance_score = df[(df['Salary'] > 35000) & (df['Performance Score'] > 25)]
print("\n\nEMPLOYEES WITH HIGH SALARY AND HIGH PERFORMANCE SCORE")
print(high_salary_and_performance_score)

# filtering rows on the basis of multiple conditions (using OR)
high_salary_or_low_age = df[(df['Salary'] > 50000) | (df['Age'] < 30)]
print("\n\nEMPLOYEES WITH HIGH SALARY OR LOW AGE")
print(high_salary_or_low_age)

