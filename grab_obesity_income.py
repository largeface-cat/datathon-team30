import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.formula.api as smf


def select_df_contain_content(df,column,content):
    return df.loc[df[column] == content,:]

slaughter_data = pd.read_csv('./Broilers_slaughter.csv')
slaughter_data = slaughter_data.loc[((2023 > slaughter_data['Year']) & (slaughter_data['Year'] >= 2011)),:]
slaughter_data = slaughter_data.groupby(['Year']).sum()[['Count']]
slaughter_data.reset_index(inplace = True)


data = pd.read_csv('./adult_income_obesity.csv')
income_ob_data = select_df_contain_content(data,'adult_StratificationCategoryId1','INC') 
income_ob_data = select_df_contain_content(income_ob_data,'LocationDesc','National') 


income_list = income_ob_data['adult_Income'].unique()
for ind in range(len(income_list)):
    df = select_df_contain_content(income_ob_data,'adult_Income',income_list[ind])
    df = df[['Year','adult_obesity_Value']]
    df['slaugter_num'] = slaughter_data['Count'].values/(10**8)
    df['adult_obesity_Value_pct'] = df['adult_obesity_Value'].pct_change()
    df['slaugter_num_b0_pct'] = df['slaugter_num'].pct_change()
    df['slaugter_num_b1'] = df['slaugter_num'].shift(1)
    df['slaugter_num_b2'] = df['slaugter_num'].shift(2)
    df['slaugter_num_b1_pct'] = df['slaugter_num_b1'].pct_change()
    df['slaugter_num_b2_pct'] = df['slaugter_num_b2'].pct_change()




    df = df.iloc[3:,:]


    # regression
    model = smf.ols(formula='adult_obesity_Value_pct ~ slaugter_num_b0_pct + slaugter_num_b1_pct + slaugter_num_b2_pct', data=df).fit()
    print(income_list[ind])
    print(model.summary())
    # slope, intercept, r_value, p_value, std_err = stats.linregress(df[['Year','adult_obesity_Value']].values.reshape(-1,2), slaughter_data['Count'].values.reshape(-1,1)/(10**8))
    # print("slope: ", slope)
    # print("intercept: ", intercept)
    # print('p_value: ', p_value)
    # fig,ax = plt.subplots(1,1,figsize = (40,20))
    # # plt.plot(df['Year'],df['adult_obesity_Value'])
    # ax.plot(df['Year'],df['adult_obesity_Value'])
    # ax.plot(slaughter_data['Year'],slaughter_data['Count']/(3*10**8))
    # ax.set_title(income_list[ind])
    # ax.set_ylim(20,40)
    # plt.legend(['obesity','slaughter_num'])
    # plt.show()




    




