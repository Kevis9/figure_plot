import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('singleview.csv')
# print(data)
ax = sns.boxplot(x='view', y='acc', data=data)
# sns.catplot(x="acc", y="view", data=data, kind='boxen')
plt.xlabel("")
plt.ylabel("")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticklabels([])
plt.savefig('box', dpi=600, transparent=True)
plt.show()
