import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
# 在这里绘制一些论文的图片

### Platform A
df = pd.read_csv('acc_data.csv')
df['ref-query'] = df.apply(lambda x: x['Ref'] + ' - ' + x['Query'], axis=1)

# ## 单独绘制图例
# fig, axs = plt.subplots()
# fig.set_figwidth(7)
# fig.set_figheight(7)

# axs.axis('off')
# plt.savefig('colorbar.svg', dpi=600, transparent=True)
# plt.show()
# exit()

#seurat
# name = "Seurat"
# major_ticks = [0.7, 0.8, 0.9, 1]
# minor_ticks = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

## Single R
# name = "SingleR"
# major_ticks = [0.2, 0.4, 0.6, 0.8, 1]
# minor_ticks = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

## scmap
# name = "scmap"
# major_ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1]
# minor_ticks = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

## CHETAH
name = "CHETAH"
major_ticks = [0.2, 0.4, 0.6, 0.8, 1]
minor_ticks = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]



fig, axs = plt.subplots()
fig.set_figwidth(5)
fig.set_figheight(5)
# ours - Seurat
sns.scatterplot(x=name, y='Ours', data=df, hue=df['ref-query'].tolist(), s=40, legend=False, ax=axs, palette=sns.color_palette("hls", 13))
sns.lineplot(x=[major_ticks[0]-0.05,1.05], y=[major_ticks[0]-0.05,1.05], ls='--', linewidth=1, color='black', ax=axs)


axs.set_xlim(major_ticks[0]-0.05, 1.05)
axs.set_ylim(major_ticks[0]-0.05, 1.05)
axs.set_xticks(major_ticks)
axs.set_yticks(major_ticks)
axs.set_xticks(minor_ticks, minor=True)
axs.set_yticks(minor_ticks, minor=True)


axs.set_xlabel("")
axs.set_ylabel("")
axs.grid(which='minor', alpha=0.3)
axs.grid(which="major",alpha=0.3)


plt.savefig(name, dpi=600, bbox_inches='tight')
plt.show()