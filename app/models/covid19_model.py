"""
FILE: covid19_model.py
DESCRIPTION: A model conntaining covid19 data from API
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-DEC-2020
"""
# Import libs
import requests
import pandas as pd


# Covid19 Model
class Covid19Model:

    def __init__(self):
        self.api_endpoint = 'https://covid19.nuttaphat.com/v2/'
    
    def get_current(self) -> pd.DataFrame:
        res = requests.get(self.api_endpoint+'current').json()
        data = res.get('data')
        df = pd.DataFrame(data)
        return df
