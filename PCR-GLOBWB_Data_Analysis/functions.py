import sys
### Directory Input
sys.path.append(r'''Directory Input''')

import pandas as pd
import numpy as np

class functions():        
   def to_pandas_data(out):
      data          = pd.DataFrame(out)
      data.columns  = ['OUT']
      data['Date']  = pd.date_range(start = '1/1/1980',periods=len(data), freq='D')
      data['Day']   = data['Date'].dt.dayofyear
      data['Month'] = data['Date'].dt.month
      data['Year']  = data['Date'].dt.year
      return(data)
      
   def to_pandas_data_month(out):
      data          = pd.DataFrame(out)
      data.columns  = ['OUT']
      data['Date']  = pd.date_range(start = '1/1/1980',periods=len(data), freq='M')
      data['Day']   = data['Date'].dt.dayofyear
      data['Month'] = data['Date'].dt.month
      data['Year']  = data['Date'].dt.year
      return(data)

   def modelled_csv(name,load_location):
      csv           = pd.read_csv(r""+load_location+name+".csv",delimiter=',')
      return csv 
      
   def inflow_observed(res_name):
      ### Directory Input 
      inflow            = pd.read_csv(r'''Directory Input'''+res_name+".csv", delimiter=';')
      inflow['Date']    = pd.to_datetime(inflow['DATE'],format='%d-%m-%Y')
      inflow['Day']     = inflow['Date'].dt.dayofyear
      inflow['Month']   = inflow['Date'].dt.month
      inflow['Year']    = inflow['Date'].dt.year
      return(inflow)

   def outflow_observed(res_name):
      ### Directory Input
      outflow           = pd.read_csv(r'''Directory Input'''+res_name+".csv", delimiter=';')
      outflow['Date']   = pd.to_datetime(outflow['DATE'],format='%d-%m-%Y')
      outflow['Day']    = outflow['Date'].dt.dayofyear
      outflow['Month']  = outflow['Date'].dt.month
      outflow['Year']   = outflow['Date'].dt.year
      return(outflow)
   
   def storage_observed(res_name):
      ### Directory Input
      storage           = pd.read_csv(r'''Directory Input'''+res_name+".csv", delimiter=';')
      storage['Date']   = pd.to_datetime(storage['DATE'],format='%d-%m-%Y')
      storage['Day']    = storage['Date'].dt.dayofyear
      storage['Month']  = storage['Date'].dt.month
      storage['Year']   = storage['Date'].dt.year 
      return(storage)
      
   def pandas_groupby(data,time_variable,column_name):
      datagrouped   = data.groupby(time_variable)
      data          = datagrouped.aggregate({column_name:np.mean})
      return(data)
      
   def pandas_groupby_median(data,time_variable,column_name):
      datagrouped   = data.groupby(time_variable)
      data          = datagrouped.aggregate({column_name:np.median})
      return(data)  
      
   def pandas_groupby_max(data,time_variable,column_name):
      datagrouped   = data.groupby(time_variable)
      data          = datagrouped.aggregate({column_name:np.max}) 
      return(data)
      
   def pandas_groupby_min(data,time_variable,column_name):
      datagrouped   = data.groupby(time_variable)
      data          = datagrouped.aggregate({column_name:np.min}) 
      return(data)
      
   def pandas_groupby_std(data,time_variable,column_name):
      datagrouped   = data.groupby(time_variable)
      data          = datagrouped.aggregate({column_name:np.std}) 
      return(data) 
      
   def flow_duration(outflow):
      xout          = np.sort(outflow)
      xoutn         = xout.size
      yout          = np.arange(1,xoutn+1) / (xoutn)
      xout = (xout/np.max(xout))*100
      qmax = np.max(xout)
      return(xout,yout,qmax)
      
   def interp(xout,yout,qp):
      interpout     = np.interp(qp,yout,xout)
      return(interpout)
      
   def unmet_demand(demand,modelled_Q):
      #print(np.mean(demand),np.mean(modelled_Q))
      if np.mean(modelled_Q) == 0.0 or np.mean(demand) == 0.0:
          unmet_demand = -999
      else:
          ratio         = modelled_Q-demand
          ratio         = ratio[ratio < 0]
          ratio         = ratio.count()
          unmet_demand  = ratio
      return unmet_demand
  
   def alpha(observed,modelled):
       std_observed     = observed.std()
       std_modelled     = modelled.std()
       alpha            = std_modelled/std_observed
       return alpha
   
   def beta(observed,modelled):
       mean_observed    = observed.mean()
       mean_modelled    = modelled.mean()
       beta             = mean_modelled/mean_observed
       return beta
   
   def demand_dependence(irr_demand,ind_dom_liv_demand,total_demand):
       irr_demand_ratio         = (irr_demand/total_demand)*100
       irr_demand_ratio         = np.mean(irr_demand_ratio)
       ind_dom_liv_demand_ratio = (ind_dom_liv_demand/total_demand)*100
       ind_dom_liv_demand_ratio = np.mean(ind_dom_liv_demand_ratio)
       return irr_demand_ratio,ind_dom_liv_demand_ratio
   
   def alpha_comparison(runx,runy):
       alpha_change     = runx['Alpha']-runy['Beta']
       alpha_to_zero_x  = 1-runx['Alpha']
       alpha_to_zero_y  = 1-runy['Alpha']
       return alpha_change,alpha_to_zero_x,alpha_to_zero_y
   
   def beta_comparison(runx,runy):
       beta_change      = runx['Beta']-runy['Beta']
       beta_to_zero_x   = 1-runx['Beta']
       beta_to_zero_y   = 1-runy['Beta']
       return beta_change,beta_to_zero_x,beta_to_zero_y
   
   def kge_comparison(runx,runy):
       kge_change       = runx['KGE']-runy['KGE']
       return kge_change
   
   def correlation_comparison(runx,runy):
       correlation_change = runx['R']-runy['R']
       return correlation_change
       
   def unmet_demand_comparison(runx,runy):
       unmet_demand_change = runx['unmet demand']-runy['unmet demand']
       return unmet_demand_change
       
       
      
