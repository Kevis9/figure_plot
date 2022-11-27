import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import seaborn as sns
import pandas as pd

method = ['ours', 'Seurat PCA', 'Seurat CCA', 'scmap', 'SingleR', 'CHETAH', 'scGCN']
def plot_bar(acc, save_path):
    # 绘制Acc比较的Bar条
    df = pd.DataFrame(data={
        'Accuracy':acc,
        'Method':method
    })
    ax = sns.catplot(data=df.sort_values(by='Accuracy', ascending=True), x='Accuracy', y='Method', kind='bar', palette='Blues')
    plt.ylabel("")
    plt.xlabel("")
    # plt.xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    plt.xticks([0, 0.2,  0.4,  0.6, 0.8, 1])
    # plt.xlim(0.6, 1)
    # plt.xticks([0.6, 0.8, 1])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    # plt.
    # plt.ysticks([])
    print(df.sort_values(by='Accuracy', ascending=True)["Method"])
    print("Save fig: {:}".format(save_path))
    plt.savefig(save_path, dpi=600, transparent=True)

# gse mouse - human
acc = [0.959, 0.579, 0.892, 0.826, 0.411, 0.21, 0.932]
plot_bar(acc, "gse_mouse_human.png")

# gse human - mouse
acc = [0.94,0.925, 0.935, 0.826, 0.866, 0.282, 0.926]
plot_bar(acc, "gse_human_mouse.png")

# gsemouse - E-mtab-5061
acc = [0.967, 0.722,  0.749, 0.86, 0.867, 0.673, 0.966]
plot_bar(acc, "gse_mouse_emtab.png")

# E-mtab-5061 - gsemouse
acc = [0.945, 0.751, 0.692, 0.751, 0.865, 0.183, 0.944]
plot_bar(acc, "emtab_gse_mouse.png")



