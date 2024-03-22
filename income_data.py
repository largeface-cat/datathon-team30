import pandas as pd
import re 
import numpy as np
import matplotlib.pyplot as plt

eco = pd.read_csv('acs_5yr_est_selected_economic_characteristics_2010-2022.csv')
category = np.array(eco['Category'])
# from category get those about Income
pattern = r'INCOME'
ind_list = []
for i in range(len(category)):
    
    if re.findall(pattern,category[i]):
        if len(ind_list) == 0 or abs(ind_list[-1] - i) > 1:
            ind_list.append(i-1)
        ind_list.append(i)
income_df = eco.iloc[ind_list,:]

cate_dict = {}
category = np.array(income_df['Category'])
state  = np.array(income_df['State'])
label = income_df['Label (Grouping)']
label = label.apply(lambda x: x.lstrip('\xa0'))
label = np.array(label)
for i in range(len(category)):
    if category[i] == 'Header':
        cate = label[i]
        s = state[i]
        cate_dict[(cate,s)] = pd.DataFrame(income_df.iloc[[i],:])
    else:
        cate_dict[(cate,s)] = pd.concat([cate_dict[(cate,s)],income_df.iloc[[i],:]])