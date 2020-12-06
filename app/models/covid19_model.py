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
        df = self._get_data(self.api_endpoint+'current')
        return df
    
    def get_total(self) -> pd.DataFrame:
        df = self._get_data(self.api_endpoint+'total')
        return df
    
    def _get_data(self, url: str) -> Dict[str, Any]:
        if not url:
            return []
        res = requests.get(url).json()
        data = res.get('data')
        df = self._create_df(data)
        return df
    
    def _create_df(self, data: Dict[str, Any]) -> pd.DataFrame:
        if not data:
            data = {}
        return pd.DataFrame(data)
