import numpy as np
from functions import functions
from variable_list import variables

class doll():    
    def __init__(self,res_name,run1_out,runx_out):
        self.col_inflow     = variables().infColObs
        self.col_outflow    = variables().outColObs
        self.col_mod        = variables().outColMod
        self.qp90           = variables().qp90
        self.res_name       = res_name
        self.run1_out       = run1_out
        self.runx_out       = runx_out
        
    def aggregation_mean(self):
        inflow_obs_Y    = functions.pandas_groupby(functions.inflow_observed(self.res_name),["Year"],self.col_inflow)
        outflow_obs_Y   = functions.pandas_groupby(functions.outflow_observed(self.res_name),["Year"],self.col_outflow)
        modelled_Y      = functions.pandas_groupby(self.runx_out,["Year"],self.col_mod)
        nat_Y           = functions.pandas_groupby(self.run1_out,["Year"],self.col_mod)
        inflow_obs_M    = functions.pandas_groupby(functions.inflow_observed(self.res_name),["Month"],self.col_inflow)
        outflow_obs_M   = functions.pandas_groupby(functions.outflow_observed(self.res_name),["Month"],self.col_outflow)
        modelled_M      = functions.pandas_groupby(self.runx_out,["Month"],self.col_mod)
        nat_M           = functions.pandas_groupby(self.run1_out,["Month"],self.col_mod)
        inflow_obs_YM   = functions.pandas_groupby(functions.inflow_observed(self.res_name),["Year","Month"],self.col_inflow)
        outflow_obs_YM  = functions.pandas_groupby(functions.outflow_observed(self.res_name),["Year","Month"],self.col_outflow)
        modelled_YM     = functions.pandas_groupby(self.runx_out,["Year","Month"],self.col_mod)
        nat_YM          = functions.pandas_groupby(self.run1_out,["Year","Month"],self.col_mod)
        return(inflow_obs_M,inflow_obs_Y,inflow_obs_YM,outflow_obs_M,outflow_obs_Y,outflow_obs_YM,modelled_M,modelled_Y,modelled_YM,nat_M,nat_Y,nat_YM)
        #       0               1            2               3             4           5               6           7           8    9       10      11
    
    def aggregation_max_min(self):        
        inflow_obs_M,_,_,outflow_obs_M,_,_,modelled_M,_,_,nat_M,_,_ = doll.aggregation_mean(self)
        
        inflow_obs_M_max    = inflow_obs_M.aggregate({self.col_inflow:np.max})
        outflow_obs_M_max   = outflow_obs_M.aggregate({self.col_outflow:np.max})
        modelled_M_max      = modelled_M.aggregate({self.col_mod:np.max})
        nat_M_max           = nat_M.aggregate({self.col_mod:np.max})
        
        inflow_obs_M_min    = inflow_obs_M.aggregate({self.col_inflow:np.min})
        outflow_obs_M_min   = outflow_obs_M.aggregate({self.col_outflow:np.min})
        modelled_M_min      = modelled_M.aggregate({self.col_mod:np.min})
        nat_M_min           = nat_M.aggregate({self.col_mod:np.min})
        return(inflow_obs_M_max,outflow_obs_M_max,modelled_M_max,nat_M_max,inflow_obs_M_min,outflow_obs_M_min,modelled_M_min,nat_M_min)
        #       0                   1               2               3           4               5               6               7      
        
    def aggregation_std(self):
        inflow_obs_std    = functions.pandas_groupby_std(functions.inflow_observed(self.res_name),["Month"],self.col_inflow)
        outflow_obs_std   = functions.pandas_groupby_std(functions.outflow_observed(self.res_name),["Month"],self.col_outflow)
        modelled_std      = functions.pandas_groupby_std(self.runx_out,["Month"],self.col_mod)
        nat_std           = functions.pandas_groupby_std(self.run1_out,["Month"],self.col_mod)
        return(inflow_obs_std,outflow_obs_std,modelled_std,nat_std)
        
    def ilta(self):
        _,inflow_obs_Y,_,_,outflow_obs_Y,_,_,modelled_Y,_,_,nat_Y,_ = doll.aggregation_mean(self)
        
        ilta_obs        = (outflow_obs_Y[self.col_outflow]-inflow_obs_Y[self.col_inflow])/(inflow_obs_Y[self.col_inflow])*100
        ilta_mod        = (modelled_Y[self.col_mod]-nat_Y[self.col_mod])/nat_Y[self.col_mod]*100
        mean_ilta_obs   = np.mean(ilta_obs)
        mean_ilta_mod   = np.mean(ilta_mod)
        return(mean_ilta_obs,mean_ilta_mod)
        
    def ilf(self):
        _,_,inflow_obs_YM,_,_,outflow_obs_YM,_,_,modelled_YM,_,_,nat_YM = doll.aggregation_mean(self)
        xinobs,yinobs       = functions.flow_duration(inflow_obs_YM[self.col_inflow])
        xoutobs,youtobs     = functions.flow_duration(outflow_obs_YM[self.col_outflow])
        interpoutobs        = functions.interp(xoutobs,youtobs,self.qp90)
        interpinobs         = functions.interp(xinobs,yinobs,self.qp90)
        xoutmod,youtmod     = functions.flow_duration(modelled_YM[self.col_mod])
        xinmod,yinmod       = functions.flow_duration(nat_YM[self.col_mod])
        interpoutmod        = functions.interp(xoutmod,youtmod,self.qp90)
        interpinmod         = functions.interp(xinmod,yinmod,self.qp90)
        
        ilfobs      = (interpoutobs-interpinobs)/interpinobs*100
        ilfmod      = (interpoutmod-interpinmod)/interpinmod*100
        return(ilfobs,ilfmod)
        
    def isa(self):
        inflow_obs_M,_,_,outflow_obs_M,_,_,modelled_M,_,_,nat_M,_,_ = doll.aggregation_mean(self)
        inflow_obs_max,outflow_obs_max,modelled_max,nat_max,_,_,_,_ = doll.aggregation_max_min(self)
        _,_,_,_,inflow_obs_min,outflow_obs_min,modelled_min,nat_min = doll.aggregation_max_min(self)
        
        isaobsmaxchange     = (outflow_obs_max[self.col_outflow]-inflow_obs_max[self.col_inflow])/inflow_obs_max[self.col_inflow]*100
        isaobsminchange     = (outflow_obs_min[self.col_outflow]-inflow_obs_min[self.col_inflow])/inflow_obs_min[self.col_inflow]*100
        isaincmaxchange     = (modelled_max[self.col_mod]-nat_max[self.col_mod])/nat_max[self.col_mod]*100
        isaincminchange     = (modelled_min[self.col_mod]-nat_min[self.col_mod])/nat_min[self.col_mod]*100
        return(isaobsmaxchange,isaobsminchange,isaincmaxchange,isaincminchange)
        
    def isr(self):
        inflow_obs_M,_,_,outflow_obs_M,_,_,modelled_M,_,_,nat_M,_,_ = doll.aggregation_mean(self)
        
        isr_obs     = (outflow_obs_M[self.col_outflow]-inflow_obs_M[self.col_inflow])/inflow_obs_M[self.col_inflow]*100
        isr_mod     = (modelled_M[self.col_mod]-nat_M[self.col_mod])/nat_M[self.col_mod]*100
        
        isr_obs     = np.sqrt(isr_obs*isr_obs)
        isr_mod     = np.sqrt(isr_mod*isr_mod)
        
        isr_obs     = np.mean(isr_obs)
        isr_mod     = np.mean(isr_mod)
        return(isr_obs,isr_mod)
    
    def its(self):
        datainflowobs   = functions.inflow_observed(self.res_name)
        inflowobs       = datainflowobs.loc[datainflowobs.groupby('Year')[self.col_inflow].idxmax().dropna()]
        dataoutflowobs  = functions.outflow_observed(self.res_name)
        outflowobs      = dataoutflowobs.loc[dataoutflowobs.groupby('Year')[self.col_outflow].idxmax().dropna()]
        datamodelled    = self.runx_out
        outflowmod      = datamodelled.loc[datamodelled.groupby('Year')[self.col_mod].idxmax().dropna()]
        datanat         = self.run1_out
        outflownat      = datanat.loc[datanat.groupby('Year')[self.col_mod].idxmax().dropna()]
        
        inflowobs       = inflowobs['Month'].reset_index()
        outflowobs      = outflowobs['Month'].reset_index()
        outflowmod      = outflowmod['Month'].reset_index()
        outflownat      = outflownat['Month'].reset_index()
        
        itsobs          = outflowobs['Month']-inflowobs['Month']
        itsinc          = datamodelled['Month']-outflownat['Month']
        
        itsobs          = np.mean(itsobs)
        itsinc          = np.mean(itsinc)
        return(itsobs,itsinc)
        
    def iiv(self):
        inflow_obs_std,outflow_obs_std,modelled_std,nat_std = doll.aggregation_std(self)
        inflow_obs_M,_,_,outflow_obs_M,_,_,modelled_M,_,_,nat_M,_,_ = doll.aggregation_mean(self)
        
        obsDelta    = (outflow_obs_std[self.col_outflow]/outflow_obs_M[self.col_outflow])-\
                      (inflow_obs_std[self.col_inflow]/inflow_obs_M[self.col_inflow])
        incDelta    = (modelled_std[self.col_mod]/modelled_M[self.col_mod])-\
                      (nat_std[self.col_mod]/nat_M[self.col_mod])
        
        obsNegative          = sum(n < 0 for n in obsDelta.values.flatten())
        obsPositive          = sum(n > 0 for n in obsDelta.values.flatten())
        natincNegative       = sum(n < 0 for n in incDelta.values.flatten())
        natincPositive       = sum(n > 0 for n in incDelta.values.flatten())
        
        obs_iiv     = obsPositive-obsNegative
        inc_iiv     = natincPositive-natincNegative
        return(obs_iiv,inc_iiv)
