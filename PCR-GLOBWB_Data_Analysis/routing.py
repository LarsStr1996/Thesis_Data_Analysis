import sys
### Directory Input
sys.path.append(r'''Directory Input''')

import pandas as pd
import numpy as np
from variable_list import variables
from read_NC import nc_reader
from functions import functions
from statistics_arg import statistics_arg
from plots import plots
from Döll import doll
from plots_döll import plots_D
from run_settings import run_settings

import warnings  
warnings.filterwarnings("ignore")
class routing(): 
   def __init__(self,res_name,run_name):   
       self.res_name    = res_name
       self.run_name    = run_name
       self.qplist      = variables().qplist
       self.storCap     = variables().storCap
       self.reservoir_type  = variables().reservoir_type
       
       self.storage_on_off  = run_settings().storage_results
       self.inflow_on_off   = run_settings().inflow_results
       self.outflow_on_off  = run_settings().outflow_results
       
       self.stoColObs   = variables().stoColObs
       self.infColObs   = variables().infColObs
       self.outColObs   = variables().outColObs
       self.outColMod   = variables().outColMod

       ### Directory Input
       self.load_location_statistics    = '''Directory Input'''
       
   def process(self,outflow_location,demand_3_location,demand_4_location):
          time_variable = variables().time_variable 
        
          for z,progress in zip(time_variable,range(1,6)):
             print(progress)
             
             observed1  = []
             modelled1  = []
             demand1    = []
             kge1       = []
             alpha1     = []
             beta1      = []
             within_year= []
             pearson_r1 = []
             NRMSE1     = []
             reservoir_type1    = []
             irri_dependence1   = []
             unmet_demand1      = []
             pearson_r_dem_out1 = []
             stor_info_ratio1  = []
             ind_dom_liv_dependence1        = []
             average_irr_demand1            = []
             average_ind_dom_liv_demand1    = []
             average_downstream_demand1     = []
             
             for k,l in zip(self.res_name,self.storCap):
                    print('     ',k)
                    name            = k + self.run_name
                    outflow         = functions.modelled_csv(name,outflow_location)
                    stor_inf_ratio  = statistics_arg().within_year(k,l)
                    stor_inf_ratio_mean = np.mean(stor_inf_ratio)
                    if self.run_name == 'run3':
                        demand      = functions.modelled_csv(name,demand_3_location)
                        demand      = functions.pandas_groupby(demand,z,self.outColMod)
                        average_downstream_demand = round(np.mean(demand[self.outColMod]),3)
                        average_downstream_demand1.append(average_downstream_demand)
                        demand1.append(demand[self.outColMod])
                    elif self.run_name == 'run4':
                        demand      = functions.modelled_csv(name,demand_4_location)
                        demand      = functions.pandas_groupby(demand,z,self.outColMod)
                        average_downstream_demand = round(np.mean(demand[self.outColMod]),3)
                        average_downstream_demand1.append(average_downstream_demand)
                        demand1.append(demand[self.outColMod])
                    #modelled   = functions.to_pandas_data(modelled)
                    modelled    = functions.pandas_groupby(outflow,z,self.outColMod)
                    if run_settings().results_demand_on_off == True:
                        name_irr    = k + '_irr_withdrawal'
                        name_ind_dom_liv = k + '_ind_dom_liv_withdrawal'
                        name_total  = k + '_total_demand'
                        
                        irr_demand_location     = variables().save_irr_withdrawal_loc
                        ind_dom_liv_location    = variables().save_ind_dom_liv_loc
                        total_location          = variables().save_total_demand
                        
                        irr_demand              = functions.modelled_csv(name_irr,irr_demand_location)
                        ind_dom_live_demand     = functions.modelled_csv(name_ind_dom_liv,ind_dom_liv_location)
                        total_demand            = functions.modelled_csv(name_total,total_location)
                        
                        irri_dependence,ind_dom_liv_dependence = functions.demand_dependence(irr_demand[self.outColMod],ind_dom_live_demand[self.outColMod],total_demand[self.outColMod])
                        irri_dependence         = round(irri_dependence,2)
                        ind_dom_liv_dependence  = round(ind_dom_liv_dependence,2)
                        
                        average_irr_demand      = round(np.mean(irr_demand[self.outColMod]*1000),3)
                        average_dom_live_demand = round(np.mean(ind_dom_live_demand[self.outColMod]*1000),3)
                        
                    if self.storage_on_off == True:
                        observed    = functions.storage_observed(k)
                        observed    = functions.pandas_groupby(observed,z,self.stoColObs)
                        kge,pearson_r,NRMSE = statistics_arg.hydrostats(observed[self.stoColObs],modelled[self.outColMod])
                        observed1.append(observed[self.stoColObs])
                        modelled1.append(modelled[self.outColMod])
                    elif self.inflow_on_off == True:
                        observed    = functions.inflow_observed(k)
                        observed    = functions.pandas_groupby(observed,z,self.infColObs)
                        kge,pearson_r,NRMSE = statistics_arg.hydrostats(observed[self.infColObs],modelled[self.outColMod])
                        observed1.append(observed[self.infColObs])
                        modelled1.append(modelled[self.outColMod])
                    elif run_settings().outflow_results == True:
                        observed    = functions.outflow_observed(k)
                        observed    = functions.pandas_groupby(observed,z,self.outColObs)
                        
                        kge,pearson_r,NRMSE = statistics_arg.hydrostats(observed[self.outColObs],modelled[self.outColMod])
                        if run_settings().results_demand_on_off == True:
                            unmet_demand    = functions.unmet_demand(demand[self.outColMod],modelled[self.outColMod])
                            unmet_demand1.append(unmet_demand)
                            _,pearson_r_dem_out,_ = statistics_arg.hydrostats(demand[self.outColMod],modelled[self.outColMod])
                        observed1.append(observed[self.outColObs])
                        modelled1.append(modelled[self.outColMod])
                    elif run_settings().inflow_and_outflow == True:
                        observed    = functions.outflow_observed(k)
                        observed    = functions.pandas_groupby(observed,z,self.outColObs)
                        kge,pearson_r,NRMSE = statistics_arg.hydrostats(observed[self.outColObs],modelled[self.outColMod])
                        observed1.append(observed[self.outColObs])
                        modelled1.append(modelled[self.outColMod])
                        
                    if run_settings().outflow_results == True:
                        alpha   = functions.alpha(observed[self.outColObs],modelled[self.outColMod])
                        beta    = functions.beta(observed[self.outColObs],modelled[self.outColMod])
                        alpha1.append(alpha)
                        beta1.append(beta)
                    
                    if run_settings().results_demand_on_off == True and run_settings().outflow_results == True:
                        stor_info_ratio1.append(stor_inf_ratio_mean)
                        pearson_r_dem_out1.append(pearson_r_dem_out)
                        
                        irri_dependence1.append(irri_dependence)
                        ind_dom_liv_dependence1.append(ind_dom_liv_dependence)
                        average_irr_demand1.append(average_irr_demand)
                        average_ind_dom_liv_demand1.append(average_dom_live_demand)
                        
                    if np.mean(stor_inf_ratio) < 0.5:
                        within_year.append('within-year')
                    elif np.mean(stor_inf_ratio) == 0.5:
                        within_year.append('carry-over')    
                    elif np.mean(stor_inf_ratio) > 0.5:
                        within_year.append('carry-over')
                    else:
                        within_year.append('no')
                    kge1.append(kge)
                    pearson_r1.append(pearson_r)
                    NRMSE1.append(NRMSE)   
                
             dataoutobs1         = pd.DataFrame(observed1).transpose()
             dataoutinc1         = pd.DataFrame(modelled1).transpose()
             if self.run_name == 'run3':
                 demand          = pd.DataFrame(demand1).transpose()
                 demand.columns  = np.arange(1,41,1)
             elif self.run_name == 'run4':
                 demand          = pd.DataFrame(demand1).transpose()
                 demand.columns  = np.arange(1,41,1)
             else: 
                 demand = 0
             dataoutobs1.columns = np.arange(1,41,1)
             dataoutinc1.columns = np.arange(1,41,1)
             
             if run_settings().outflow_results == True and run_settings().results_demand_on_off == True:
                 data1  = pd.DataFrame([self.res_name,within_year,average_downstream_demand1,self.reservoir_type,kge1,NRMSE1,alpha1,beta1,pearson_r1,unmet_demand1,irri_dependence1,ind_dom_liv_dependence1,average_irr_demand1,average_ind_dom_liv_demand1,pearson_r_dem_out1,stor_info_ratio1]).replace([np.inf, -np.inf], np.nan)
                 data1  = data1.transpose()
                 data1.columns  = ['Name','Within year','Downstream Dem. Ave.','reservoir type','KGE','NRMSE','Alpha','Beta','Pearson R','Unmet Demand','Irrigational Dep.','Ind Dom Liv Dep.','Irr Abs Demand','Ind Dom Liv Abs Demand','Pearson R dem_out_mod','c']

                 ### Directory Input 
                 data1.to_csv('''Directory Input'''+self.run_name+str(z)+"_outflow_stats.csv")
             elif run_settings().inflow_results == True or run_settings().storage_results == True:
                 data1  = pd.DataFrame([self.res_name,kge1,alpha1,beta1,pearson_r1,within_year,NRMSE1]).replace([np.inf, -np.inf], np.nan)
                 data1  = data1.transpose()
                 data1.columns  = ['Name','KGE','Alpha','Beta','Pearson R','Within year','NRMSE']
                 
                 ### Directory Input 
                 data1.to_csv('''Directory Input'''+self.run_name+str(z)+"_storage_stats.csv")
             elif run_settings().outflow_results == True and run_settings().results_demand_on_off == False:
                 data1  = pd.DataFrame([self.res_name,within_year,self.reservoir_type,kge1,NRMSE1,alpha1,beta1,pearson_r1]).replace([np.inf, -np.inf], np.nan)
                 data1  = data1.transpose()
                 data1.columns  = ['Name','Within year','reservoir type','KGE','NRMSE','Alpha','Beta','Pearson R']

                 ### Directory Input 
                 data1.to_csv('''Directory Input'''+self.run_name+str(z)+"_else_stats.csv")
             
             if run_settings().results_plot_on_off == True:   
                 plot   = plots().graphs(z,dataoutobs1,dataoutinc1,self.run_name,demand,self.reservoir_type)
                
             if run_settings().res_stats_plot_on_off ==  True:
                 statistical_graphs     = plots().graphs_statistics(z,data1['KGE'],data1['Pearson R'],data1['NRMSE'],data1['Name'],self.run_name)
                 
             if run_settings().ind_plot_on_off == True:  
                 individual_plot = plots().individual_res_plots()
                 
   def analyis_runs(self):
        unmet_demand = []
        for j in variables().time_variable:
            run1    = functions.modelled_csv('run1'+str(j)+'_else_stats',self.load_location_statistics)
            run2    = functions.modelled_csv('run2'+str(j)+'_else_stats',self.load_location_statistics)
            run3    = functions.modelled_csv('run3'+str(j)+'_outflow_stats',self.load_location_statistics)
            run4    = functions.modelled_csv('run4'+str(j)+'_outflow_stats',self.load_location_statistics)
            
            run1_2_alpha,run1_alpha_to_zero,run2_alpha_to_zero  = functions.alpha_comparison(run1,run2)
            run2_3_alpha,_,run3_alpha_to_zero                   = functions.alpha_comparison(run2,run3)
            run3_4_alpha,run3_alpha_to_zero,run4_alpha_to_zero  = functions.alpha_comparison(run3,run4)
            
            run1_2_beta = functions.beta_comparison(run1,run2)
            run2_3_beta = functions.beta_comparison(run2,run3)
            run3_4_beta = functions.beta_comparison(run3,run4)
            
            run1_2_corr = functions.correlation_comparison(run1,run2)
            run2_3_corr = functions.correlation_comparison(run2,run3)
            run3_4_corr = functions.correlation_comparison(run3,run4)
            
            run1_2_kge  = functions.kge_comparison(run1,run2)
            run2_3_kge  = functions.kge_comparison(run2,run3)
            run3_4_kge  = functions.kge_comparison(run3,run4)
            
            if run_settings().run_comparison_demand == True:
                run3_4_unmet_demand = functions.unmet_demand_comparison(run3,run4)
                unmet_demand.append(run3_4_unmet_demand)
        if run_settings().run_comparison_demand == True:        
            unmet_demand = pd.DataFrame(unmet_demand).transpose()
            unmet_demand.columns = ['Daily','Year,Month','Month','Year,Day','Year']
            print(unmet_demand)
            
    
   def döll_process(self,outflow_location):
        run_name1_ini = "run1"        
        for i in self.run_name:
            iltaobs     = []
            iltamod     = []
            ilfobs      = []
            ilfmod      = []
            isaobsmax   = []
            isaobsmin   = []
            isamodmax   = []
            isamodmin   = []
            isrobs      = []
            isrmod      = []
            itsobs      = []
            itsmod      = []
            iivobs      = []
            iivmod      = []
            name1       = []
            for k in self.res_name:
                 name       = k+i
                 print(name)
                 run_name1  = k+str(run_name1_ini)
                 print(run_name1)
                 outflow_run1 = functions.modelled_csv(run_name1,outflow_location)
                 outflow_runx = functions.modelled_csv(name,outflow_location)
                 mean_ilta_obs,mean_ilta_mod    = doll(k,outflow_run1,outflow_runx).ilta()
                 ilf_obs,ilf_inc                = doll(k,outflow_run1,outflow_runx).ilf()
                 isaobsmaxchange,isaobsminchange,isamodmaxchange,isamodminchange  = doll(k,outflow_run1,outflow_runx).isa()
                 isr_obs,isr_mod                = doll(k,outflow_run1,outflow_runx).isr()
                 its_obs,its_mod                = doll(k,outflow_run1,outflow_runx).its()
                 iiv_obs,iiv_mod                = doll(k,outflow_run1,outflow_runx).iiv()
                 
                 iltaobs.append(mean_ilta_obs)
                 iltamod.append(mean_ilta_mod)
                 ilfobs.append(ilf_obs)
                 ilfmod.append(ilf_inc)
                 isaobsmax.append(isaobsmaxchange)
                 isaobsmin.append(isaobsminchange)
                 isamodmax.append(isamodmaxchange)
                 isamodmin.append(isamodminchange)
                 isrobs.append(isr_obs)
                 isrmod.append(isr_mod)
                 itsobs.append(its_obs)
                 itsmod.append(its_mod)
                 iivobs.append(iiv_obs)
                 iivmod.append(iiv_mod)
                 name1.append(name)
            name = pd.DataFrame(name1)
            
            ILTA = pd.DataFrame([iltaobs,iltamod])
            ILTA = ILTA.round(1)
            ILTA.columns = name
            ILTA = ILTA.transpose()
            ILTA.columns = ['Observed','Modelled']
            ILTA.round(2)
    
            ILF = pd.DataFrame([ilfobs,ilfmod])
            ILF = ILF.round(1)
            ILF.columns = name
            ILF = ILF.transpose()
            ILF.columns = ['Q90_observed','Q90_modelled']
            
            ISA = pd.DataFrame([isaobsmax,isaobsmin,isamodmax,isamodmin])
            ISA = ISA.round(1)
            ISA.columns = name
            ISA = ISA.transpose()
            ISA.columns = ['Observed_MAX','Observed_MIN','Modelled_MAX','Modelled_MIN']
    
            ISR = pd.DataFrame([isrobs,isrmod])
            ISR = ISR.round(1)
            ISR.columns = name
            ISR = ISR.transpose()
            ISR.columns = ['Observed','Modelled']
            
            ITS = pd.DataFrame([itsobs,itsmod])
            ITS = ITS.round(1)
            ITS.columns = name
            ITS = ITS.transpose()
            ITS.columns = ['Observed','Modelled']
            
            IIV = pd.DataFrame([iivobs,iivmod])
            IIV = IIV.round(1)
            IIV.columns = name
            IIV = IIV.transpose()
            IIV.columns = ['Observed','Modelled']
           
            plots = plots_D().plot_döll(i,ILTA,ILF,ISA,ISR,ITS,IIV,name)
       
   def flow_duration_curves(self,outflow_location):
        interpout10     = []
        interpout20     = []
        interpout30     = []
        interpout40     = []
        interpobserved1 = []
        inflow_interpobserved1 = []
        res_name = variables().res_name
        qp = np.arange(0,1.01,0.01)
        for k in res_name:
             name           = k+'run1'
             outflow_run1   = functions.modelled_csv(name,outflow_location)
             outflow_run1   = functions.pandas_groupby_median(outflow_run1,'Day','OUT')
             name           = k+'run2'
             outflow_run2   = functions.modelled_csv(name,outflow_location)
             outflow_run2   = functions.pandas_groupby_median(outflow_run2,'Day','OUT')
             name           = k+'run3'
             outflow_run3   = functions.modelled_csv(name,outflow_location)
             outflow_run3   = functions.pandas_groupby_median(outflow_run3,'Day','OUT')
             name           = k+'run4'
             outflow_run4   = functions.modelled_csv(name,outflow_location)
             outflow_run4   = functions.pandas_groupby_median(outflow_run4,'Day','OUT')
             
             outflow        = functions.outflow_observed(k)
             outflow        = functions.pandas_groupby_median(outflow,'Day','OUT_OBS')
             
             inflow        = functions.inflow_observed(k)
             inflow        = functions.pandas_groupby_median(inflow,'Day','IN_OBS')
             
             xinobserved,yinobserved = functions.flow_duration(inflow['IN_OBS'])
             inflow_interpobserved = functions.interp(xinobserved,yinobserved,qp)
             
             xoutobserved,youtobserved = functions.flow_duration(outflow['OUT_OBS'])
             interpobserved = functions.interp(xoutobserved,youtobserved,qp)
             
             xout1,yout1,qmax1    = functions.flow_duration(outflow_run1['OUT'])
             xout2,yout2,qmax2    = functions.flow_duration(outflow_run2['OUT']) 
             xout3,yout3,qmax3    = functions.flow_duration(outflow_run3['OUT'])
             xout4,yout4,qmax4    = functions.flow_duration(outflow_run4['OUT'])
             
             interpout1     = functions.interp(xout1,yout1,qp)
             interpout2     = functions.interp(xout2,yout2,qp)
             interpout3     = functions.interp(xout3,yout3,qp)
             interpout4     = functions.interp(xout4,yout4,qp)
             interpout10.append(interpout1)
             interpout20.append(interpout2)
             interpout30.append(interpout3)
             interpout40.append(interpout4)
             interpobserved1.append(interpobserved)
             inflow_interpobserved1.append(inflow_interpobserved)
             
        interpout1  = pd.DataFrame(interpout10).transpose()
        interpout2  = pd.DataFrame(interpout20).transpose()
        interpout3  = pd.DataFrame(interpout30).transpose()
        interpout4  = pd.DataFrame(interpout40).transpose()
        interpobserved  = pd.DataFrame(interpobserved1).transpose()
        inflowinterpobserved = pd.DataFrame(inflow_interpobserved1).transpose()
        
        interpout1.columns  = np.arange(1,41,1)
        interpout2.columns  = np.arange(1,41,1)
        interpout3.columns  = np.arange(1,41,1)
        interpout4.columns  = np.arange(1,41,1)
        interpobserved.columns = np.arange(1,41,1)
        inflowinterpobserved.columns = np.arange(1,41,1)
        plot        = plots().flow_duration(interpout1,interpout2,interpout3,interpout4,interpobserved,self.res_name,inflowinterpobserved)   
