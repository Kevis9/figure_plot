import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import numpy as np
import os
colors = sns.color_palette("tab10")
colors += ['#342009']
cell_label = ['activated_stellate', 'alpha', 'beta', 'delta', 'ductal', 'endothelial', 'gamma', 'macrophage', 'quiescent_stellate', 'schwann', 't cell']

def plot_cluster(data_df, path):
    labels = list(set(data_df['label'].to_list()))
    labels.sort()
    use_color = []
    for i in range(len(labels)):
        use_color.append(colors[cell_label.index(labels[i])])

    ax = sns.scatterplot(x='x', y='y', data=data_df, hue='label', s=3, palette=use_color, legend=False)
    # plt.legend(loc=3, bbox_to_anchor=(1, 0))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.ylabel("")
    plt.xlabel("")

    plt.savefig(path, dpi=600, bbox_inches='tight', transparent=True)
    plt.show()

def read_data(path, raw=False):
    if raw:
        embeddings = np.load(os.path.join(path, "raw_data_2d.npy"), allow_pickle=True)
        labels = np.load(os.path.join(path, "raw_trues.npy"),allow_pickle=True)
    else:
        embeddings = np.load(os.path.join(path, "embeddings_2d.npy"), allow_pickle=True)
        labels = np.load(os.path.join(path, "all_pred.npy"), allow_pickle=True)


    data_df = pd.DataFrame({
        'x': embeddings[:, 0],
        'y': embeddings[:, 1],
        'label': labels
    })
    # label转小写
    data_df['label'] = data_df['label'].apply(lambda x: x.lower())
    # 对label按照字典序升序
    data_df = data_df.sort_values(by='label')
    return data_df

# path = 'result_new/gse/mouse_human'
# save_path = 'gsemouse_gsehuman_raw'

# path = 'result_new/gse/human_mouse'
# save_path = 'gsehuman_gsemouse_raw'
#
# path = 'result/gse_emtab/mouse_human'
# save_path = 'gsemouse_emtab_raw'
#

# path = 'result/gse_emtab/human_mouse'
# save_path = 'emtab_gsemouse_raw'

# path = 'result_new/gse/mouse_human'
# save_path = 'gsemouse_gsehuman_emb_new'

# path = 'result_new/gse/human_mouse'
# save_path = 'gsehuman_gsemouse_emb_new'
#
# path = 'result_new/gse_emtab/mouse_human'
# save_path = 'gsemouse_emtab_emb_new'
#
path = 'result_new/gse_emtab/human_mouse'
save_path = 'emtab_gsemouse_emb_new'


data_df = read_data(path, False)
plot_cluster(data_df, save_path)

# 单独绘制图例
# label = list(set(data_df['label'].tolist()))
# label.sort()
# data_df = pd.DataFrame({
#     'label':label
# })
# print(label)
# fig, axs = plt.subplots()
# fig.set_figwidth(7)
# fig.set_figheight(7)
# # ours - Seurat
# sns.scatterplot(x=[1 for i in range(11)], y=[i for i in range(60, 5, -5)], legend=None, data=data_df, hue=data_df['label'], s=200, ax=axs, palette=colors)
#
# axs.axis('off')
# plt.savefig('colorbar_11.svg', dpi=600, transparent=True)
# plt.show()
# exit()
