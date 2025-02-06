# Employee Data Analysis with Pandas

## 📌 Project Description
This project is a simple **Employee Data Analysis** tool using Python and Pandas, written in a **Jupyter Notebook**. It demonstrates how to create, manipulate, and filter data in a Pandas DataFrame. The dataset consists of employee details such as **Name, Age, City, Salary, and Performance Score**.

## 🚀 Features
- **Create a DataFrame** from a dictionary.
- **Save DataFrame** in CSV, Excel, and JSON formats.
- **Retrieve basic information** (shape, columns, data types, statistics, etc.).
- **Filter rows** based on conditions.
- **Select single or multiple columns.**
- **Apply multi-condition filtering** using AND (`&`) and OR (`|`).

## 🛠 Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **Install dependencies**
   This project requires **Python** and **Pandas**. Install them using:
   ```bash
   pip install pandas
   ```
3. **Run the Jupyter Notebook**
   Open Jupyter Notebook and load the **.ipynb** file:
   ```bash
   jupyter notebook
   ```

## 📂 Project Files
- `employee_data_analysis.ipynb` → Jupyter Notebook with all analysis
- `mydataframe.csv` → Saved CSV file
- `mydataframe.xlsx` → Saved Excel file
- `mydataframe.json` → Saved JSON file

## 📌 Usage
1. Run the notebook and execute each cell step by step.
2. The script will generate **statistical insights** and **filtered datasets**.
3. Modify the dataset or filtering conditions as needed.

## 🏆 Example Outputs
- **Employees with High Salary (>35,000) and High Performance Score (>25):**
  ```
  Name                 Salary   Performance Score
  Jon Snow            50000         25
  Ragnar Loathbroke   40000         26
  Chikni Chameli      52000         26
  Genduji Mahaprabhu  51000         29
  ```
- **Employees with Salary > 50,000 OR Age < 30:**
  ```
  Name                 Salary   Age
  Jon Snow            50000    25
  Chikni Chameli      52000    18
  Genduji Mahaprabhu  51000    25
  Linon Kumar Ghosh   23000    15
  ```

## 🔥 Future Improvements
- Add **interactive visualizations** using Matplotlib/Seaborn.
- Implement **salary comparison** using NumPy.
- Expand dataset with more employee details.



