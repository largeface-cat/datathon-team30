import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.formula.api as smf


def select_df_contain_content(df,column,content):
    return df.loc[df[column] == content,:]

# add new feature
s_p_data = pd.read_csv('Broilers_store_prod.csv')
s_p_data.dropna(inplace = True)
s_p_data = s_p_data.loc[((2021 >= s_p_data['Year']) & (s_p_data['Year'] >= 2011)),:]


sold_data = s_p_data['Storage'].shift(1) - s_p_data['Storage'] + s_p_data['Production']
sold_data /= 133
sold_data = sold_data.to_list()[::-1]
# s_p_data['Sold'] = sold_data
# s_p_data.dropna(inplace=True)
# print(s_p_data)
# # s_p_data = s_p_data.groupby(['Year']).sum()[['Sold']]
# s_p_data.reset_index(inplace = True)
data = pd.read_csv('./adult_income_obesity.csv')
income_ob_data = select_df_contain_content(data,'adult_StratificationCategoryId1','INC') 
income_ob_data = select_df_contain_content(income_ob_data,'LocationDesc','National') 
# print
income_list = income_ob_data['adult_Income'].unique()

for ind in range(len(income_list)):
    ob = select_df_contain_content(income_ob_data,'adult_Income',income_list[ind])
    ob = ob['adult_obesity_Value'].to_list()
    tmp = []
    for i in range(len(ob)):
        if i < len(ob)-1:
            d = (ob[i+1] - ob[i])/12
            tmp+= [ob[i]+n*d for n in range(12)]
    df = pd.DataFrame( {'Date':s_p_data['Date'],'obesity':tmp,'sold':sold_data})
    model = smf.ols(formula='obesity ~ sold', data=df).fit()
    print(income_list[ind])
    print(model.summary())
    plt.plot(tmp)
    
    plt.plot(sold_data)
    plt.title(income_list[ind])

    plt.show()


"""
sold_data = s_p_data['Sold']/1000


slaughter_data = pd.read_csv('./Broilers_slaughter.csv')
slaughter_data = slaughter_data.loc[((2023 > slaughter_data['Year']) & (slaughter_data['Year'] >= 2011)),:]
# slaughter_data = slaughter_data.groupby(['Year']).sum()[['Count']]
slaughter_data.reset_index(inplace = True)





for ind in range(len(income_list)):
    df = select_df_contain_content(income_ob_data,'adult_Income',income_list[ind])
    df = df[['Year','adult_obesity_Value']]
    df['adult_obesity_Value_diff_b1'] = df['adult_obesity_Value'].diff()
    df['adult_obesity_Value_pct_b1'] = df['adult_obesity_Value'].pct_change()
    df['sold_weight_Value'] = sold_data.values
    df['sold_weight_Value_diff_b1'] = df['sold_weight_Value'].diff()
    df['sold_weight_Value_pct'] = df['sold_weight_Value'].pct_change()
    df['sold_weight_Value_pct_b1'] = df['sold_weight_Value'].pct_change().shift(1)
    df['sold_weight_Value_pct_b2'] = df['sold_weight_Value'].pct_change().shift(1).shift(1)
    # df['slaugter_num'] = slaughter_data['Count'].values/(10**8)

    # df['slaugter_num_b0_pct'] = df['slaugter_num'].pct_change()
    # df['slaugter_num_b1'] = df['slaugter_num'].shift(1)
    # df['slaugter_num_b2'] = df['slaugter_num'].shift(2)
    # df['slaugter_num_b1_pct'] = df['slaugter_num_b1'].pct_change()
    # df['slaugter_num_b2_pct'] = df['slaugter_num_b2'].pct_change()




    df = df.iloc[2:,:]

# plot the obe and sold 
    
    # slope, intercept, r_value, p_value, std_err = stats.linregress(df[['Year','adult_obesity_Value']].values.reshape(-1,2), slaughter_data['Count'].values.reshape(-1,1)/(10**8))
    # print("slope: ", slope)
    # print("intercept: ", intercept)
    # print('p_value: ', p_value)
    fig,ax = plt.subplots(1,1,figsize = (40,20))
    # plt.plot(df['Year'],df['adult_obesity_Value'])
    ax.plot(df['Year'],df['adult_obesity_Value_pct_b1'])
    ax.plot(df['Year'],df['sold_weight_Value_pct_b2'])
    ax.set_title(income_list[ind])
    ax.set_ylim(-0.05,0.05)
    plt.legend(['obesity','sold_pounds'])
    plt.show()


    # regression
    model = smf.ols(formula='adult_obesity_Value_pct_b1 ~ sold_weight_Value_pct_b1', data=df).fit()
    print(income_list[ind])
    print(model.summary())
"""

    




