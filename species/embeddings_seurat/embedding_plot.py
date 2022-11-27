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

    plt.savefig(path, dpi=600, bbox_inches='tight')
    # plt.show()

def read_data(path):

    ref_embeddings = pd.read_csv(os.path.join(path, "ref_embeddings_2d.csv"), index_col=0).to_numpy()
    ref_labels = pd.read_csv(os.path.join(path, "ref_label.csv")).to_numpy()

    query_embeddings = pd.read_csv(os.path.join(path, "query_embeddings_2d.csv"), index_col=0).to_numpy()
    query_labels = pd.read_csv(os.path.join(path, "query_pred.csv")).to_numpy()

    embeddings = np.concatenate([ref_embeddings, query_embeddings], axis=0)
    labels = np.concatenate([ref_labels, query_labels], axis=0).reshape(-1)


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


# path = 'result/gse/mouse_human'
# save_path = 'gsemouse_gsehuman_emb'

# path = 'result/gse/human_mouse'
# save_path = 'gsehuman_gsemouse_emb'
#
# path = 'result/gse_emtab/mouse_human'
# save_path = 'gsemouse_emtab_emb'
#
# path = 'result/gse_emtab/human_mouse'
# save_path = 'emtab_gsemouse_emb'


data_df = read_data(path)
plot_cluster(data_df, save_path)
