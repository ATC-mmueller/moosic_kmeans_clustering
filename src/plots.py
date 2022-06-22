def subplot_minmax(df):
    from matplotlib import pyplot as plt
    df_clusters = []
    fig, axs = plt.subplots(9, 4, figsize=(14, 24), sharex='row')
    for i in range(4):
        df_clusters.append(df[df.cl_minmax == i])
        axs[0, i].set_title(f'Cluster {i}')
    for j in range(9):
        axs[j,0].set_ylabel(df.columns[j])
        for i in range(4):
            axs[j, i].hist(df_clusters[i][df.columns[j]], bins=50, color = colortab(j))
    plt.show()
    
def colortab(n):
    if n == 0:
        return 'tab:blue'
    if n == 1:
        return 'tab:orange'
    if n == 2:
        return 'tab:green'
    if n == 3:
        return 'tab:red'
    if n == 4:
        return 'tab:purple'
    if n == 5:
        return 'tab:brown'
    if n == 6:
        return 'tab:pink'
    if n == 7:
        return 'tab:gray'
    if n == 8:
        return 'tab:olive'
    if n == 9:
        return 'tab:cyan'