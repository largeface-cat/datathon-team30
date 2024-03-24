import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

def select_df_contain_content(df,column,content):
    return df.loc[df[column] == content,:]


import numpy as np

def remove_outliers(X):
    # 计算均值和标准差
    mu = np.mean(X)
    sigma = np.std(X)
    
    # 确定上下界
    lower_bound = mu - 2 * sigma
    upper_bound = mu + 2 * sigma
    
    # 筛选出在上下界之间的点
    X_filtered = [True if x >= lower_bound and x <= upper_bound else False for x in X ]
    
    return X_filtered



# 1. Load the data
beef_list = ['Cattle','Steers','Heifers'] # beef list
chicken_list = ['Broilers', 'Other chickens']

# 2. production data 

meat_production = pd.read_csv('./Clean Meat Consumption Data/meatProduction.csv')
meat_slaughter = pd.read_csv('./Clean Meat Consumption Data/slaughterCount.csv')


datetime_dates = pd.to_datetime(meat_slaughter['Date'], format="%b-%Y")
meat_slaughter['Date'] = datetime_dates




# get data from beef_list

dic = {}
for beef in beef_list:
    df = select_df_contain_content(meat_slaughter,'Animal',beef)
    selected = remove_outliers(df['Count'])
    df = df.loc[selected,:]
    df['Moving_average'] = df['Count'].rolling(window=3).mean()
    df.dropna(subset= ['Moving_average'],inplace=True)
    dic[beef] = df

for chicken in chicken_list:
    df = select_df_contain_content(meat_slaughter,'Animal',chicken)
    selected = remove_outliers(df['Count'])
    df = df.loc[selected,:]
    df['Moving_average'] = df['Count'].rolling(window=3).mean()
    df.dropna(subset= ['Moving_average'],inplace=True)
    dic[chicken] = df

# 3. plot the data
def get_amount_gap(beef,chicken):
    pass

def plot_amount(df):
    fig,ax = plt.subplots(1,1,figsize=(10,5))
    ax.plot(df['Date'],df['Moving_average'])
    ax.set_title('Slaughter Count of {}'.format(df['Animal'].iloc[0]))
    plt.show()


for key in dic.keys():
    plot_amount(dic[key])

chicken = select_df_contain_content(meat_slaughter,'Type_Of_Meat','Poultry')
beef = select_df_contain_content(meat_slaughter,'Type_Of_Meat','Red Meat')

sum_chicken = chicken.groupby(['Date'])['Count'].sum()
sum_beef = beef.groupby(['Date'])['Count'].sum()



# 4. plot the data
fig,ax = plt.subplots(1,2,figsize = (12,5))
ax[0].plot(sum_chicken.index, sum_chicken.values)
ax[0].set_title('Chicken Slaughter Count')

ax[1].plot(sum_beef.index, sum_beef.values)
ax[1].set_title('Beef Slaughter Count')
plt.show()







