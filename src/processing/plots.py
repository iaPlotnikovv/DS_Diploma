import matplotlib.pyplot as plt
import seaborn as sns



def plot(df, hist=False, box=False):
    plt.figure(figsize=(10, 10))
    columns = df.columns
    n = len(columns)
    cols = 3
    rows = (n + cols) // cols  # округление вверх
    for i, col in enumerate(columns, 1):
        plt.subplot(rows, cols, i)
        
        if hist:
            plt.hist(df[col], bins=65, color='green', edgecolor='black')
        if box:
            sns.boxplot(df[col],color='green', width=0.5)
            
        plt.title(col)
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()