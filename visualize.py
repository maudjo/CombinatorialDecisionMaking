
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np



def visualize(dfout, df):

    plt.rcParams['figure.figsize'] = [6, 4]

    px = dfout['x']
    py = dfout['y']
    pw = dfout['w']
    ph = dfout['h']
    pindx = dfout['indx']
    colors = [ 'tab:'+df['color'][ind] for ind in pindx ]

    fig = plt.figure()
    ax = fig.add_subplot(111) 

    plt.xlim([0, 30]) 
    plt.ylim([0, 20]) 

    nn = len(px)
    for i in range(nn):
        r = plt.Rectangle((px[i],py[i]),pw[i],ph[i],edgecolor='black',facecolor=colors[i])
        ax.add_patch(r)

    used_indx = np.sort(pindx.unique())
    ucolors = ['tab:'+ df['color'][i] for i in used_indx]
    uname =  [df['item'][i] for i in used_indx]
    handle = [ mpatches.Patch(color=ucolors[i],label=uname[i]) for i in range(len(used_indx))  ]
    dummy=plt.legend(handles=handle,loc='center left', bbox_to_anchor=(1, 0.5))