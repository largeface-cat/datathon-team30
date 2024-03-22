import pandas as pd
import re 
import numpy as np
import matplotlib.pyplot as plt
import json

# eco = pd.read_csv('acs_5yr_est_selected_economic_characteristics_2010-2022.csv')
# category = np.array(eco['Label (Grouping)'])
# # from category get those about Income
# pattern = r'INCOME'
# ind_list = []
# for i in range(len(category)):
#     if re.findall(pattern,category[i]):
#         if len(ind_list) == 0 or abs(ind_list[-1] - i) > 1:
#             ind_list.append(i-1)
#         ind_list.append(i)
# income_df = eco.iloc[ind_list,:]

# cate_dict = {}
# category = np.array(income_df['Category'])
# state  = np.array(income_df['State'])
# label = income_df['Label (Grouping)']
# label = label.apply(lambda x: x.lstrip('\xa0'))
# label = np.array(label)
# for i in range(len(category)):
#     if category[i] == 'Header':
#         cate = label[i]
#         s = state[i]
#         cate_dict[(cate,s)] = pd.DataFrame(income_df.iloc[[i],:])
#     else:
#         cate_dict[(cate,s)] = pd.concat([cate_dict[(cate,s)],income_df.iloc[[i],:]])                                    

# # get the nominal income

def select_df_contain_content(df,column,content):
    return df.loc[df[column] == content,:]

def get_question_and_sort(df,question,column = 'Question',):
    result = select_df_contain_content(df,'Question',question)
    result = result.sort_values('YearStart',ascending = True)
    return result


eco = pd.read_csv('./Clean ACS Data/nominalIncome.csv')
state_list = np.array(eco['State'].unique()) # get states list
# get selected data type
selected_list = [ 'Median household income (dollars)','Mean household income (dollars)','Median family income (dollars)','Mean family income (dollars)','Median nonfamily income (dollars)','Mean nonfamily income (dollars)','Per capita income (dollars)']
income_dic = {}
for label in selected_list: # iterate the selected_list 
    dic = {}
    for state in state_list: # iterate the state_list
        df = select_df_contain_content(eco, 'Label..Grouping.', label)
        df = select_df_contain_content(df,'State',state)
        df = df[['Estimate','Year']]
        dic[state] = df.to_dict('list')
    income_dic[label] = dic 



# Assuming 'data' is your dictionary
with open('clean_income.json', 'w') as json_file:
    json.dump(income_dic, json_file)



    




