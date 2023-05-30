'''
 Desc  : Collection of utilities used in other codes 
'''

import pandas as pd
import urllib.request
import numpy as np


class CmdNuChart(object):
    '''
    wrapper for https://www-nds.iaea.org/relnsd/vcharthtml/api_v0_guide.html
    '''
    
    def __init__(self,http="https://nds.iaea.org/relnsd/v0/data?"):
        self._url = http
        self._df = None
        
    def _return_csv(self,url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
        self._df = pd.read_csv(urllib.request.urlopen(req))
        return
    
    def get_df(self):
        return self._df
    
    def _ask_df(self,url):
        url = self._url + url
        self._return_csv(url)
        return

    def get_nu_chart(self,nuclide="all"):
        self._ask_df("fields=ground_states&nuclides="+nuclide)
        return
    
    def get_nuclear_levels(self,nuclide=None):
        self._ask_df("fields=levels&nuclides="+nuclide)
        return    
    
    def get_fission_yields(self,kind='cumulative',parent=None):
        if kind == 'cumulative':
            name = "fields=cumulative_fy"
        if kind == "independent":
            name = "fields=independent_fy"
        self._ask_df(name+"&parents="+parent)
        return
        
    def get_df_labels(self):
        return list(self._df.columns)
    
    def get_number_of_elements(self):
        return len(self.get_df())
    
    def get_index_non_empty(self,column_name = None):
        return np.where(np.array(self.get_df()[column_name]) != " ")[0]
    
    def get_array(self,column_name=None):
        data = np.array(self.get_df()[column_name])
        
        if len(data.shape) == 2:
            for col in range(data.shape[1]):
                data[:,col][data[:,col]==" "] = np.nan
                try:
                    data[:,col] = data[:,col].astype(float)
                except:
                    data[:,col] = data[:,col].astype(str)
                    
        if len(data.shape) == 1:
            for col in range(data.shape[0]):
                try:
                    data[col] = float(data[col])
                except:
                    data[col] = str(data[col])    
                    
        return data
    
    def get_decays(self,nuclide=None,dtype="bm"): #135xe
        self._ask_df("fields=decay_rads&nuclides="+nuclide+"&rad_types="+dtype)
        return
