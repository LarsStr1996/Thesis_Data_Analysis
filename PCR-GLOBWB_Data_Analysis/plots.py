import sys
### Set Path
sys.path.append(r'''Directory Input''')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from variable_list import variables
from run_settings import run_settings
from functions import functions
from matplotlib.pyplot import cm
from cycler import cycler
import seaborn as sns
import matplotlib as mpl

class plots():
   def __init__(self):
       self.outflow_location    = run_settings().outflow_location
       self.storage_location    = run_settings().storage_location
       self.inflow_location     =run_settings().inflow_location 
       self.outflow_on_off      = run_settings().outflow_results
       self.storage_on_off      = run_settings().storage_results
       self.inflow_on_off       = run_settings().inflow_results
       self.res_name            = variables().res_name
       self.reservoir_type      = variables().reservoir_type
       self.inflow_and_outflow  = run_settings().inflow_and_outflow
       
   def graphs(self,time,dataoutobs1,dataoutinc1,run_name,demand,reservoir_type):
       first_half = run_settings().plots_first_half
       second_half = run_settings().plots_second_half
       if first_half == True:
          xrange=range(1,21)
          res_name = self.res_name[0:20]
       elif second_half == True:
          xrange=range(1,21)
          res_name = self.res_name[20:40]

       sns.set(font_scale=2)
       
       n = 40
       L = n//1.6
       
       LW = 3.0
       plt.rcParams.update({'font.size': 20})
       n_color = 4
       ccc = cm.winter(np.linspace(0.0,1.0,n_color))
       ccc2 = cm.spring(np.linspace(0.0,1.0,n_color))
       ccc3 = cm.cool(np.linspace(0.0,1.0,n_color))
       ccobserved = cm.autumn(np.linspace(0.0,1.0,4))
       fig, ax     = plt.subplots(nrows=5,ncols=4,figsize = (n,L),sharex=True,dpi=150)
       fig.subplots_adjust(top=0.98,left=0.05,right=0.95,bottom=0.10)
       
       
       for ch,na,ty in zip(xrange,res_name,reservoir_type):
              axis   = ax.flatten()[ch-1]       
              res_name_mod1 = na + 'run1'
              res_name_mod2 = na + 'run2'
              res_name_mod3 = na + 'run3'
              res_name_mod4 = na + 'run4'              
              if second_half == True:        
                 if run_settings().all_runs_combined == True and run_settings().outflow_results == True:
                    ### Directory Input (3x)
                    load_location_inc  = '''Directory Input'''
                    dataoutincrun1 = functions.modelled_csv(res_name_mod1,load_location_inc)
                    dataoutincrun1 = functions.pandas_groupby(dataoutincrun1,time,'OUT')
                    load_location_dem3 = '''Directory Input'''
                    load_location_dem4 = '''Directory Input'''
                    demandrun3     = functions.modelled_csv(res_name_mod3,load_location_dem3)
                    demandrun3     = functions.pandas_groupby(demandrun3,time,'OUT')
                    demandrun4     = functions.modelled_csv(res_name_mod4,load_location_dem4)
                    demandrun4     = functions.pandas_groupby(demandrun4,time,'OUT')
                    
                    dataoutincrun2 = functions.modelled_csv(res_name_mod2,load_location_inc)
                    dataoutincrun2 = functions.pandas_groupby(dataoutincrun2,time,'OUT')
                    dataoutincrun3 = functions.modelled_csv(res_name_mod3,load_location_inc)
                    dataoutincrun3 = functions.pandas_groupby(dataoutincrun3,time,'OUT')
                    dataoutincrun4 = functions.modelled_csv(res_name_mod4,load_location_inc)
                    dataoutincrun4 = functions.pandas_groupby(dataoutincrun4,time,'OUT')
                 elif run_settings().all_runs_combined == True and run_settings().storage_results == True:
                    ### Directory Input
                    load_location_inc  = '''Directory Input'''
                    dataoutincrun2 = functions.modelled_csv(res_name_mod2,load_location_inc)
                    dataoutincrun2 = functions.pandas_groupby(dataoutincrun2,time,'OUT')
                    dataoutincrun3 = functions.modelled_csv(res_name_mod3,load_location_inc)
                    dataoutincrun3 = functions.pandas_groupby(dataoutincrun3,time,'OUT')
                    dataoutincrun4 = functions.modelled_csv(res_name_mod4,load_location_inc)
                    dataoutincrun4 = functions.pandas_groupby(dataoutincrun4,time,'OUT')
                 elif run_settings().all_runs_combined == True and run_settings().inflow_and_outflow == True:
                    ### Directory Input (2x)
                    load_location_inc = '''Directory Input'''
                    load_location_outflow = '''Directory Input'''
                    datainrun1 = functions.modelled_csv(res_name_mod1,load_location_inc)
                    datainrun1 = functions.pandas_groupby(datainrun1,time,'OUT')
                    datainrun2 = functions.modelled_csv(res_name_mod2,load_location_inc)
                    datainrun2 = functions.pandas_groupby(datainrun2,time,'OUT')
                    datainrun3 = functions.modelled_csv(res_name_mod3,load_location_inc)
                    datainrun3 = functions.pandas_groupby(datainrun3,time,'OUT')
                    datainrun4 = functions.modelled_csv(res_name_mod4,load_location_inc)
                    datainrun4 = functions.pandas_groupby(datainrun4,time,'OUT')
                    dataoutincrun4 = functions.modelled_csv(res_name_mod4,load_location_outflow)
                    dataoutincrun4 = functions.pandas_groupby(dataoutincrun4,time,'OUT')
                              
                 length_ = range(1,len(dataoutobs1[ch])+1)
                 if run_settings().all_runs_combined == True and run_settings().outflow_results == True:
                       q1 = axis.plot(length_,demandrun3['OUT'],color='dimgray',label='3',linewidth=LW)
                       q2 = axis.plot(length_,demandrun4['OUT'],color='dimgray',linestyle='--',label='4',linewidth=LW)

                       o1 = axis.plot(length_,dataoutobs1[ch+20],color=ccobserved[1],label='Observed',linewidth=LW)

                       p1 = axis.plot(length_,dataoutincrun1['OUT'],color=ccc[0],label='1',linewidth=LW)
                       p2 = axis.plot(length_,dataoutincrun2['OUT'],color=ccc3[0],label='2',linewidth=LW)
                       p3 = axis.plot(length_,dataoutincrun3['OUT'],color=ccc[2],label='3',linewidth=LW)
                       p4 = axis.plot(length_,dataoutincrun4['OUT'],color=ccc2[3],linestyle='--',label='4',linewidth=LW)

                       axis.xaxis.set_tick_params(which='both', labelbottom=True)
                       #axis.set_yscale('symlog')
                       axis.set_ylim(0)
                 elif run_settings().storage_results == True:
                       #o1 = axis.plot(length_,dataoutobs1[ch+20],color=ccobserved[1],label='Observed',linewidth=LW)
                       p2 = axis.plot(length_,dataoutincrun2['OUT'],color=ccc3[0],label='2',linewidth=LW)
                       p3 = axis.plot(length_,dataoutincrun3['OUT'],color=ccc[2],label='3',linewidth=LW)
                       p4 = axis.plot(length_,dataoutincrun4['OUT'],color=ccc2[3],linestyle='--',label='4',linewidth=LW)

                       axis.xaxis.set_tick_params(which='both', labelbottom=True)
                       #axis.set_yscale('log')
                       axis.set_ylim(0)
                 elif run_settings().all_runs_combined == True and run_settings().inflow_and_outflow == True:
                       o1 = axis.plot(length_,dataoutobs1[ch+20],color=ccobserved[1],label='Observed',linewidth=LW)
                       p1 = axis.plot(length_,datainrun1['OUT'],color=ccc[0],label='1',linewidth=LW)
                       p4 = axis.plot(length_,datainrun4['OUT'],color=ccc2[3],linestyle='--',label='4',linewidth=LW)
                       p2 = axis.plot(length_,dataoutincrun4['OUT'],color=ccc3[0],label='4 outflow',linewidth=LW)
                       #p3 = axis.plot(length_,datainrun3['OUT'],color=ccc[2],label='',linewidth=LW) 
                 label  = na
                 axis.set_title(label=label,fontsize=L,fontweight='bold')
                 chalte = ch+20
                 print(chalte)
                 #if time    == ['Year']:
                        #axis.set_xticks(['1980','1990','2000','2010'])
                        #axis.set_xlim(1980,2010)
                        #if ch ==1 or ch == 5 or ch == 9 or ch == 13 or ch == 17:
                           #axis.set_xlabel('Year')
                        #if chalte > 36:
                           #axis.set_xlabel('Year')
                 if time  == ['Month']:
                        #axis.set_xticks(np.arange(0,13,1))
                        axis.set_xlim(1,12)
                        #if chalte > 36:
                           #axis.set_xlabel('Month')
                 elif time  == ['Month','Day']:
                        axis.set_xticks(np.arange(0,400,100))
                        axis.set_xticklabels([0,100,200,300])
                        axis.set_xlim(0,376)
                        #if chalte > 36:
                           #axis.set_xlabel('Day')
                 elif time  == ['Year','Month']:
                        axis.set_xticks(np.arange(0,400,100))
                        axis.set_xticklabels([0,100,200,300])
                        axis.set_xlim(0,372)
                        if chalte > 36:
                           axis.set_xlabel('Month')
                 elif time  == ['Year','Day']:
                        axis.set_xticks(np.arange(0,16000,3650))
                        axis.set_xticklabels([1980,1990,2000,2010])
                        axis.set_xlim(3650,7300)
                        if chalte > 36:
                           axis.set_xlabel('Year')
      
              elif first_half == True:
                 if run_settings().all_runs_combined == True and run_settings().outflow_results == True:
                    ### Directory Input (3x)
                    load_location_inc  = '''Directory Input'''
                    dataoutincrun1 = functions.modelled_csv(res_name_mod1,load_location_inc)
                    dataoutincrun1 = functions.pandas_groupby(dataoutincrun1,time,'OUT')
                    load_location_dem3 = '''Directory Input'''
                    load_location_dem4 = '''Directory Input'''
                    demandrun3     = functions.modelled_csv(res_name_mod3,load_location_dem3)
                    demandrun3     = functions.pandas_groupby(demandrun3,time,'OUT')
                    demandrun4     = functions.modelled_csv(res_name_mod4,load_location_dem4)
                    demandrun4     = functions.pandas_groupby(demandrun4,time,'OUT')
                    dataoutincrun2 = functions.modelled_csv(res_name_mod2,load_location_inc)
                    dataoutincrun2 = functions.pandas_groupby(dataoutincrun2,time,'OUT')
                    dataoutincrun3 = functions.modelled_csv(res_name_mod3,load_location_inc)
                    dataoutincrun3 = functions.pandas_groupby(dataoutincrun3,time,'OUT')
                    dataoutincrun4 = functions.modelled_csv(res_name_mod4,load_location_inc)
                    dataoutincrun4 = functions.pandas_groupby(dataoutincrun4,time,'OUT')
                 elif run_settings().storage_results == True:
                    ### Directory Input
                    load_location_inc  = '''Directory Input'''
                    dataoutincrun2 = functions.modelled_csv(res_name_mod2,load_location_inc)
                    dataoutincrun2 = functions.pandas_groupby(dataoutincrun2,time,'OUT')
                    dataoutincrun3 = functions.modelled_csv(res_name_mod3,load_location_inc)
                    dataoutincrun3 = functions.pandas_groupby(dataoutincrun3,time,'OUT')
                    dataoutincrun4 = functions.modelled_csv(res_name_mod4,load_location_inc)
                    dataoutincrun4 = functions.pandas_groupby(dataoutincrun4,time,'OUT')
                 elif run_settings().all_runs_combined == True and run_settings().inflow_and_outflow == True:
                    ### Directory Input
                    load_location_inc = '''Directory Input'''
                    load_location_outflow = '''Directory Input'''
                    datainrun1 = functions.modelled_csv(res_name_mod1,load_location_inc)
                    datainrun1 = functions.pandas_groupby(datainrun1,time,'OUT')
                    datainrun2 = functions.modelled_csv(res_name_mod2,load_location_inc)
                    datainrun2 = functions.pandas_groupby(datainrun2,time,'OUT')
                    datainrun3 = functions.modelled_csv(res_name_mod3,load_location_inc)
                    datainrun3 = functions.pandas_groupby(datainrun3,time,'OUT')
                    datainrun4 = functions.modelled_csv(res_name_mod4,load_location_inc)
                    datainrun4 = functions.pandas_groupby(datainrun4,time,'OUT')
                    dataoutincrun4 = functions.modelled_csv(res_name_mod4,load_location_outflow)
                    dataoutincrun4 = functions.pandas_groupby(dataoutincrun4,time,'OUT')
                              
                 length_ = range(1,len(dataoutobs1[ch])+1)
                 if run_settings().all_runs_combined == True and run_settings().outflow_results == True:
                       q1 = axis.plot(length_,demandrun3['OUT'],color='dimgray',label='3',linewidth=LW)
                       q2 = axis.plot(length_,demandrun4['OUT'],color='dimgray',linestyle='--',label='4',linewidth=LW)

                       o1 = axis.plot(length_,dataoutobs1[ch],color=ccobserved[1],label='Observed',linewidth=LW)

                       p1 = axis.plot(length_,dataoutincrun1['OUT'],color=ccc[0],label='1',linewidth=LW)
                       p2 = axis.plot(length_,dataoutincrun2['OUT'],color=ccc3[0],label='2',linewidth=LW)
                       p3 = axis.plot(length_,dataoutincrun3['OUT'],color=ccc[2],label='3',linewidth=LW)
                       p4 = axis.plot(length_,dataoutincrun4['OUT'],color=ccc2[3],linestyle='--',label='4',linewidth=LW)

                       axis.xaxis.set_tick_params(which='both', labelbottom=True)
                       #axis.set_yscale('symlog')
                       axis.set_ylim(0)
                 elif run_settings().storage_results == True:
                       #o1 = axis.plot(length_,dataoutobs1[ch],color=ccobserved[1],label='Observed',linewidth=LW)
                       p2 = axis.plot(length_,dataoutincrun2['OUT'],color=ccc3[0],label='2',linewidth=LW)
                       p3 = axis.plot(length_,dataoutincrun3['OUT'],color=ccc[2],label='3',linewidth=LW)
                       p4 = axis.plot(length_,dataoutincrun4['OUT'],color=ccc2[3],linestyle='--',label='4',linewidth=LW)

                       axis.xaxis.set_tick_params(which='both', labelbottom=True)
                       #axis.set_yscale('log')
                       axis.set_ylim(0)
                 elif run_settings().all_runs_combined == True and run_settings().inflow_and_outflow == True:
                       o1 = axis.plot(length_,dataoutobs1[ch],color=ccobserved[1],label='Observed',linewidth=LW)
                       p1 = axis.plot(length_,datainrun1['OUT'],color=ccc[0],label='1',linewidth=LW)
                       p4 = axis.plot(length_,datainrun4['OUT'],color=ccc2[3],linestyle='--',label='4',linewidth=LW)
                       p2 = axis.plot(length_,dataoutincrun4['OUT'],color=ccc3[0],label='4 outflow',linewidth=LW)
                       #p3 = axis.plot(length_,datainrun3['OUT'],color=ccc[2],label='',linewidth=LW) 
                 label  = na
                 axis.set_title(label=label,fontsize=L,fontweight='bold')
                 if time    == ['Year']:
                        #axis.set_xticks(['1980','1990','2000','2010'])
                        #axis.set_xlim(1980,2010)
                        #if ch ==1 or ch == 5 or ch == 9 or ch == 13 or ch == 17:
                           #axis.set_xlabel('Year')
                        if ch > 16:
                           axis.set_xlabel('Year')
                 if time  == ['Month']:
                        #axis.set_xticks(np.arange(0,13,1))
                        axis.set_xlim(1,12)
                        if ch > 16:
                           axis.set_xlabel('Month')
                 elif time  == ['Month','Day']:
                        axis.set_xticks(np.arange(0,400,100))
                        axis.set_xticklabels([0,100,200,300])
                        axis.set_xlim(0,376)
                        if ch > 16:
                           axis.set_xlabel('Day')
                 elif time  == ['Year','Month']:
                        axis.set_xticks(np.arange(0,400,100))
                        axis.set_xticklabels([0,100,200,300])
                        axis.set_xlim(0,372)
                        if ch > 16:
                           axis.set_xlabel('Month')
                 elif time  == ['Year','Day']:
                        axis.set_xticks(np.arange(0,16000,3650))
                        axis.set_xticklabels([1980,1990,2000,2010])
                        axis.set_xlim(3650,7300)
                        if ch > 16:
                           axis.set_xlabel('Year')
               
       if self.outflow_on_off    == True or self.inflow_on_off == True or run_settings().inflow_and_outflow == True:
           fig.text(0.02, 0.5, 'Discharge & Demand [cms]', va='center',\
                    rotation='vertical',fontsize=L)
           #fig.text(0.02, 0.4, 'Discharge [cms]', va='center',\
                    #fontweight='bold', rotation='vertical',fontsize=L)
           
       elif self.storage_on_off  == True:
           fig.text(0.02, 0.5, 'Storage [cm]', va='center',\
                    rotation='vertical',fontsize=L)
       
               
       if run_settings().all_runs_combined == True and run_settings().storage_results == True:        
          handles, labels       = axis.get_legend_handles_labels()
          handles2,labels2 = handles[:],labels[:]
          #observed_legend = fig.legend(handles[0:1],labels[0:1],loc='upper center',fancybox=True,\
          #                          bbox_to_anchor=(0.35, 0.07),ncol=7,handlelength=3,fontsize=L+5)
          #observed_legend.set_title('Observed Data:',prop={'weight': 'bold','size':L+5})
          first_legend = fig.legend(handles[0:3],labels[0:3],loc='upper center',fancybox=True,\
                                    bbox_to_anchor=(0.5, 0.07),ncol=7,handlelength=3,fontsize=L+5)
          first_legend.set_title('Runs:',prop={'weight': 'bold','size':L+5})
          for line in first_legend.legendHandles:
             line.set_linewidth(8.0)
          #axa = plt.gca().add_artist(first_legend)
             
       elif run_settings().all_runs_combined == True and run_settings().outflow_results == True:
          handles, labels       = axis.get_legend_handles_labels()
          handles2,labels2 = handles[:],labels[:]
          observed_legend = fig.legend(handles[2:3],labels[2:3],loc='upper center',fancybox=True,\
                                    bbox_to_anchor=(0.2, 0.07),ncol=7,handlelength=3,fontsize=L+5)
          observed_legend.set_title('Observed Data:',prop={'weight': 'bold','size':L+5})
          first_legend = fig.legend(handles[3:7],labels[3:7],loc='upper center',fancybox=True,\
                                    bbox_to_anchor=(0.43, 0.07),ncol=7,handlelength=3,fontsize=L+5)
          first_legend.set_title('Runs:',prop={'weight': 'bold','size':L+5})
          for line in first_legend.legendHandles:
             line.set_linewidth(8.0)
          axa = plt.gca().add_artist(first_legend)
          second_legend = fig.legend(handles2[0:2],labels2[0:2],loc='upper center',fancybox=True,\
                                     bbox_to_anchor=(0.65, 0.07),ncol=7,handlelength=4.5,fontsize=L+5)
          second_legend.set_title('Demand per Run:',prop={'weight': 'bold','size':L+5})
          for line in second_legend.legendHandles:
             line.set_linewidth(8.0)
       elif run_settings().all_runs_combined == True and run_settings().inflow_and_outflow == True:
          handles, labels       = axis.get_legend_handles_labels()
          handles2,labels2 = handles[:],labels[:]
          observed_legend = fig.legend(handles[0:1],labels[0:1],loc='upper center',fancybox=True,\
                                    bbox_to_anchor=(0.35, 0.07),ncol=7,handlelength=3,fontsize=L+5)
          observed_legend.set_title('Observed Data:',prop={'weight': 'bold','size':L+5})
          first_legend = fig.legend(handles[1:4],labels[1:4],loc='upper center',fancybox=True,\
                                    bbox_to_anchor=(0.65, 0.07),ncol=7,handlelength=3,fontsize=L+5)
          first_legend.set_title('Runs:',prop={'weight': 'bold','size':L+5})
          for line in first_legend.legendHandles:
             line.set_linewidth(8.0)
          axa = plt.gca().add_artist(first_legend)
       #first_legend = fig.legend(loc='upper center',bbox_to_anchor=(0.5, -0.03))
       #plt.legend(labels, loc='left',fontsize=L,ncol=2)
       #axa = plt.gca().add_artist(first_legend)          
       #plt.tight_layout()
       sns.axes_style()
       if first_half == True:
          if self.outflow_on_off    == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"1half.jpg")
              plt.close()
          elif self.inflow_on_off   == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"1half.jpg")
              plt.close()
          elif self.storage_on_off  == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"1half.jpg")
              plt.close()
          elif run_settings().inflow_and_outflow == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"1half.jpg")
              plt.close()
       elif second_half == True:
          if self.outflow_on_off    == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"2half.jpg")
              plt.close()
          elif self.inflow_on_off   == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"2half.jpg")
              plt.close()
          elif self.storage_on_off  == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"2half.jpg")
              plt.close()
          elif self.inflow_and_outflow == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"2half.jpg")
              plt.close()    
            
   def graphs_statistics(self,time,kge,pearson_r,NRMSE,res_name,run_name):
          #bins = np.linspace(-5, 5, 100)
          n         = len(res_name)
          fig,ax    = plt.subplots(figsize=(5,n//5),dpi=150)
          ind       = np.arange(n)
          width     = 0.3
          ax.set_axisbelow(True)
          ax.grid(alpha=0.6)
          ax.barh(ind,kge,width,color='red',alpha=1.0,label='KGE')
          ax.barh(ind+width,pearson_r,width,color='black',alpha=1.0,label='R')
          ax.barh(ind+width+width,NRMSE,width,color='grey',alpha=1.0,label='NRMSE')
          ax.set(yticks=ind + width, yticklabels=res_name, ylim=[2*width - 1, len(kge)],\
                 xticklabels =['-1.0','-0.75','-0.5','-0.25','0','0.25','0.5','0.75','1.0'])
          plt.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1),ncol=3,fancybox=True)
          plt.tight_layout()
          plt.xlim(-1,1)
          plt.xticks(np.arange(-1.0,1.25,step=0.25))
          
          if self.outflow_on_off    == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"statistics.jpg")
              plt.close()
          elif self.inflow_on_off   == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"statistics.jpg")
              plt.close()
          elif self.storage_on_off  == True:
              ### Directory Input
              plt.savefig(r'''Directory Input'''+run_name+"/"+str(time)+"statistics.jpg")
              plt.close()
          
   def flow_duration(self,interpout1,interpout2,interpout3,interpout4,observed,res_name,inflowobserved):
          sns.set(font_scale=2)
          n = 40
          L = n//1.6
          n_color = 4
          LW = 3.0
          ccc = cm.winter(np.linspace(0.0,1.0,n_color))
          ccc2 = cm.spring(np.linspace(0.0,1.0,n_color))
          ccc3 = cm.cool(np.linspace(0.0,1.0,n_color))
          ccobserved = cm.autumn(np.linspace(0.0,1.0,4))
          
          fig, axes     = plt.subplots(nrows=5,ncols=4,figsize = (n,L),sharex=True,dpi=150)
          fig.subplots_adjust(top=0.98,left=0.05,right=0.95,bottom=0.10)
          first_half = run_settings().first_half
          second_half = run_settings().second_half
          if first_half == True:
             xrange=range(1,21)
             res_name = self.res_name[0:20]
             print(interpout1)
          elif second_half == True:
             xrange=range(1,21)
             res_name = self.res_name[20:40]
             print(interpout1)
          Q90x = [10,10]
          Q90y = [0,10000]
          Q50x = [50,50]
          Q50y = [0,10000]
          Q05x = [95,95]
          Q05y = [0,10000]
          for ch,na,ty in zip(xrange,res_name,self.reservoir_type):
                 axis   = axes.flatten()[ch-1]
                 if second_half == True:
                    axis.plot(Q90x,Q90y,color='grey',linewidth=LW,label='Low')
                    axis.plot(Q50x,Q50y,color='grey',linestyle='--',linewidth=LW,label='Median')
                    axis.plot(Q05x,Q05y,color='grey',linestyle=':',linewidth=LW,label='High')
                    
                    length_ = range(0,len(observed[ch+20]))
                    axis.plot(length_,inflowobserved[ch+20],color='blue',label='Outflow',linewidth=LW)
                    length_ = range(0,len(inflowobserved[ch+20]+1))
                    axis.plot(length_,inflowobserved[ch+20],color='blue',linestyle='--',label='Inflow',linewidth=LW)
                    length_ = range(0,len(interpout1[ch+20]))
                    axis.plot(length_,interpout1[ch+20],color='red',label='1',linewidth=LW)
                    length_ = range(0,len(interpout2[ch+20]))
                    axis.plot(length_,interpout2[ch+20],color='fuchsia',label='2',linewidth=LW)
                    length_ = range(0,len(interpout3[ch+20]))
                    axis.plot(length_,interpout3[ch+20],color='yellow',label='3',linewidth=LW)
                    length_ = range(0,len(interpout4[ch+20]))
                    axis.plot(length_,interpout4[ch+20],color='green',linestyle='--',label='4',linewidth=LW)                  
                     

                    based_on = observed[ch+20]
                    #plt.ylim(0)
                    name   = na
                    print(na)
                    #axis.set_ylim(0)
                    #axis.set_yscale('symlog')
                    '''
                    if name == 'Oroville' or name == 'Sirikit':
                       axis.set_yticks([5,10,20,50,100,500,1000,2000,5000])
                       axis.set_ylim(5,5000)
                    elif name == 'Oahe':
                       axis.set_yticks([200,500,1000,2000,5000])
                       axis.set_ylim(200,5000)
                    elif name == 'Kayrakkum'or name == 'Grand Coulee' or name=='Nurek':
                       axis.set_yticks([200,500,1000,2000,5000])
                       axis.set_ylim(100,5000)
                    elif name == 'Sirikit':
                       axis.set_yticks([10,100,500,1000,2000,5000])
                       axis.set_ylim(10,5000)
                    elif name == 'Oldman River Dam':
                       axis.set_yticks([1,5,10,20,50,100,300])
                       axis.set_ylim(1,500)
                    elif name == 'Powell':
                       axis.set_yticks([20,50,100,500,1000,2000])
                       axis.set_ylim(20,2000)
                    elif name == 'McPhee' or name == 'Rafferty' or name == 'Ross' or name == 'Seminoe' or name == 'Ririe':
                       axis.set_yticks([1,10,50,100,500,1000])
                       axis.set_ylim(1,1000)
                    elif name == 'Lake Helena' :
                       axis.set_yticks([10,50,100,500,1000])
                       axis.set_ylim(10,1000)
                    elif name == 'Split Rock Dam':
                       axis.set_yticks([0,1,5,10])
                       axis.set_ylim(-1,10)
                    elif name =='Tuyen Quang':
                       axis.set_yticks([10,50,100,500,1000,2000])
                       axis.set_ylim(10,2000)
                    elif name == 'Lake Kemp Dam' or name == 'Waterton':
                       axis.set_yticks([0,1,5,10,50,100])
                       axis.set_ylim(0,100)
                    elif name == 'Red Fleet'  or name == 'St Mary':
                       axis.set_yticks([0,1,5,10,20,50,100,300])
                       axis.set_ylim(0,300)
                    '''
                    axis.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())
                    axis.set_title(label=name,fontsize=L+5,fontweight='bold')
                    axis.set_xticklabels([100,80,60,40,20,0])
                    axis.set_xlim(0,100)
                    if ch > 16:
                       axis.set_xlabel('Confidence Coefficient (%)',fontsize=L,fontweight='bold')
                    axis.set_ylim(0,100)
                    axis.set_ylabel('% Qmax',fontsize=L,fontweight='bold')
                    
                 elif first_half == True:
                    axis.plot(Q90x,Q90y,color='grey',linewidth=LW,label='Low')
                    axis.plot(Q50x,Q50y,color='grey',linestyle='--',linewidth=LW,label='Median')
                    axis.plot(Q05x,Q05y,color='grey',linestyle=':',linewidth=LW,label='High')
                    
                    length_ = range(0,len(observed[ch]))
                    axis.plot(length_,observed[ch],color='blue',label='Outflow',linewidth=LW)
                    length_ = range(0,len(inflowobserved[ch]+1))
                    axis.plot(length_,inflowobserved[ch],color='blue',linestyle='--',label='Inflow',linewidth=LW)
                    length_ = range(0,len(interpout1[ch]))
                    axis.plot(length_,interpout1[ch],color='red',label='1',linewidth=LW)
                    length_ = range(0,len(interpout2[ch]))
                    axis.plot(length_,interpout2[ch],color='fuchsia',label='2',linewidth=LW)
                    length_ = range(0,len(interpout3[ch]))
                    axis.plot(length_,interpout3[ch],color='yellow',label='3',linewidth=LW)
                    length_ = range(0,len(interpout4[ch]))
                    axis.plot(length_,interpout4[ch],color='green',linestyle='--',label='4',linewidth=LW)                  
                     

                    based_on = observed[ch]
                    #plt.ylim(0)
                    name   = na
                    #axis.set_ylim(0)
                    #axis.set_yscale('symlog')
                    '''
                    if name == 'Albeni Falls':
                       axis.set_yticks([50,100,500,1000,3000])
                       axis.set_ylim(50,3000)
                    elif name == 'American Falls' or name == 'International Amistad Dam' or name == 'International Falcon Lake Dam':
                       axis.set_yticks([10,50,100,500,1000])
                       axis.set_ylim(10,1000)
                    elif name == 'Bhumibol' or name == 'Charvak' or name == 'Keystone Lake':
                       axis.set_yticks([5,10,20,50,100,250,500,1000,2000,5000])
                       axis.set_ylim(5,5000)
                    elif name == 'Big Sandy Dike' or name == 'Copeton':
                       axis.set_yticks([0,1,5,10,20,50])
                       axis.set_ylim(0,50)
                    elif name == 'Blue Mesa' or name == 'Buffalo Bill':
                       axis.set_yticks([1,5,10,20,50,100,250,500])
                       axis.set_ylim(1,500)
                    elif name == 'Chardara':
                       axis.set_yticks([5,10,20,50,100,300,500,1000,2000,5000,10000])
                       axis.set_ylim(5,10000)
                    elif name == 'Kayrakkum'or name == 'Grand Coulee':
                       axis.set_yticks([200,500,1000,2000,5000,7500])
                       axis.set_ylim(200,7500)
                    elif name == 'Fall River Lake' or name == 'Joes Valley':
                       axis.set_yticks([0,1,5,10,20,50,100])
                       axis.set_ylim(0,100)
                    elif name == 'Flaming Gorge'  or name == 'Ghost':
                       axis.set_yticks([10,20,50,100,200,300,500])
                       axis.set_ylim(10,500)
                    elif name == 'Fort Peck Dam':
                       axis.set_yticks([50,100,200,300,500,1000,2000])
                       axis.set_ylim(50,2000)
                    elif name == 'Garrison': 
                       axis.set_yticks([100,200,300,500,1000,2000,3000])
                       axis.set_ylim(100,3000)
                    '''   
                    axis.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())
                    axis.set_title(label=name,fontsize=L+5,fontweight='bold')
                    axis.set_xticklabels([100,80,60,40,20,0])
                    axis.set_xlim(0,100)
                    axis.set_ylabel('% Qmax',fontsize=L,fontweight='bold')
                    if ch > 16:
                       axis.set_xlabel('Confidence Coefficient (%)',fontsize=L,fontweight='bold')
                    axis.set_ylim(0,100)


          #plt.subplots_adjust(bottom=0.1,right=0.9,left=0.1,top=0.92)
          L = L+5
          #fig.text(0.02, 0.5, 'Discharge [cms]', va='center', rotation='vertical',fontsize=L,fontweight='bold')
          handles, labels       = axis.get_legend_handles_labels()
          handles2,labels2 = handles[:],labels[:]
          Q_legend = fig.legend(handles[0:3],labels[0:3],loc='upper center',fancybox=True,\
                              bbox_to_anchor=(0.5, 0.07),ncol=7,handlelength=3,fontsize=L)
          Q_legend.set_title('Q:',prop={'weight': 'bold','size':L})
          for line in Q_legend.legendHandles:
               line.set_linewidth(5.0)
               
          observed_legend = fig.legend(handles[3:5],labels[3:5],loc='upper center',fancybox=True,\
                              bbox_to_anchor=(0.2, 0.07),ncol=7,handlelength=3,fontsize=L)
          observed_legend.set_title('Observed Data:',prop={'weight': 'bold','size':L})
          for line in observed_legend.legendHandles:
               line.set_linewidth(5.0)
          first_legend = fig.legend(handles[5:9],labels[5:9],loc='upper center',fancybox=True,\
                              bbox_to_anchor=(0.8, 0.07),ncol=7,handlelength=3,fontsize=L)
          first_legend.set_title('Runs:',prop={'weight': 'bold','size':L})
          for line in first_legend.legendHandles:
               line.set_linewidth(5.0)
          axa = plt.gca().add_artist(first_legend)
          if first_half == True:
             ### Directory Input
             plt.savefig(r'''Directory Input''')
          elif second_half == True:
             ### Directory Input
             plt.savefig(r'''Directory Input''')
          plt.close()
          
   def individual_res_plots(self):
       if run_settings().ind_plot_on_off == True:
          
          run_name = run_settings().run_name
          res_name = variables().res_name
          
          outflow_on_off = True
          fs = 20
          L = fs
          n_color = 4
          ccc = cm.winter(np.linspace(0.0,1.0,n_color))
          ccc2 = cm.spring(np.linspace(0.0,1.0,n_color))
          ccc3 = cm.cool(np.linspace(0.0,1.0,n_color))
          
          if outflow_on_off == True:
              
             for r in res_name:
                  sns.set(font_scale=2)
                  fig,ax     = plt.subplots(figsize = (15,6.5),sharex=True,dpi=150)
                  fig.subplots_adjust(top=0.95,left=0.1,right=0.95,bottom=0.30)
                  print('Individual Plot ',r)
                  dataoutobs = functions.outflow_observed(r)
                  time_variable = ['Year','Month']
                  dataoutobs = functions.pandas_groupby(dataoutobs,time_variable,'OUT_OBS')
          
                  res_name_mod1 = r + 'run1'
                  res_name_mod2 = r + 'run2'
                  res_name_mod3 = r + 'run3'
                  res_name_mod4 = r + 'run4'
                  
                  ### Directory Input
                  load_location_inc = '''Directory Input'''
                  dataoutinc1 = functions.modelled_csv(res_name_mod1,load_location_inc)
                  dataoutinc1 = functions.pandas_groupby(dataoutinc1,time_variable,'OUT')

                  ### Directory Input
                  load_location_inc = '''Directory Input'''
                  dataoutinc2 = functions.modelled_csv(res_name_mod3,load_location_inc)
                  dataoutinc2 = functions.pandas_groupby(dataoutinc2,time_variable,'OUT')

                  ### Directory Input
                  load_location_inc = '''Directory Input'''
                  dataoutinc3 = functions.modelled_csv(res_name_mod4,load_location_inc)
                  dataoutinc3 = functions.pandas_groupby(dataoutinc3,time_variable,'OUT')

                  dataoutinc4 = functions.modelled_csv(res_name_mod2,load_location_inc)
                  dataoutinc4 = functions.pandas_groupby(dataoutinc4,time_variable,'OUT')
                  
                  if run_name == 'run3' or run_name == 'run4':
                      ### Directory Input
                      load_location_demand3 = '''Directory Input'''
                      demand3 = functions.modelled_csv(res_name_mod3,load_location_demand3)
                      demand3 = functions.pandas_groupby(demand3,time_variable,'OUT')

                      ### Directory Input
                      load_location_demand4 = '''Directory Input'''
                      demand4 = functions.modelled_csv(res_name_mod4,load_location_demand4)
                      demand4 = functions.pandas_groupby(demand4,time_variable,'OUT')
                      
                  if run_name == 'run1':
                      dataoutobs['OUT_OBS'].plot(ax=ax,color='blue',fontsize=fs,label='Natural Q Obs.')
                      dataoutinc1['OUT'].plot(ax=ax,color='red',fontsize=fs,label='Natural Q Mod. run1')
                      dataoutinc2['OUT'].plot(ax=ax,color='red',linestyle='--',fontsize=fs,label='Q Mod. run2')
                  else: 
                      dataoutobs['OUT_OBS'].plot(ax=ax,color='blue',fontsize=fs,label='Observed')
                      dataoutinc1['OUT'].plot(ax=ax,color='red',fontsize=fs,label='1')
                      dataoutinc4['OUT'].plot(ax=ax,color='fuchsia',fontsize=fs,label='2')
                      dataoutinc2['OUT'].plot(ax=ax,color='yellow',fontsize=fs,label='3')
                      dataoutinc3['OUT'].plot(ax=ax,color='green',linestyle='--',fontsize=fs,label='4')
                      
                  if run_name == 'run3' or run_name == 'run4':
                     if outflow_on_off == True:
                         demand3['OUT'].plot(ax=ax,color='black',fontsize=fs,label='3',alpha=0.6)
                         demand4['OUT'].plot(ax=ax,color='black',linestyle='--',fontsize=fs,label='4',alpha=0.6)

                  handles, labels       = ax.get_legend_handles_labels()
                  handles2,labels2 = handles[:],labels[:]
                  observed_legend = fig.legend(handles[0:1],labels[0:1],loc='upper center',fancybox=True,\
                                       bbox_to_anchor=(0.2, 0.15),ncol=7,handlelength=3,fontsize=L-5)
                  observed_legend.set_title('Observed Data:',prop={'weight': 'bold','size':L-5})
                  first_legend = fig.legend(handles[1:5],labels[1:5],loc='upper center',fancybox=True,\
                                       bbox_to_anchor=(0.5, 0.15),ncol=7,handlelength=3,fontsize=L-5)
                  first_legend.set_title('Runs:',prop={'weight': 'bold','size':L-5})
                  for line in first_legend.legendHandles:
                      line.set_linewidth(5.0)
                  axa = plt.gca().add_artist(first_legend)
                  second_legend = fig.legend(handles2[5:7],labels2[5:7],loc='upper center',fancybox=True,\
                                              bbox_to_anchor=(0.8, 0.15),ncol=7,handlelength=4.5,fontsize=L-5)
                  second_legend.set_title('Demand per Run:',prop={'weight': 'bold','size':L-5})
                  for line in second_legend.legendHandles:
                     line.set_linewidth(5.0)
               
                  ax.set_title(label=r,fontsize=fs)
                  ax.set_xticks(np.arange(0,500,120))
                  ax.set_xticklabels([1980,1990,2000,2010])
                  ax.set_xlim(0,372)
                  ax.set_xlabel('Time [Year]',fontsize=fs)
                  ax.set_ylabel('Discharge & Demand [cumsec]',fontsize=fs)
                  #plt.tight_layout(pad=1)
                  
                  ### Directory Input
                  plt.savefig(r'''Directory Input'''+r+run_name+".jpg")
                  plt.close()
        
   def plot_ratio_outflow_demand():
        ### Read CSV, give Directory
        df = pd.read_csv(r'''Directory Input''',delimiter=';')
        name = df['Name']
        ratio = df['c']
        unmet_demand = df['Delta']
        unmet_demand4 = df['Unmet Demand run4']
        fig,ax = plt.subplots(1,1,figsize =(5,5),dpi=150)
        plt.scatter(unmet_demand,ratio,color='red')
        xline=[-400,400]
        yline=[1,1]
        plt.plot(xline,yline,color='black')
        #plt.scatter(unmet_demand4,ratio)
        z = np.polyfit(unmet_demand, ratio,1)
        p = np.poly1d(z)
        z4 = np.polyfit(unmet_demand4, ratio,1)
        p4 = np.poly1d(z4)
        #plt.plot(range(-400,440,40),np.mean(ratio))
        #plt.plot(unmet_demand,p(unmet_demand),"r--")
        #plt.plot(unmet_demand4,p4(unmet_demand4),"r--")
        plt.axis([-400, 400, -1, 10])
        plt.yticks(np.arange(-1, 11, step=1))
        plt.xlabel('Unmet Demand [months]')
        plt.ylabel('c')
        plt.title('')
        #plt.ylim(372,100)
        plt.show()
        ### Directory Input
        #plt.savefig('''Directory Input''')
