import numpy as np
def cut_percentile(df,feature,perc):
    Q3 = np.percentile(df[feature], perc)
    return df.loc[df.FreQ<=Q3]
    
