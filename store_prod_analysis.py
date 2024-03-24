import pandas as pd

def select_df_contain_content(df,column,content):
    return df.loc[df[column] == content,:]

storage = pd.read_csv('Meat_Stats_Cold_Storage.csv')
production = pd.read_csv('Meat_Stats_Meat_Production.csv')

datetime_dates = pd.to_datetime(storage['Date'], format="%b-%Y")
storage['Date'] = datetime_dates

datetime_dates = pd.to_datetime(production['Date'], format="%b-%Y")
production['Date'] = datetime_dates

Broilers_p = select_df_contain_content(production,'Animal','Broilers')
Broilers_s = select_df_contain_content(storage,'Animal','Broiler')
Broilers_p = select_df_contain_content(Broilers_p,'Commercial or Federally Inspected','Federally Inspected')

df = pd.merge(Broilers_p,Broilers_s,how='inner',on='Date')[['Date','Year_x','Month_x','Production','Weight','Unit_x']]
df = df.rename(columns={'Year_x':'Year','Month_x':'Month','Unit_x':'Unit','Weight':'Storage'})
df.to_csv('Broilers_store_prod.csv',index=False)

