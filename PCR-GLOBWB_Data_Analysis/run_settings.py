''' The run_settings.py module implements the ability for the user to
turn parts on and off with True and False and implement personal
directories. This results in reduced processing time and an enhanced
overview of the modules used during this study.
'''

import hydrostats as hs
class run_settings():
    def __init__(self):       
        ### Modelled input Directory
        self.run1_dir               = '''netCDF Directory'''
        self.run2_dir               = '''netCDF Directory'''
        self.run3_dir               = '''netCDF Directory'''
        self.run4_dir               = '''netCDF Directory'''
        
        ### Observed Input Directory To change input directory for observed data:
        self.inflowdirobs           = '''inflow Directory'''
        self.outflowdirobs          = '''outflow Directory'''
        self.storagedirobs          = '''Storage Directory'''
        
        ### OutputDir. To change Output directory for observed data:
        self.outflow_location       = '''Outflow Results Directory'''
        self.storage_location       = '''Storage Results Directory'''
        self.inflow_location        = '''Inflow Results Directory'''
        self.in_and_outflow_location= '''Inflow + Outflow Results Directory'''
        ### Set metrics that you want to be calculated and plotted (max. 3)
        # Hydrostats documentation: https://readthedocs.org/projects/hydrostats/downloads/pdf/latest/ --> page 45 - 47
        self.metric_1 = hs.kge_2009
        self.metric_2 = hs.pearson_r
        self.metric_3 = hs.nrmse_mean
    
        ### Read NC Files. If True -- > obtains outflow data
        #True/False
        self.outflow_nc             = False                 
        self.only_run3_run4         = False
        self.inflow_nc              = False                
        self.storage_nc             = False               
        self.water_withdrawal_nc    = False      
        self.irrigational_demand_nc = False       
        self.ind_dom_liv_demand_nc  = False    
        self.total_gross_demand_nc  = False
                
        ### Results --> If results == True --> all results are obtained. If resuls_demand == True --> only run3 and run4 are obtained
            ### Results True/False needs to be combined with outflow_results, inflow_results, or storage_results
        ### If results_plot_on_off == True --> Plots are made.
        ### If results_statistical_plot_on_off == True --> Statistical plots are made.
        #True/False
        self.results_on_off         = False     
        self.results_demand_on_off  = False
        
        self.results_plot_on_off    = False
        self.all_runs_combined      = False
        self.res_stats_plot_on_off  = False
        
        self.outflow_results        = False
        self.inflow_results         = False
        self.storage_results        = False
        self.inflow_and_outflow     = False

        ## Plot is divided into two parts to make an improved visualization.
        ## First-half takes into account the first 20 reservoirs
        ## Second-half takes into account the second 20 reservoirs

        # Sets the half to 'first-half' or 'second-half'
        self.plots = '-'
        # Initial settings
        self.plots_first_half = False
        self.plots_second_half = False
        # Sets the half
        if self.plots == 'first-half':
            self.plots_first_half = True
        elif self.plots == 'second-half':
            self.plots_second_half = True

        # Run Comparison
        self.run_comparison         = False
        self.run_comparison_demand  = False
        
        ### Döll results. If True --> Obtains Döll data
        self.doll_on_off            = False
        #True/None
        self.demand_true_none       = None
        
        ### If self_fdc_on_off  == True --> Flow duration curve is made
        self.fdc_on_off             = False
        self.first_half             = False
        self.second_half            = False
        
        ### Individual plot
        self.ind_plot_on_off        = True
        self.run_name               = 'run3'
        self.ind_plot_name          = 'Kayrakkum'
        
        
