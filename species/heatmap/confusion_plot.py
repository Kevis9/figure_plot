import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import multilabel_confusion_matrix

'''
    绘制混淆矩阵
'''
## embedding_ours, 取query部分
# pred = np.load('gse_mouse_human/ours/preds.npy', allow_pickle=True)[1868:]
# true = np.load('gse_mouse_human/ours/raw_trues.npy', allow_pickle=True)[1868:]
# save_name = "ours"
# print(pred.shape)
# print(true.shape)

### scGCN
# pred = np.load('gse_mouse_human/scGCN/all_pred.npy', allow_pickle=True)
# mask = np.load('gse_mouse_human/scGCN/query_mask.npy', allow_pickle=True)
# true = np.load('gse_mouse_human/scGCN/all_trues.npy', allow_pickle=True)
#
# pred = pred[mask]
# true = true[mask]
# save_name = "scGCN"


### Seurat
# pred = pd.read_csv('gse_mouse_human/Seurat_pca/query_pred.csv')['x'].to_numpy()
# true = np.load('gse_mouse_human/Seurat_pca/raw_trues.npy', allow_pickle=True)[1868:]
# save_name = "Seurat"
# print(pred.shape)
# print(true.shape)

# ### scmap
pred = pd.read_csv('gse_mouse_human/scmap/preds.csv', index_col=0)
pred[pred['yan'] == 'unassigned'] = 'Unassigned'
pred = pred['yan'].to_numpy()
true = np.load('gse_mouse_human/scmap/raw_trues.npy', allow_pickle=True)[1868:]
save_name = "scmap"

### Chetah
# pred = pd.read_csv('others/chetah.csv')
# pred['V1'] = pred['V1'].apply(lambda x: "Unassigned" if x.startswith("Node") else x)
# pred = pred['V1'].to_numpy()
# save_name = "Chetah"

'''
==================================================
'''

# true = np.load('ours_result/raw_trues.npy', allow_pickle=True)[3727:]
name = list(set(true))
name = [x.lower() for x in name]
name.sort()
if not "unassigned" in name:
    name.append("unassigned")


name_idx = {}
for i in range(len(name)):
    name_idx[name[i]] = i

confusion_mat = []


# 行是true，只考虑true的部分
for i in range(len(set(true))):
    confusion_mat.append([0 for j in range(len(name))])

pred = list(pred)
true = list(true)
true = [x.lower() for x in true]
pred = [x.lower() for x in pred]

for i in range(len(true)):
    row = name_idx[true[i]]
    col = name_idx[pred[i]]
    confusion_mat[row][col] += 1

## 构造DataFrame
confusion_mat = np.array(confusion_mat)
# 归一化
confusion_mat = confusion_mat / np.sum(confusion_mat, axis=1).reshape(-1, 1)
data_df = pd.DataFrame(
    confusion_mat
)
data_df.columns = name
true_name = list(set(true))
true_name.sort()
data_df.index = true_name

# 将数据倒置过来
data_df = data_df.reindex(index=data_df.index[::-1])

print(data_df.index)
print(data_df.columns)

sns.heatmap(data=data_df, cmap="Blues", cbar=False, xticklabels=False, yticklabels=False)
plt.savefig(save_name, dpi=600, bbox_inches="tight", transparent=True)
plt.show()
