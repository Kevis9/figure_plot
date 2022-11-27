import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import numpy as np

embeddings = np.load('seq_well_10x/embeddings_2d.npy', allow_pickle=True)
preds = np.load('seq_well_10x/preds.npy', allow_pickle=True)
trues = np.load('seq_well_10x/trues_after_shuffle.npy', allow_pickle=True)

ref_data = pd.DataFrame({
    'x': embeddings[:3727, 0],
    'y': embeddings[:3727, 1],
    'true': trues[:3727]
})
query_data = pd.DataFrame({
    'x': embeddings[3727:, 0],
    'y': embeddings[3727:, 1],
    'true': preds[3727:]
})
# 去掉ref_data里面的plas细胞类型 ， 用来展示
# ref_data = ref_data[ref_data['true']!='Plasmacytoid dendritic cell']

# 对细胞类型按照字典序排序
ref_data = ref_data.sort_values(by='true')
query_data = query_data.sort_values(by='true')

# sns.scatterplot(x='x', y='y', data=ref_data, hue='true', s=3, ax=axs, legend=True)

# query
ax = sns.scatterplot(x='x', y='y', data=query_data, hue='true', s=4)
ax.set_xlabel("")
ax.set_ylabel("")

# 去掉上边框和右边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.legend(loc=3, bbox_to_anchor=(1, 0))
plt.savefig("query_embedding", dpi=600, bbox_inches='tight')
plt.show()

