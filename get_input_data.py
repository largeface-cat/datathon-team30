import json
import pandas as pd
# Assuming you have a file named 'data.json'
with open('clean_income.json', 'r') as f:
    income_data = json.load(f)

with open('clean_obesity.json','r') as f:
    obesity_data = json.load(f)

# Create a new dictionary to store the combined data
household_income_median = income_data.get('Median household income (dollars)')
household_income_mean = income_data.get('Mean household income (dollars)')
family_income_median = income_data.get('Median family income (dollars)')
family_income_mean = income_data.get('Mean family income (dollars)')

obesity_rate_adults = obesity_data.get('obRateAdults')
ow_rate_adults = obesity_data.get('owRateAdults')
obesity_rate_children = obesity_data.get('obRateKids')
ow_rate_children = obesity_data.get('owRateKids')

income_ob_data_adult = {}
# add adult obe data
for state,df in obesity_rate_adults.items():
    df = pd.DataFrame(df)
    df.rename(columns={'Data_Value': 'adult_obesity_Value','Income':'adult_Income','StratificationCategoryId1':'adult_StratificationCategoryId1','StratificationID1':'adult_StratificationID1'}, inplace=True)
    if len(df.Year.unique()) > 10:
        income_ob_data_adult[state] = df[['Year','adult_obesity_Value','adult_Income','adult_StratificationCategoryId1','adult_StratificationID1']]



# add household_incom_mean_data_to_df
for state in household_income_mean:
    signal = True if income_ob_data_adult.get(state) is not None else False 
    if signal:
        mapping_dict = dict(zip(household_income_mean[state].get('Year'),household_income_mean[state].get("Estimate")))
        income_ob_data_adult[state]['Mean household income (dollars)'] = income_ob_data_adult[state]['Year'].map(mapping_dict)

# add household_income_median_Data_to_df
for state in household_income_mean:
    signal = True if income_ob_data_adult.get(state) is not None else False 
    if signal:
        mapping_dict = dict(zip(household_income_median[state].get('Year'),household_income_median[state].get("Estimate")))
        income_ob_data_adult[state]['Median household income (dollars)'] = income_ob_data_adult[state]['Year'].map(mapping_dict)


# convert dict into df
income_ob_df = pd.DataFrame(columns = ['Year','adult_obesity_Value','adult_Income','adult_StratificationCategoryId1','adult_StratificationID1','Mean household income (dollars)','Median household income (dollars)','LocationDesc'])
for key,df in income_ob_data_adult.items():
    df['LocationDesc'] = [key] * df.shape[0]
    income_ob_df = pd.concat([income_ob_df,df])

income_ob_df.to_csv('adult_income_obesity.csv',index = False)






# add children obe data
income_ob_data_child = {}
for state,df in obesity_rate_children.items():
    df = pd.DataFrame(df)
    df.rename(columns={'Data_Value': 'child_obesity_Value','StratificationCategoryId1':'child_StratificationCategoryId1','StratificationID1':'child_StratificationID1'}, inplace=True)
    if len(df.Year.unique()) > 8:
        income_ob_data_child[state] = df[['Year','child_obesity_Value','child_StratificationCategoryId1','child_StratificationID1','Grade','Gender']]


# add family_incom_mean_data_to_df
for state in household_income_mean:
    signal = True if income_ob_data_child.get(state) is not None else False 
    if signal:
        mapping_dict = dict(zip(family_income_mean[state].get('Year'),family_income_mean[state].get("Estimate")))
        income_ob_data_child[state]['Mean family income (dollars)'] = income_ob_data_child[state]['Year'].map(mapping_dict)

# add family_income_median_Data_to_df
for state in household_income_mean:
    signal = True if income_ob_data_child.get(state) is not None else False 
    if signal:
        mapping_dict = dict(zip(family_income_median[state].get('Year'),family_income_median[state].get("Estimate")))
        income_ob_data_child[state]['Median family income (dollars)'] = income_ob_data_child[state]['Year'].map(mapping_dict)

income_ob_df = pd.DataFrame(columns = ['Year','child_obesity_Value','child_StratificationCategoryId1','child_StratificationID1','Grade','Gender','Mean household income (dollars)','Median household income (dollars)','LocationDesc'])
for key,df in income_ob_data_child.items():
    df['LocationDesc'] = [key] * df.shape[0]
    income_ob_df = pd.concat([income_ob_df,df])

income_ob_df.to_csv('child_income_obesity.csv',index = False)