# Python Tools & Concepts Used in This Project
A clear, beginner‑friendly explanation of everything used to complete the Titanic Data Cleaning project.

---

# 1. Python
Python is the core programming language used in this project. It provides:

- Clean, readable syntax  
- A massive ecosystem of data tools  
- Strong support for data cleaning, analysis, and automation  

In this project, Python was used to:

- Load data  
- Inspect missing values  
- Clean and transform columns  
- Save cleaned datasets  
- Build a reusable cleaning script  

---

# 2. Pandas
Pandas is the primary data manipulation library in Python. It provides the DataFrame, which is like a spreadsheet in code.

### Why Pandas was used
- Easy CSV loading  
- Powerful data cleaning functions  
- Built‑in handling of missing values  
- Simple filtering and transformation  
- Clean syntax for renaming and dropping columns  

### Key Pandas functions used
| Function | Purpose |
|---------|---------|
| `read_csv()` | Load raw data into a DataFrame |
| `isnull().sum()` | Count missing values per column |
| `drop()` | Remove unnecessary columns |
| `fillna()` | Replace missing values |
| `median()` | Compute the middle value of a numeric column |
| `mode()` | Find the most common value |
| `rename()` | Clean up column names |
| `df[df['col'] > X]` | Filter rows based on conditions |
| `to_csv()` | Save cleaned data |

---

# 3. Jupyter Notebooks
Jupyter notebooks were used for exploration, learning, and step‑by‑step cleaning.

### Why notebooks are ideal for this project
- Run code in small chunks  
- See results immediately  
- Add explanations between code cells  
- Great for learning and documenting your thought process  
- Perfect for data cleaning and exploratory data analysis

Your notebook shows:

- The raw dataset  
- Missing value checks  
- Cleaning steps  
- Final cleaned output  

---

# 4. Python Scripts (`clean_data.py`)
The script version is the production‑ready version of your notebook.

### Why create a script?
- Reusable  
- Automatable  
- Can be run from the command line  
- Shows you understand how to convert exploration into production  
- Demonstrates engineering discipline  

### What the script does
- Loads raw data  
- Checks for missing values  
- Cleans the dataset  
- Saves the cleaned file  
- Prints progress messages  

---

# 5. Git & GitHub
Git and GitHub were used for:

- Version control  
- Tracking changes  
- Committing updates  
- Pushing your project online  
- Building a professional portfolio  

### Key Git concepts used
| Concept | Meaning |
|--------|---------|
| Commit | A snapshot of your work |
| Push | Send commits to GitHub |
| Sync | Pull and push combined |
| Branch | A separate line of development |
| Repo | Your project folder stored online |

You also learned:

- How to delete files  
- How to amend commit messages  
- How to fix notebook issues  
- How to structure a clean repo  

---

# 6. Project Structure
Your project follows a clean, professional layout:

- data/ train.csv cleaned_titanic.csv  
- notebooks/ titanic_cleaning.ipynb  
- scripts/ clean_data.py  
- README.md docs/ python_tools_breakdown.md


### Why this structure matters
- Easy to navigate  
- Separates raw data from code  
- Keeps notebooks and scripts organized  
- Matches real‑world data engineering patterns  

---

# 7. ETL Concepts
This project demonstrates a full ETL pipeline.

### Extract
Load raw CSV data using Pandas.

### Transform
- Drop columns  
- Fill missing values  
- Rename columns  
- Filter rows  
- Validate data  

### Load
Save the cleaned dataset back to the `data` folder.

---

# 8. Tools Used
| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data cleaning and manipulation |
| Jupyter Notebook | Exploration and documentation |
| VS Code | Code editing and Git integration |
| Git | Version control |
| GitHub | Portfolio hosting |

---

# 9. What You Learned
- How to structure a data project  
- How to clean data using Pandas  
- How to write a reusable Python script  
- How to use Git and GitHub professionally  
- How to document your work  
- How to think like a data engineer  

---

# 10. Future Extensions
This project can grow into:

### 1. A Python dashboard
Using:
- Streamlit  
- Plotly Dash  
- Plotly Express  

### 2. A Power BI dashboard
Using the cleaned CSV.

### 3. A SQL practice dataset
Load the cleaned data into SQLite or PostgreSQL.

### 4. A machine learning model
Predict survival using scikit‑learn.

### 5. A full ETL pipeline
Using:
- Python  
- Airflow  
- Prefect  
- Azure Data Factory  
