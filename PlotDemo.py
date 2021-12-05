###################################################################################################
## 1.Histogram
import seaborn as sns
import matplotlib.pyplot as plt

Y_Language = ['LPT_story','LPT_math','LPT_story_math','RPT_story','RPT_math','RPT_story_math','det_story','det_math','det_story_math']
Y_Social = ['LPT_TOM','LPT_RAD','LPT_TOM_RAD','RPT_TOM','RPT_RAD','RPT_TOM_RAD','det_TOM','det_RAD','det_TOM_RAD']   
Y_Gambling = ['LPT_con1','LPT_con2','LPT_con3','RPT_con1','RPT_con2','RPT_con3','det_con1','det_con2','det_con3']
Y_Emotion = ['LPT_FACE','LPT_SHAPE','LPT_F_S','RPT_FACE','RPT_SHAPE','RPT_F_S','det_FACE','det_SHAPE','det_F_S']

fig, axes = plt.subplots(3,3,figsize=(20, 10))
for k,y_str in enumerate(Y_Emotion):
    Y = eval(y_str)
    k1=k//3
    k2=k%3
    fig.suptitle('Emotion',fontsize=25)

    sns.set_style('darkgrid')
    sns.distplot(Y,ax=axes[k1][k2])
    axes[k1][k2].set_title(y_str)
fig.savefig('/mnt/data/Project/PT/RidgeRegression/Taskt_view/Emotion.png')

###################################################################################################
