"""
FILE: helper.py
DESCRIPTION: A module conntaining helpers
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-DEC-2020
"""
# Import libs
import dash_html_components as html
import pandas as pd
import pycountry_convert as pc

import io
import requests


# Helper module
class DataFrameHelper:
    def __init__(self):
        self.lookup_table_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv'
        self.lookup_table_content = requests.get(self.lookup_table_url).content # escape CERTIFICATE_VERIFY_FAILED
        self.lookup_df = pd.read_csv(io.StringIO(self.lookup_table_content.decode('utf-8')))[['iso2', 'iso3', 'Country_Region']]
        self.lookup_data_iso2 = {v['Country_Region']: v['iso2'] for v in self.lookup_df.to_dict('records')}
        self.lookup_data_iso3 = {v['Country_Region']: v['iso3'] for v in self.lookup_df.to_dict('records')}
    
    def clean_df_total(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Run all pre-processing procedures for COVID19 total data
            return:
                    category	total
                0	confirmed	66540034
                1	deaths	    1528868
                2	recovered	42789879
                3	active	    22221289
        """
        if not isinstance(df, pd.DataFrame):
            return pd.DataFrame({})

        df = df.T.reset_index()
        df.columns = ['category', 'total']

        return df
    
    def clean_df_current(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Run all pre-processing procedures for COVID19 current data
            return:
                            location  confirmed  deaths  recovered   active country_code continent
                0                  US   14757000  282299    5624444  8850257           US        NA
                1               India    9677203  140573    9139901   396729           IN        AS
                2              Brazil    6603540  176941    5866657   559942           BR        SA
        """
        if not isinstance(df, pd.DataFrame):
            return pd.DataFrame({})
        
        df['country_code_iso2'] = df['location'].apply(lambda country_name: self.country_name_to_code_iso2(country_name))
        df['country_code_iso3'] = df['location'].apply(lambda country_name: self.country_name_to_code_iso3(country_name))
        df['continent'] = df['country_code_iso2'].apply(lambda country_code_iso2: self.country_code_to_continent(country_code_iso2))

        return df
    
    def country_name_to_code_iso2(self, country_name: str) -> str:
        """ Convert country name to country code iso2 """
        code = self.lookup_data_iso2.get(country_name, '')
        return str(code)

    def country_name_to_code_iso3(self, country_name: str) -> str:
        """ Convert country name to country code iso2 """
        code = self.lookup_data_iso3.get(country_name, '')
        return str(code)
    
    def country_code_to_continent(self, country_code_iso2: str) -> str:
        """ Convert country code iso2 to country code iso2 continent """
        try:
            continent = pc.country_alpha2_to_continent_code(country_code_iso2)
        except:
            continent = 'Other'

        return continent

class DashHelper:
    def generate_table(self, dataframe: pd.DataFrame, max_rows: int = 10) -> html:
        return html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))
            ])
        ], style={'margin-left': 'auto', 'margin-right': 'auto'})
