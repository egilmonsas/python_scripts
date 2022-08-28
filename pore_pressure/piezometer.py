
from dataclasses import dataclass
from typing import List
import pandas as pd
import datetime

@dataclass
class PiezometerMetaData:
    path:str
    id:str
    elevation:float

class PiezometerDataHandler:
    SKIPROWS= [0,1,3]
    USECOLS = [0,1,2]
    TO_RISE = lambda row: (row.Abs_pressure-10)*9.81
    
    def __init__(self, piezomer_meta_data:List[PiezometerMetaData]) -> None:
        self.piezometers = piezomer_meta_data
    
    def _read_single_piezometer(self,piezometer):
        df = pd.read_table(
            piezometer.path,
            skiprows=self.SKIPROWS,
            usecols=self.USECOLS,
            parse_dates=[['Date','Time']],
            )
        df['Rise']=df["Absolute pressure"].apply(lambda x: (x-10)/9.81)
        df['GWL']=df["Rise"].apply(lambda x: x+piezometer.elevation)
        return (piezometer.id,df)

    def load_piezometer_data(self):
        for piezometer in self.piezometers:
            yield self._read_single_piezometer(piezometer)