"""
FILE: helper.py
DESCRIPTION: A module conntaining helpers
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-DEC-2020
"""
# Import libs
import requests

import pandas as pd
import pycountry_convert as pc


# Helper module
class DataFrameHelper:
    def __init__(self):
        self.lookup_table_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv'
        self.lookup_df = pd.read_csv(self.lookup_table_url)[['iso2', 'Country_Region']]
        self.lookup_data = {v['Country_Region']: v['iso2'] for v in self.lookup_df.to_dict('records')}
    
    def clean_df_current(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Run all pre-processing procedures for COVID19 current data """
        if not isinstance(df, pd.DataFrame):
            return pd.DataFrame({})
        
        df['country_code'] = df['location'].apply(lambda country_name: self.country_name_to_code(country_name))
        df['continent'] = df['country_code'].apply(lambda country_code: self.country_code_to_continent(country_code))

        return df
    
    def country_name_to_code(self, country_name: str) -> str:
        """ Convert country name to country code iso2 """
        code = self.lookup_data.get(country_name, '')
        return str(code)
    
    def country_code_to_continent(self, country_code: str) -> str:
        """ Convert country code iso2 to country code iso2 continent """
        try:
            continent = pc.country_alpha2_to_continent_code(country_code)
        except:
            continent = 'Other'

        return continent
