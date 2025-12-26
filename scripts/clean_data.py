import pandas as pd

# -------------------------------------------------
# 1. Load the raw dataset
# -------------------------------------------------
# HOW IT WORKS:
# Pandas reads the CSV file and loads it into a DataFrame (a table in memory).
df = pd.read_csv('data/train.csv')


# -------------------------------------------------
# 2. Drop unnecessary columns
# -------------------------------------------------
# HOW IT WORKS:
# Pandas creates a new version of the DataFrame without these columns.
df = df.drop(columns=['Cabin', 'Ticket'])


# -------------------------------------------------
# 3. Fill missing values
# -------------------------------------------------
# HOW IT WORKS:
# fillna() replaces missing values.
# median() finds the middle value.
# mode()[0] finds the most common value.
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


# -------------------------------------------------
# 4. Rename columns
# -------------------------------------------------
# HOW IT WORKS:
# rename() creates a new DataFrame with updated column names.
df = df.rename(columns={
    'Survived': 'survived',
    'Pclass': 'passenger_class',
    'SibSp': 'siblings_spouses',
    'Parch': 'parents_children'
})


# -------------------------------------------------
# 5. Filter rows
# -------------------------------------------------
# HOW IT WORKS:
# df['Age'] > 0 creates a True/False filter.
# Pandas keeps only the rows where the condition is True.
df = df[df['Age'] > 0]


# -------------------------------------------------
# 6. Save the cleaned dataset
# -------------------------------------------------
# HOW IT WORKS:
# to_csv() writes the DataFrame to a new CSV file.
# index=False prevents row numbers from being added.
df.to_csv('data/cleaned_titanic.csv', index=False)

print("Cleaning complete. File saved to data/cleaned_titanic.csv")
