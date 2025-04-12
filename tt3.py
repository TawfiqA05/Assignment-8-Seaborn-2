import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in planets dataset
planets = sns.load_dataset("planets")

# Preview the dataset
print(planets.head())


plt.figure(figsize=(8, 5))
sns.histplot(data=planets, x='mass', bins=30, kde=True)
plt.title('Distribution of Planet Mass')
plt.xlabel('Mass (Jupiter Masses)')
plt.xscale('log')
plt.tight_layout()
plt.show()

# Load the built-in planets dataset
planets = sns.load_dataset("planets")

# Compute correlation matrix of numerical features
correlation = planets.corr(numeric_only=True)

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="viridis", cbar_kws={'label': 'Correlation Coefficient'})
plt.title("Heatmap of Numerical Features in the Planets Dataset")
plt.tight_layout()
plt.show()


