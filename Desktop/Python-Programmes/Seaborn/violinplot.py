import matplotlib.pyplot as plt
import seaborn as sns

# Load the built-in tips data
tips = sns.load_dataset("tips")
sns.violinplot(x = "total_bill", data=tips)
plt.show()