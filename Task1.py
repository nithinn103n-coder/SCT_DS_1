# ---------------------------------------------
# SKILLCRAFT TASK 1 – COMPLETE COMBINED CODE
# ---------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------
# 1. CREATE SAMPLE DATASET & SAVE TO CSV
# ---------------------------------------------
np.random.seed(42)

data = {
    'Age': np.random.randint(0, 85, 500),
    'Gender': np.random.choice(
        ['Male', 'Female', 'Non-Binary'], 
        500, 
        p=[0.48, 0.48, 0.04]
    ),
    'Country': np.random.choice(
        ['USA', 'India', 'UK', 'Canada', 'Germany'], 
        500
    ),
    'Employment_Status': np.random.choice(
        ['Employed', 'Unemployed', 'Student', 'Retired'], 
        500
    )
}

df_sample = pd.DataFrame(data)
df_sample.to_csv('skillcraft_task1_data.csv', index=False)
print("File 'skillcraft_task1_data.csv' has been created!")

# ---------------------------------------------
# 2. LOAD DATASET
# ---------------------------------------------
df = pd.read_csv('skillcraft_task1_data.csv')

# ---------------------------------------------
# 3. AGE DISTRIBUTION & GENDER DISTRIBUTION
# ---------------------------------------------
plt.figure(figsize=(14, 6))

# Age Distribution
plt.subplot(1, 2, 1)
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

# Gender Distribution
plt.subplot(1, 2, 2)
sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# ---------------------------------------------
# 4. POPULATION DISTRIBUTION CURVE
# ---------------------------------------------
# Age range
age = np.linspace(0, 100, 500)

# Simulated population curve (young population peak)
population = 26 * np.exp(-0.5 * ((age - 28) / 22) ** 2)

# Create plot
plt.figure(figsize=(10, 6))

# Age groups
young = age <= 20
working = (age > 20) & (age <= 64)
old = age > 64

# Plot filled areas for each age group
plt.fill_between(age[young], population[young], color="gold", label="0–20 Years")
plt.fill_between(age[working], population[working], color="dodgerblue", label="21–64 Years")
plt.fill_between(age[old], population[old], color="deeppink", label="65+ Years")

# Labels and title
plt.title("India’s Population Distribution by Age (Simulated)", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Population (Millions)")

# Text annotations (similar to image)
plt.text(5, 5, "0–20 Years\n36.1%", fontsize=9)
plt.text(30, 6, "21–64 Years\n57.0%\nMedian Age: 28", fontsize=9)
plt.text(70, 3, "65+ Years\n6.9%", fontsize=9)

# Limits and layout
plt.xlim(0, 100)
plt.ylim(0)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()

