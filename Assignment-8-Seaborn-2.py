import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in planets dataset
planets = sns.load_dataset("planets")

# Preview the dataset
print(planets.head())

# 1. Distributional Plot (Histogram of Mass) - Already present
plt.figure(figsize=(8, 5))
sns.histplot(data=planets, x='mass', bins=30, kde=True)
plt.title('Distribution of Planet Mass')
plt.xlabel('Mass (Jupiter Masses)')
plt.xscale('log')
plt.tight_layout()
plt.show()

# 2. Distributional Plot (KDE of Year)
plt.figure(figsize=(8, 5))
sns.kdeplot(data=planets, x='year', fill=True)
plt.title('Distribution of Planet Discovery Year')
plt.xlabel('Year')
plt.ylabel('Density')
plt.tight_layout()
plt.show()

# 3. Relational Plot (Scatter plot of Year vs Orbital Period)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=planets, x='year', y='orbital_period')
plt.title('Planet Orbital Period Over Time')
plt.xlabel('Discovery Year')
plt.ylabel('Orbital Period (Days)')
plt.yscale('log') # Using log scale for better visualization of spread
plt.tight_layout()
plt.show()

# 4. Relational Plot (Scatter plot of Distance vs Mass)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=planets, x='distance', y='mass')
plt.title('Planet Mass vs Distance from Star')
plt.xlabel('Distance (Light Years)')
plt.ylabel('Mass (Jupiter Masses)')
plt.xscale('log')
plt.yscale('log') # Using log scale for better visualization of spread
plt.tight_layout()
plt.show()

# 5. Categorical Plot (Box plot of Orbital Period by Method)
plt.figure(figsize=(12, 6))
sns.boxplot(data=planets, x='method', y='orbital_period')
plt.title('Orbital Period by Discovery Method')
plt.xlabel('Discovery Method')
plt.ylabel('Orbital Period (Days)')
plt.yscale('log') # Using log scale for better visualization of spread
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 6. Categorical Plot (Bar plot of Number of Planets by Method)
plt.figure(figsize=(10, 6))
sns.countplot(data=planets, y='method', order=planets['method'].value_counts().index)
plt.title('Number of Planets Discovered by Method')
plt.xlabel('Number of Planets')
plt.ylabel('Discovery Method')
plt.tight_layout()
plt.show()

# 7. Heatmap of Numerical Features - Already present
planets_numeric = planets.select_dtypes(include=['number'])
correlation = planets_numeric.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="viridis", cbar_kws={'label': 'Correlation Coefficient'})
plt.title("Heatmap of Numerical Features in the Planets Dataset")
plt.tight_layout()
plt.show()
