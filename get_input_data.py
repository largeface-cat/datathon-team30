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


obesity_rate_adults = obesity_data.get('obRateAdults')
ow_rate_adults = obesity_data.get('owRateAdults')
obesity_rate_children = obesity_data.get('obRateChildren')
ow_rate_children = obesity_data.get('owRateChildren')

income_ob_data = {}
for state,df in obesity_rate_adults.items():
    df = pd.DataFrame(df)
    if len(df.Year.unique()) > 10:
        income_ob_data[state] = df[['Year','Data_Value','Income','StratificationCategoryId1','StratificationID1']]

# add household_incom_mean_data_to_df
for state in household_income_mean:
    signal = True if income_ob_data.get(state) is not None else False 
    if signal:
        mapping_dict = dict(zip(household_income_mean[state].get('Year'),household_income_mean[state].get("Estimate")))
        income_ob_data[state]['Mean household income (dollars)'] = income_ob_data[state]['Year'].map(mapping_dict)

# add household_income_median_Data_to_df
for state in household_income_mean:
    signal = True if income_ob_data.get(state) is not None else False 
    if signal:
        mapping_dict = dict(zip(household_income_median[state].get('Year'),household_income_median[state].get("Estimate")))
        income_ob_data[state]['Median household income (dollars)'] = income_ob_data[state]['Year'].map(mapping_dict)


# convert dict into df,o







