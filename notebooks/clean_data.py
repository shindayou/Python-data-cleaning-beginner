import pandas as pd

df = pd.read_csv('data/train.csv')

null_counts = df.isnull().sum()
print("Missing values per column:")
print(null_counts)
print("\n")

df = df.drop(columns=['Cabin', 'Ticket'])

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

df = df.rename(columns={
    'Survived': 'Survived',
    'Pclass': 'Passenger_Class',
    'SibSp': 'Siblings_Spouses',
    'Parch': 'Parents_Children'
})

df = df[df['Age'] > 0]

df.to_csv('data/cleaned_titanic.csv', index=False)
print("Cleaning complete. File saved to data/cleaned_titanic.csv")
