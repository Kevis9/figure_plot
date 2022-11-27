import numpy as np
import pandas as pd

trues = np.load('trues_after_shuffle.npy', allow_pickle=True)
ref_true = list(trues[:3727])
query_true = list(trues[3727:])

ref_data = pd.DataFrame({
    'label':ref_true,
})

query_data = pd.DataFrame({
    'label':query_true,
})



print(ref_data['label'].value_counts())
ref_label = list(set(ref_data['label'].to_list()))
ref_label.sort()
print(ref_label)
print(query_data['label'].value_counts())
query_label = list(set(query_data['label'].to_list()))
query_label.sort()
print(query_label)


'''
    下面是js代码
'''
'''
option = {
  series: {
    type: 'sankey',
    layout: 'none',
    emphasis: {
      focus: 'adjacency'
    },
    data: [
      {
        name: 'Reference'
      },
      {
        name: 'Query'
      },
      {
        name: 'B cell'
      },
      {
        name: 'CD14+ monocyte'
      },
      {
        name: 'CD4+ T cell'
      },
      {
        name: 'Cytotoxic T cell'
      },
      {
        name: 'Dendritic cell'
      },
      {
        name: 'Megakaryocyte'
      },
      {
        name: 'Plasmacytoid dendritic cell'
      },
      
    ],
    links: [
      {
        source: 'Reference',
        target: 'Cytotoxic T cell',
        value: 1278
      },
      {
        source: 'Reference',
        target: 'CD14+ monocyte',
        value: 1255
      },
      {
        source: 'Reference',
        target: 'CD4+ T cell',
        value: 566
      },
      {
        source: 'Reference',
        target: 'B cell',
        value: 527
      },
      {
        source: 'Reference',
        target: 'Megakaryocyte',
        value: 38
      },
      {
        source: 'Reference',
        target: 'Dendritic cell',
        value: 37
      },
      {
        source: 'Reference',
        target: 'Plasmacytoid dendritic cell',
        value: 26
      },
      {
        source: 'Query',
        target: 'Cytotoxic T cell',
        value: 962
      },
      {
        source: 'Query',
        target: 'CD14+ monocyte',
        value: 960
      },
      {
        source: 'Query',
        target: 'CD4+ T cell',
        value: 354
      },
      {
        source: 'Query',
        target: 'B cell',
        value: 346
      },
      {
        source: 'Query',
        target: 'Megakaryocyte',
        value: 270
      },
      {
        source: 'Query',
        target: 'Dendritic cell',
        value: 38
      },
      
    ]
  }
};
'''
