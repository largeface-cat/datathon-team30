import os
import pandas as pd
import json
# Assuming 'path_to_directory' is the directory you want to iterate through
# path_to_directory = './Clean Obesity Data/'
# for filename in os.listdir(path_to_directory):
#     filepath = os.path.join(path_to_directory, filename)
#     # Now you can work with 'filepath'

def select_df_contain_content(df,column,content):
    return df.loc[df[column] == content,:]

def get_question_and_sort(df,question,column = 'Question',):
    result = select_df_contain_content(df,'Question',question)
    result = result.sort_values('YearStart',ascending = True)
    return result


path_to_directory = './Clean Obesity Data/'
selected_file = ['obRateAdults.csv','owRateKids.csv','owRateAdults.csv','obRateKids.csv']
whole_location = pd.read_csv('Nutrition_Physical_Activity_and_Obesity_Data.csv')['LocationDesc'].unique() 
abbr_location = pd.read_csv('Nutrition_Physical_Activity_and_Obesity_Data.csv')['LocationAbbr'].unique()

mapping_dict = dict(zip(abbr_location,whole_location)) # convert abbr into whole name


obesity_dic = {}
for filename in selected_file:
    filepath = os.path.join(path_to_directory, filename) # get the file path
    df = pd.read_csv(filepath) # read the file
    df = df.sort_values('Year',ascending = True)
    df['LocationDesc'] = df['LocationAbbr'].map(mapping_dict) # convert abbr into whole name
    df.drop('LocationAbbr',axis = 1,inplace = True) # drop the abbr column
    df.dropna(subset=['Data_Value'],axis = 0,inplace = True) # drop the row with whitch Data has nan value
    states_range = df['LocationDesc'].unique()
    dic = {}
    for state in states_range:
        df_state = select_df_contain_content(df,'LocationDesc',state) # get the state data
        dic[state] = df_state.to_dict('list')
    obesity_dic[filename[:-4]] = dic


with open('clean_obesity.json', 'w') as json_file:
    json.dump(obesity_dic, json_file)





