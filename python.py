import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Connect to SQL and read data
conn = sqlite3.connect("students.db")
df = pd.read_sql_query("SELECT * FROM students", conn)

# Exploratory analysis
sns.boxplot(x="gender", y="math_score", data=df)
plt.show()

# Create target variable (Pass=1 if average>=50, else Fail=0)
df['avg_score'] = df[['math_score','reading_score','writing_score']].mean(axis=1)
df['pass'] = (df['avg_score'] >= 50).astype(int)

# Features & target
X = df.drop(['pass'], axis=1).select_dtypes(include=[int, float])
y = df['pass']

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
preds = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))
