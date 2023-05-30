import numpy as np
import h5py
from base import base_utilities

class LazyWriter:
    
    '''
    some info here
    
    '''
    
    def __init__(self, output_path=None,name=None):
        
        '''
        some info here
        
        '''
        output_path = base_utilities.fix_path(output_path)
        self._file = output_path+name  +'.lazy'

        return
        
    def get_file_name(self):
        return self._file
    
    def __check_exist(self,path=None,group_name = None):

        with h5py.File(self._file,'r') as f:
            if path is None:
                names = list(f.keys())   
            else:
                names = list(f[path].keys() ) 
            if group_name in names:
                return True
            else:
                return False
    
    def set_general_info(self, dictionary=None):
        
        '''
        some info here
        
        '''
                
        with h5py.File(self._file,'a') as f:

            if self.__check_exist(group_name = "info") is False:
                general_info=f.create_group('info')
            else:
                general_info=f.get("info")
        
            for key, value in dictionary.items():
                self.__save_parameter(general_info,key,value)
        return
    
    
    def write_nuclide_data(self, nuclide_name=None, dtype="info",dictionary=None, vname = None, vvalue = None):        
        
        '''
        some info here
        
        '''
        big_group = "nuclides"       
        
        
        with h5py.File(self._file,'a') as f:
        
            if self.__check_exist(path=None,group_name = big_group) is False:
                f.create_group(big_group)
            
            if self.__check_exist(path=big_group,group_name = nuclide_name) is False:
                group=f.create_group(big_group + "/"+ nuclide_name)
            else:
                group=f.get(big_group + "/"+ nuclide_name)        
                    
            nuclide_name = big_group + "/"+ nuclide_name
            
            if self.__check_exist(path=nuclide_name,group_name = dtype) is False:
                group=f.create_group(nuclide_name+"/"+dtype)
            else:
                group=f.get(nuclide_name+"/"+dtype)      
                
            if dictionary is not None:    
                for key, value in dictionary.items():
                    self.__save_parameter(group,key,value)            
            else:
                self.__save_parameter(group,vname,vvalue)
        return
        

    def __save_parameter(self,group,variable_name,value):
        try:
            group.create_dataset(variable_name, data=value)        
        except (ValueError):     #if exist, overwrite it
            group[variable_name][...] = value 
        return
 
 
        with h5py.File(self.__file,'a') as f:       
            f.create_dataset(path+'/'+name,data=value)
        return

    def __delete_parameter(self,path,name):
        with h5py.File(self.__file,  "a") as f:
            del f[path+'/'+name]
        return



class LazyReader:
    
    def __init__(self, path_file):
        self._file = path_file
        
    def __check_exist(self,path=None,group_name = None):

        with h5py.File(self._file,'r') as f:
            if path is None:
                names = list(f.keys())   
            else:
                names = list(f[path].keys() ) 
            if group_name in names:
                return True
            else:
                return False

    def __convert_to_dict(self, group):
        dic = {}

        for key in group.keys():
            el = group[key]
            if el.shape != ():
                el = np.array(el)
            elif el.dtype == 'object':
                el = str(np.array(el).astype(str))
            else:
                el = float(np.array(el).astype(float))
            dic[key] = el
        return dic    

    
    def get_info(self):
        with h5py.File(self._file,'r') as f:
            return self.__convert_to_dict(f['info'])
    
    def get_nuclides_list(self, group_path = "nuclides"):
        with h5py.File(self._file,'r') as f:
            return list(f[group_path].keys())
    

    def get_parameters(self,name=None, group_path="nuclides",sub_group = "info",variable_not_found=-2):
        with h5py.File(self._file,'r') as f:
            temp = []
            for el in f[group_path].keys():
                try:
                    value = f[group_path][el][sub_group][name]
                except:
                    value = variable_not_found
                temp.append(np.array(value))
            temp = np.array(temp)
            if temp.dtype == "O":
                temp = temp.astype(str)
        return temp
    
    def get_nuclide(self,name=None,loc=None,group_path="nuclides"):
        subgroup1_name = "info"
        subgroup2_name = "data"
        with h5py.File(self._file,'r') as f:
            if name is not None:
                nuclide_name = name
            if loc is not None:
                nuclide_name = self.get_nuclides_list()[loc]
            
            dic1 = self.__convert_to_dict(f[group_path][nuclide_name][subgroup1_name])
            if self.__check_exist(path=group_path+"/"+nuclide_name,group_name = subgroup2_name) is True:
                dic2 = self.__convert_to_dict(f[group_path][nuclide_name][subgroup2_name])
                dic1.update(dic2)
            dic1['lazy_name'] = nuclide_name
        return dic1
        
    def get_data(self):
        pass
