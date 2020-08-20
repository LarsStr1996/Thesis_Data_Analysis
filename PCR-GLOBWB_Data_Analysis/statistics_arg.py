import sys
import numpy as np
### Set path --> Directory Input
sys.path.append(r'''Set Path''')

from functions import functions
from variable_list import variables
from run_settings import run_settings

class statistics_arg():
    def __init__(self):
        self.infColObs          = variables().infColObs
        self.seconds_in_year    = variables().seconds_in_year
        
    def hydrostats(observed,modelled):
        kge         = run_settings().metric_1(modelled,observed)
        pearson_r   = run_settings().metric_2(modelled,observed)
        NRMSE       = run_settings().metric_3(modelled,observed)
        return(kge,pearson_r,NRMSE)
        
    def within_year(self,res_name,storCap):
        inflow              = functions.inflow_observed(res_name)
        mean_annual_inflow  = np.mean(functions.pandas_groupby(inflow,'Year',self.infColObs)*self.seconds_in_year)
        storCap             = storCap*10**6
        c       = storCap / mean_annual_inflow
        c       = round(c,2)
        return c
    
    def within_year_modelled(self,res_name,storCap):
        inflow              = functions.modelled_csv(res_name)
        mean_annual_inflow  = np.mean(functions.pandas_groupby(inflow,'Year',self.infColObs)*self.seconds_in_year)
        storCap             = storCap*10**6
        c       = storCap / mean_annual_inflow
        c       = round(c,2)
        return c          
