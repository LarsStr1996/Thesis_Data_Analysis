import sys
### Directory Input
sys.path.append(r'''Directory Input''')
import netCDF4 as nc4
from run_settings import run_settings

class nc_reader():
   def __init__(self):
      self.run1_location = run_settings().run1_dir
      self.run2_location = run_settings().run2_dir
      self.run3_location = run_settings().run3_dir
      self.run4_location = run_settings().run4_dir
      self.inflowdirobs  = run_settings().inflowdirobs
      self.outflowdirobs = run_settings().outflowdirobs
      self.storagedirobs = run_settings().storagedirobs
        
   def outflow(self):
      run1_outflow = nc4.Dataset(r""+self.run1_location+"discharge_dailyTot_output.nc")
      run2_outflow = nc4.Dataset(r""+self.run2_location+"lake_and_reservoir_outflow_dailyTot_output.nc")
      run3_outflow = nc4.Dataset(r""+self.run3_location+"lake_and_reservoir_outflow_dailyTot_output.nc")
      run4_outflow = nc4.Dataset(r""+self.run4_location+"lake_and_reservoir_outflow_dailyTot_output.nc")
      return run1_outflow,run2_outflow,run3_outflow,run4_outflow
   
   def inflow(self):
      run1_inflow  = nc4.Dataset(r""+self.run1_location+"discharge_dailyTot_output.nc")
      run2_inflow  = nc4.Dataset(r""+self.run2_location+"lake_and_reservoir_inflow_dailyTot_output.nc")
      run3_inflow  = nc4.Dataset(r""+self.run3_location+"lake_and_reservoir_inflow_dailyTot_output.nc")
      run4_inflow  = nc4.Dataset(r""+self.run4_location+"lake_and_reservoir_inflow_dailyTot_output.nc")
      return run1_inflow,run2_inflow,run3_inflow,run4_inflow

   def storage(self): 
      run2_storage  = nc4.Dataset(r""+self.run2_location+"waterBodyStorage_dailyTot_output.nc")
      run3_storage  = nc4.Dataset(r""+self.run3_location+"waterBodyStorage_dailyTot_output.nc")
      run4_storage  = nc4.Dataset(r""+self.run4_location+"waterBodyStorage_dailyTot_output.nc")
      return run2_storage,run3_storage,run4_storage
      
   def irrigational_demand(self):
      irrigational_demand  = nc4.Dataset(r""+self.run3_location+"irrigationWaterWithdrawal_monthAvg_output.nc")
      return irrigational_demand

   def ind_dom_liv_demand(self):
      ind_demand    = nc4.Dataset(r""+self.run3_location+"industryWaterWithdrawal_monthAvg_output.nc") 
      dom_demand    = nc4.Dataset(r""+self.run3_location+"domesticWaterWithdrawal_monthAvg_output.nc") 
      liv_demand    = nc4.Dataset(r""+self.run3_location+"livestockWaterWithdrawal_monthAvg_output.nc")
      return ind_demand,dom_demand,liv_demand
  
   def total_gross_demand(self):
      total_demand  = nc4.Dataset(r""+self.run3_location+"surfaceWaterAbstraction_dailyTot_output.nc") 
      return total_demand
      
   def water_withdrawal_down_res(self):
      run3_demand   =  nc4.Dataset(r""+self.run3_location+"reservoir_downstream_demand_dailyTot_output.nc")
      run4_demand   =  nc4.Dataset(r""+self.run4_location+"reservoir_downstream_demand_dailyTot_output.nc")
      return run3_demand,run4_demand

   def convert_and_save(self,outflow,run_name,res_name,save_location):
      csv1         = outflow.to_csv(r""+save_location+""+res_name+run_name+".csv") 
      print('Csv'+res_name+'Saved')
      return csv1
   
   def outflow_from_NC(self,out,latitude,longitude,parameter):
      discharge   = out.variables[parameter][:,latitude,longitude]
      return discharge  
