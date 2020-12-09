"""
FILE: covid19_model.py
DESCRIPTION: A model conntaining covid19 data from API
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-DEC-2020
"""
# Import libs
import requests
from typing import Dict, Any

import pandas as pd


# Covid19 Model
class Covid19Model:

    def __init__(self):
        self.api_endpoint = 'https://covid19.nuttaphat.com/v2/'
    
    def get_current(self) -> pd.DataFrame:
        data = self._get_data(self.api_endpoint+'current')
        df = pd.DataFrame(data)
        return df
    
    def get_total(self) -> pd.DataFrame:
        data = self._get_data(self.api_endpoint+'total')
        df = pd.DataFrame(data, index=[0]) # escape scalar value error
        return df
    
    def _get_data(self, url: str) -> Dict[str, Any]:
        if not url:
            return []
        res = requests.get(url, verify=False).json()
        data = res.get('data')
        return data
