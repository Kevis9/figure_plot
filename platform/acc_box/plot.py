import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('platform_acc.csv')
# print(data)
ax = sns.boxplot(x='Method', y='acc', data=data, order=['CHETAH', 'SingleR', 'scmap', 'scGCN', 'Seurat_cca', 'Seurat_pca', 'Ours'])
# sns.catplot(x="acc", y="view", data=data, kind='boxen')
plt.xlabel("")
plt.ylabel("")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticklabels([])
plt.savefig('box', dpi=600, transparent=True)
plt.show()
