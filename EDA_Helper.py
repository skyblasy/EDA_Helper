class EDA_Check:
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    def __init__(self, data):
        self.df = data
        
    def naratio(self):
        result = df.isna().sum()/len(df)
        return result
    
    def nachart(self):
        result = sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='crest')
        return result
    
    def valueratio(self,value):
        result = df.eq(value).sum()/len(df)
        return result
        
    def valuechart(self,value):
        sns.heatmap(df.eq(value),yticklabels=False,cbar=False,cmap="mako")
    
    def corrmap(self):
        corr_matrix = df.corr()
        mask = np.zeros_like(corr_matrix, dtype=np.bool)
        mask[np.triu_indices_from(mask)]= True
        
        f, ax = plt.subplots(figsize=(20, 25)) 
        heatmap = sns.heatmap(corr_matrix, 
                              mask = mask,
                              square = True,
                              linewidths = .5,
                              cmap = 'coolwarm',
                              cbar_kws = {'shrink': .4, 
                                        'ticks' : [-1, -.5, 0, 0.5, 1]},
                              vmin = -1, 
                              vmax = 1,
                              annot = True,
                              annot_kws = {'size': 12})
        #add the column names as labels
        ax.set_yticklabels(corr_matrix.columns, rotation = 0)
        ax.set_xticklabels(corr_matrix.columns)
        sns.set_style({'xtick.bottom': True}, {'ytick.left': True})
