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