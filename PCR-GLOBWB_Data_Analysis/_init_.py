import sys
sys.path.append(r'C:\Users/Lars__000/Documents/PythonScripts/Reservoir_data/30_year_run/hydrostats/Hydrostats_model/')
import pandas as pd
from routing import routing
from read_NC import nc_reader
from variable_list import variables
from functions import functions
from run_settings import run_settings

class runner():
    def __init__(self):
        self.res_name       = variables().res_name
        self.reservoir_type = variables().reservoir_type
        self.latitude       = variables().latitude
        self.longitude      = variables().longitude
        self.parameter      = 'discharge'
        self.parameter2     = 'lake_and_reservoir_outflow'
        self.parameter3     = 'reservoir_downstream_demand'
        self.run_name       = variables().run_name
        self.demand_run_name = variables().demand_run_name
        
        self.save_location_demand3      = ###Directory Input###
        self.save_location_demand4      = ###Directory Input###
        self.save_irr_withdrawal_loc    = ###Directory Input###
        self.save_ind_dom_liv_loc       = ###Directory Input###
        self.save_total_demand          = ###Directory Input###
        self.outflow_location           = run_settings().outflow_location
        self.save_location_storage      = run_settings().storage_location
        
    def nc_reader_runner(self):
        if run_settings().outflow_nc  == True and run_settings().only_run3_run4== False:
            print('Reads NC-files outflow and writes to csv',', Results=',run_settings().outflow_nc,'Runs 3 and 4',run_settings().only_run3_run4)
            run1_outflow,run2_outflow,run3_outflow,run4_outflow             = nc_reader().outflow()
            for i,j,k in zip(self.latitude,self.longitude,self.res_name):
                parameter_nat   = 'discharge'
                outflow1        = nc_reader().outflow_from_NC(run1_outflow,i,j,parameter_nat)
                outflow1        = functions.to_pandas_data(outflow1)
                save            = nc_reader().convert_and_save(outflow1,'run1',k,self.outflow_location)
                
                parameter_lake  = 'lake_and_reservoir_outflow'
                outflow2        = nc_reader().outflow_from_NC(run2_outflow,i,j,parameter_lake)
                outflow2        = functions.to_pandas_data(outflow2)
                save            = nc_reader().convert_and_save(outflow2,'run2',k,self.outflow_location) 
                outflow3        = nc_reader().outflow_from_NC(run3_outflow,i,j,parameter_lake)
                outflow3        = functions.to_pandas_data(outflow3)
                save            = nc_reader().convert_and_save(outflow3,'run3',k,self.outflow_location) 
                outflow4        = nc_reader().outflow_from_NC(run4_outflow,i,j,parameter_lake)
                outflow4        = functions.to_pandas_data(outflow4)
                save            = nc_reader().convert_and_save(outflow4,'run4',k,self.outflow_location) 
                
        elif run_settings().outflow_nc  == True and run_settings().only_run3_run4== True:
            print('Reads NC-files outflow and writes to csv')
            run1_outflow,run2_outflow,run3_outflow,run4_outflow             = nc_reader().outflow()
            for i,j,k in zip(self.latitude,self.longitude,self.res_name):
                print(k) 
                parameter_lake  = 'lake_and_reservoir_outflow'
                outflow         = nc_reader().outflow_from_NC(run3_outflow,i,j,parameter_lake)
                outflow         = functions.to_pandas_data(outflow)
                save            = nc_reader().convert_and_save(outflow,'run3',k,self.outflow_location)     
                outflow         = nc_reader().outflow_from_NC(run4_outflow,i,j,parameter_lake)
                outflow         = functions.to_pandas_data(outflow)
                save            = nc_reader().convert_and_save(outflow,'run4',k,self.outflow_location)  
                        
        elif run_settings().inflow_nc   == True:
            print('Reads NC-files inflow and writes to csv')
            run1_inflow,run2_inflow,run3_inflow,run4_inflow                 = nc_reader().inflow()
            run                 = [run1_inflow,run2_inflow,run3_inflow,run4_inflow]
            for r,rname in zip(run,self.run_name):
                print(rname,'processing')
                for i,j,k in zip(self.latitude,self.longitude,self.res_name):
                    print(k)
                    if r == run1_inflow:
                        break
                        self.parameter = 'discharge'
                        inflow  = nc_reader().outflow_from_NC(r,i,j,self.parameter)
                        inflow  = functions.to_pandas_data(inflow)
                        save    = nc_reader().convert_and_save(inflow,'run1',k,self.inflow_location)
                    else: 
                        parameterinflow = 'lake_and_reservoir_inflow'
                        inflow  = nc_reader().outflow_from_NC(r,i,j,parameterinflow)
                        inflow  = functions.to_pandas_data(inflow)
                        save    = nc_reader().convert_and_save(inflow,rname,k,run_settings().inflow_location)
        elif run_settings().storage_nc  == True:
            print('Reads NC-files storage and writes to csv')
            run2_storage,run3_storage,run4_storage  = nc_reader().storage() 
            #run1_storage,run2_storage,
            run                 = [run2_storage,run3_storage,run4_storage]
            #run2_storage
            self.run_name       = ['run2','run3','run4']
            for r,rname in zip(run,self.run_name):
                print(rname,' processing')
                for i,j,k in zip(self.latitude,self.longitude,self.res_name):
                    print(k)
                    par_stor    = 'lake_and_reservoir_storage'
                    storage     = nc_reader().outflow_from_NC(r,i,j,par_stor)
                    storage     = functions.to_pandas_data(storage)
                    save        = nc_reader().convert_and_save(storage,rname,k,self.save_location_storage)
                
        elif run_settings().water_withdrawal_nc   == True:
            print('Reads NC-files demand and writes to csv')
            run3_demand,run4_demand                                     = nc_reader().water_withdrawal_down_res()
            run                 = [run3_demand,run4_demand]
            parameter3_2        = 'reservoir_downstream_demand'
            self.parameter      = 'reservoir_downstream_demand'
            save_location       = [self.save_location_demand3,self.save_location_demand4]
            for i,j,k in zip(self.latitude,self.longitude,self.res_name):
                print(k)
                outflow         = nc_reader().outflow_from_NC(run3_demand,i,j,parameter3_2)
                outflow_3       = outflow*24*3600
                outflow_3       = functions.to_pandas_data(outflow_3)
                save            = nc_reader().convert_and_save(outflow_3,'run3',k,self.save_location_demand3)
                outflow         = nc_reader().outflow_from_NC(run4_demand,i,j,self.parameter)
                outflow         = functions.to_pandas_data(outflow)
                save            = nc_reader().convert_and_save(outflow,'run4',k,self.save_location_demand4)
                
        elif run_settings().irrigational_demand_nc == True:
            print('Reads NC-files')
            irrigational_demand = nc_reader().irrigational_demand()
            self.parameter      = 'irrigation_withdrawal'
            for i,j,k in zip(self.latitude,self.longitude,self.res_name):
                print(k)
                irr_demand      = nc_reader().outflow_from_NC(irrigational_demand,i,j,self.parameter)
                irr_demand      = functions.to_pandas_data_month(irr_demand)
                save            = nc_reader().convert_and_save(irr_demand,'_irr_withdrawal',k,self.save_irr_withdrawal_loc)
                
        elif run_settings().ind_dom_liv_demand_nc == True:
            print('Reads NC-files')
            ind_demand,dom_demand,liv_demand = nc_reader().ind_dom_liv_demand()
            self.parameter_ind  = 'industry_water_withdrawal'
            self.parameter_dom  = 'domestic_water_withdrawal'
            self.parameter_liv  = 'livestock_water_withdrawal'
            for i,j,k in zip(self.latitude,self.longitude,self.res_name):
                print(k)
                i_demand        = nc_reader().outflow_from_NC(ind_demand,i,j,self.parameter_ind)
                d_demand        = nc_reader().outflow_from_NC(dom_demand,i,j,self.parameter_dom)
                l_demand        = nc_reader().outflow_from_NC(liv_demand,i,j,self.parameter_liv)
                ind_dom_liv_dem = i_demand+d_demand+l_demand
                ind_dom_liv_dem = functions.to_pandas_data_month(ind_dom_liv_demand)
                save            = nc_reader().convert_and_save(ind_dom_liv_dem,'_ind_dom_liv_withdrawal',k,self.save_ind_dom_liv_loc)
                
        elif run_settings().total_gross_demand_nc == True:
            print('Reads NC-files demand and writes to csv')
            #run3_demand,run4_demand                    = nc_reader().water_withdrawal_down_res()
            #run3_total_demand                           = nc_reader().total_gross_demand()
            run3_downstream_demand,run4_downstream_demand = nc_reader().water_withdrawal_down_res()
            
            self.parameter      = 'reservoir_downstream_demand'
            save_location       = [self.save_location_demand3,self.save_location_demand4]
            for i,j,k in zip(self.latitude,self.longitude,self.res_name):
                print(k)
                ddemand3        = nc_reader().outflow_from_NC(run3_downstream_demand,i,j,self.parameter)
                #totaldemand3    = nc_reader().outflow_from_NC(run3_total_demand,i,j,'surface_water_abstraction')*24*3600
                outflow_3       = functions.to_pandas_data(ddemand3)
                save            = nc_reader().convert_and_save(outflow_3,'run3',k,self.save_location_demand3)
                outflow         = nc_reader().outflow_from_NC(run4_downstream_demand,i,j,self.parameter)
                outflow         = functions.to_pandas_data(outflow)
                save            = nc_reader().convert_and_save(outflow,'run4',k,self.save_location_demand4)
                
    def results(self):
        if run_settings().results_on_off == True:
            if run_settings().outflow_results == True:
                print('Results outflow Process. Including statistics, plots and statistical plots')
                for i,j in zip(self.run_name,self.res_name):
                    print('start',i)
                    results     = routing(self.res_name,i).process(self.outflow_location,self.save_location_demand3,self.save_location_demand4)
            elif run_settings().inflow_results == True:
                print('Results inflow Process. Including statistics, plots and statistical plots')
                for i,j in zip(self.run_name,self.res_name):
                    print('start',i)
                    inflow_loc  = variables().inflow_location
                    results     = routing(self.res_name,i).process(inflow_loc,self.save_location_demand3,self.save_location_demand4)
            elif run_settings().storage_results == True:
                print('Results storage Process. Including statistics, plots and statistical plots')
                for i,j in zip(self.run_name,self.res_name):
                    print('start',i)
                    storage_loc = self.save_location_storage
                    results     = routing(self.res_name,i).process(storage_loc,self.save_location_demand3,self.save_location_demand4)
            elif run_settings().inflow_and_outflow == True:
                print('Results in- and outflow Process. Including statistics, plots and statistical plots')
                for i,j in zip(self.run_name,self.res_name):
                    print('start',i)
                    in_and_out_loc = self.save_in_and_out
                    results     = routing(self.res_name,i).process(run_settings().in_and_outflow_location,self.save_location_demand3,self.save_location_demand4)
            
        elif run_settings().results_demand_on_off == True:
            if run_settings().outflow_results == True:
                print('Results outflow Process. Including statistics, plots and statistical plots')
                run_name        = variables().demand_run_name
                for i,j in zip(run_name,self.res_name):
                    print('start',i)
                    results     = routing(self.res_name,i).process(self.outflow_location,self.save_location_demand3,self.save_location_demand4)
            elif run_settings().inflow_results == True:
                print('Results inflow Process. Including statistics, plots and statistical plots')
                run_name        = variables().demand_run_name
                for i,j in zip(run_name,self.res_name):
                    print('start',i)
                    results     = routing(self.res_name,i).process(variables().inflow_location,self.save_location_demand3,self.save_location_demand4)
            elif run_settings().storage_results == True:
                print('Results inflow Process. Including statistics, plots and statistical plots')
                self.run_name   = variables().demand_run_name
                for i,j in zip(self.run_name,self.res_name):
                    print('start',i)
                    results     = routing(self.res_name,i).process(run_settings().storage_location,self.save_location_demand3,self.save_location_demand4)
            elif run_settings().inflow_and_outflow == True:
                print('Results in- and outflow Process. Including statistics, plots and statistical plots')
                self.run_name   = variables().demand_run_name
                for i,j in zip(self.run_name,self.res_name):
                    print('start',i)
                    results     = routing(self.res_name,i).process(run_settings().in_and_outflow_location,self.save_location_demand3,self.save_location_demand4)
            
    
    def analyis_run(self):
        if run_settings().run_comparison == True:
            print('Analysis process')
            output  = routing(self.res_name,self.run_name).analyis_runs()
                        
    def doll_process(self): 
        if run_settings().doll_on_off == True and run_settings().demand_true_none == True:
            print("Doll process")
            doll    = routing(self.res_name,self.demand_run_name).döll_process(self.outflow_location)
        elif run_settings().doll_on_off == True and run_settings().demand_true_none == None:
            doll    = routing(self.res_name,self.run_name).döll_process(self.outflow_location)
            
    def flow_duration(self):
        if run_settings().fdc_on_off == True:
            print('FDC process')
            fdc     = routing(self.res_name,self.run_name).flow_duration_curves(self.outflow_location)
