'''
 Desc  : Collection of utilities used in other codes 
'''

import pandas as pd
import urllib.request
import numpy as np
from base import base_utilities
from os import listdir
import subprocess



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
        
        
class CmdBetaShape(object):

    def __init__(self,betashape_path=None):
        self._betashape_path = betashape_path
        self._save_path = None
        self._message = None
        
    def set_betashape(self,path=None):
        self._betashape_path = path
        return
        
    def set_save_path(self,path=None):
        self._save_path = path
        return
        
        
    def run_betashape(self,fpath=None,fname = None, options = "",verbose=True):
        bpath = base_utilities.fix_path(self._betashape_path)
        original_files = [f for f in listdir(bpath)] # name of the files in the betashape folder BEFORE launching betashape
        
        file_to_process = base_utilities.fix_path(fpath) + fname  #copy the file to process inside the betashape folder
        subprocess.call(["cp",file_to_process, bpath])
        
        cmd = "betashape "+fname + " " + options  #launch betashape
        message =subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True,cwd=self._betashape_path).communicate()
        if verbose is True:
            print(message[0].decode('ascii'))
            
        full_files = [f for f in listdir(bpath)] # name of the files in the betashape folder AFTER launching betashape
        ii =np.uint32(np.where(np.in1d(np.array(full_files),np.array(original_files),invert = True))[0])
        new_files = np.array(full_files)[ii]     # file created by betashape
        
        file_dir = None
        for filen in new_files:
            if os.path.isdir(bpath+filen) is True:
                file_dir = filen
            subprocess.call(["mv",  bpath+filen, self._save_path])
        self._message = message[0].decode('ascii')
        
        new_files = np.delete(new_files,new_files==file_dir)  
        if file_dir is not None:    #copy ALL the betashape output inside the nuclide folder (file_dir).
            for filen in new_files:
                subprocess.call(["mv",  CmdBEtashape._save_path+"/"+filen, CmdBEtashape._save_path+"/"+file_dir])
        return  
        
    def get_result_state(self,thr=800):
        if self._message is None:
            return "Not executed"
        if len(self._message) == 0:
            return "file not found"
        if len(self._message) >= thr:
            return "file processed"
        if len(self._message) < thr:
            return "file not processed"
        
    def __read_header(self,fname=None):
        with open(fname,"r") as f:    
            nrow = 1
            header = ""
            header += f.readline()
            compact = header.replace(" ","")
            while compact[:6] != "E(keV)":
                text = f.readline()
                compact = text.replace(" ","")
                header+=text
                nrow +=1
            header =header.split("\n")[:-1]
            labels = header[-1]
            labels = labels.split("  ")
            labels_true = [x for x in labels if( (x != '') & (x != ' '))]
            for i in range(len(labels_true)):
                labels_true[i] = labels_true[i].replace(" ","")
        return header, labels_true, nrow
        
    def get_data(self,fname=None,dtype="normal"):
        header,labels,nrow = self.__read_header(fname)
        
        if dtype == "normal":
            data = np.loadtxt(fname,skiprows=nrow)
            return labels, data
        if dtype == "nupartial":
            with open(fname,"r") as f:    
                a = f.readlines()
                a = np.array(a)
                index = np.where(a=='\n')[0]

            nrows1 = index[index>nrow][0] - nrow
            data1 =  np.loadtxt(fname,skiprows=nrow,max_rows=nrows1)
            nrow2 = index[index>nrow][-1] +2   
            data2 =  np.loadtxt(fname,skiprows=nrow2)
            return labels, data1, data2
    
