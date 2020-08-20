# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:32:01 2020

@author: Lars__000
"""
import pandas as pd
from plots import plots
from functions import functions
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm

def graphs_statistics():
          L = 0.5
          plt.rcParams['font.sans-serif'] = ['Calibri', 'sans-serif']
          plt.rcParams.update({'font.size': 14})
          
          ### ls reads the statistics that were given in a certain csv file.
          ### Therefore, it is necessary to give a certain csv-file input directory.
          ls = pd.read_csv(''' Directory Input ''',delimiter=';')
          ls = ls.sort_values('KGE_run4',ascending=True)
          setx = 'KGE_'
          n         = len(ls['Name'])
          fig,ax    = plt.subplots(figsize=(8,n//4),dpi=600)
          ind       = np.arange(n)
          width     = 0.2
          ax.set_axisbelow(True)
          ax.grid(alpha=0.6)
          n_color=4
          color=cm.coolwarm(np.linspace(0.0,1.0,n_color))

          line1 = ls.loc[(ls['KGE_run4'] >=0)]
          line2 = ls.loc[(ls['KGE_run4'] <=0)&(ls['KGE_run4'] >=-1)]
          line3 = ls.loc[(ls['KGE_run4'] <=-1)]
          if setx =='KGE_':
                 y1 = np.arange(-1,1.1,0.1)
                 x1 = np.empty(21)
                 x1.fill(27-width)
                 
                 ax.plot(y1,x1,'r--',color='black',linewidth=1.0)
                 
                 y2 = np.arange(-1,1.1,0.1)
                 x2 = np.empty(21)
                 x2.fill(13-width)
                 ax.plot(y2,x2,'r--',color='black',linewidth=1.0)

                 fig.text(0.96, 0.75, 'High', va='center',rotation=270)
                 fig.text(0.96, 0.50, 'Moderate', va='center',rotation=270)
                 fig.text(0.96, 0.24, 'Low', va='center',rotation=270)

          elif setx =='Alpha ':
                 y1 = np.arange(-1,4.1,0.1)
                 x1 = np.empty(len(y1))
                 x1.fill(27-width)
                 
                 ax.plot(y1,x1,'r--',color='black',linewidth=1.0)
                 
                 y2 = np.arange(-1,4.1,0.1)
                 x2 = np.empty(len(y1))
                 x2.fill(16-width)
                 ax.plot(y2,x2,'r--',color='black',linewidth=1.0)

                 fig.text(0.96, 0.81, 'High', va='center',rotation=270)
                 fig.text(0.96, 0.55, 'Moderate', va='center',rotation=270)
                 fig.text(0.96, 0.29, 'Low', va='center',rotation=270)

          elif setx =='Beta ':
                 y1 = np.arange(-1,4.1,0.1)
                 x1 = np.empty(len(y1))
                 x1.fill(27-width)
                 
                 ax.plot(y1,x1,'r--',color='black',linewidth=1.0)
                 
                 y2 = np.arange(-1,4.1,0.1)
                 x2 = np.empty(len(y1))
                 x2.fill(16-width)
                 ax.plot(y2,x2,'r--',color='black',linewidth=1.0)

                 fig.text(0.96, 0.81, 'High', va='center',rotation=270)
                 fig.text(0.96, 0.55, 'Moderate', va='center',rotation=270)
                 fig.text(0.96, 0.29, 'Low', va='center',rotation=270)
          elif setx =='R ':
                 y1 = np.arange(-1,4.1,0.1)
                 x1 = np.empty(len(y1))
                 x1.fill(27-width)
                 
                 ax.plot(y1,x1,'r--',color='black',linewidth=1.0)
                 
                 y2 = np.arange(-1,4.1,0.1)
                 x2 = np.empty(len(y1))
                 x2.fill(16-width)
                 ax.plot(y2,x2,'r--',color='black',linewidth=1.0)

                 fig.text(0.96, 0.81, 'High', va='center',rotation=270)
                 fig.text(0.96, 0.55, 'Moderate', va='center',rotation=270)
                 fig.text(0.96, 0.29, 'Low', va='center',rotation=270)
                 
          for c,i in zip(color,range(n_color)):                 
                 if i == 0:
                        ax.barh(ind,ls[setx+'run4'],width,color=c,label='4',edgecolor='black',linewidth=L)
                 elif i==1:
                        ax.barh(ind+width,ls[setx+'run3'],width,color=c,label='3',edgecolor='black',linewidth=L)
                 elif i==2:
                        ax.barh(ind+width+width,ls[setx+'run2'],width,color=c,label='2',edgecolor='black',linewidth=L)
                 elif i==3:
                        ax.barh(ind+width+width+width,ls[setx+'run1'],width,color=c,label='1',edgecolor='black',linewidth=L)
          if setx == 'KGE_' or setx == 'R ':
              ax.set(yticks=ind + width, yticklabels=ls['Name'], ylim=[2*width - 1, len(ls['Alpha run1'])],xticklabels =['<-1.0','-0.75','-0.5','-0.25','0','0.25','0.5','0.75','1.0'])
              plt.xticks(np.arange(-1.0,1.25,step=0.25))
              plt.xlim(-1,1)
              
              if setx == 'KGE_':
                  fig.text(0.2, 0.97, '(a)', va='center')
                  ax.set_title('KGE')
              elif setx == 'R ':
                  fig.text(0.2, 0.97, '(c)', va='center')
                  ax.set_title('R')
          elif setx == 'Alpha ' or setx == 'Beta ':
              ax.set(yticks=ind + width, yticklabels=ls['Name'], ylim=[2*width - 1, len(ls['Alpha run1'])],xticklabels =['0.0','0.5','1.0','1.5','2.0','2.5','3.0','3.5','>4.0'])
              plt.xticks(np.arange(0,4.5,step=0.5))
              plt.xlim(0,4)
              
              if setx == 'Alpha ':
                  fig.text(0.2, 0.97, '(b)', va='center')
              elif setx == 'Beta ':
                  fig.text(0.2, 0.97, '(d)', va='center')
              ax.set_title(setx)
          handles, labels = ax.get_legend_handles_labels()
          leg = ax.legend(handles[::-1],labels[::-1],loc='upper center',bbox_to_anchor=(0.5, -0.03),ncol=4,fancybox=True,title='Runs:',handletextpad=0.5)
          leg.set_title('Runs:',prop={'weight': 'heavy'})
          leg._legend_box.align = "left"
          plt.tight_layout()
          plt.savefig("additional_statistics/annual/"+setx+".jpg")
          plt.close()
graphs_statistics()

def individual_plot():
      fig,ax     = plt.subplots(figsize = (15,6.5),sharex=True,dpi=150)
      plt.rcParams['font.sans-serif'] = ['Calibri', 'sans-serif']
      plt.rcParams.update({'font.size': 20})
      r = 'Bhumibol'
      run_name = 'run1'
      fs=20
      outflow_on_off = True
      dataoutobs = functions.outflow_observed(r)
      time_variable = ['Year','Month']
      dataoutobs = functions.pandas_groupby(dataoutobs,time_variable,'OUT_OBS')
  
      res_name_mod1 = r + 'run1'
      res_name_mod3 = r + 'run3'
      res_name_mod4 = r + 'run4'

      ### Input of Directory essential
      load_location_inc = '''Directory'''
      dataoutinc1 = functions.modelled_csv(res_name_mod1,load_location_inc)
      dataoutinc1 = functions.pandas_groupby(dataoutinc1,time_variable,'OUT')

      ### Input of Directory essential
      res_name_mod2 = r + 'run2'
      load_location_inc = '''Directory'''
      dataoutinc2 = functions.modelled_csv(res_name_mod2,load_location_inc)
      dataoutinc2 = functions.pandas_groupby(dataoutinc2,time_variable,'OUT')
      
      if run_name == 'run3' or run_name == 'run4':
          ### Input of Directory essential (twice)
          load_location_demand3 = '''Directory'''
          demand3 = functions.modelled_csv(res_name_mod3,load_location_demand3)
          demand3 = functions.pandas_groupby(demand3,time_variable,'OUT')
          load_location_demand4 = '''Directory'''
          demand4 = functions.modelled_csv(res_name_mod4,load_location_demand4)
          demand4 = functions.pandas_groupby(demand4,time_variable,'OUT')
          
      if run_name == 'run1':
          dataoutinc1['OUT'].plot(ax=ax,color='red',fontsize=fs,label='Natural Run1')
          dataoutinc2['OUT'].plot(ax=ax,color='red',linestyle='--',fontsize=fs,label='Modified Run2')
          dataoutobs['OUT_OBS'].plot(ax=ax,color='blue',fontsize=fs,label='Observed.')
      else: 
          dataoutinc1['OUT'].plot(ax=ax,color='red',fontsize=fs,label='Modified Run3')
          dataoutinc2['OUT'].plot(ax=ax,color='red',linestyle='--',fontsize=fs,label='Modified Run4')
          
         
      if run_name == 'run3' or run_name == 'run4':
         if outflow_on_off == True:
             #ax2 = ax.twinx()
             demand3['OUT'].plot(ax=ax,color='black',fontsize=fs,label='Total Demand Run3',alpha=0.6)
             demand4['OUT'].plot(ax=ax,color='black',linestyle='--',fontsize=fs,label='Total Demand Run4',alpha=0.6)
             dataoutobs['OUT_OBS'].plot(ax=ax,color='blue',fontsize=fs,label='Observed')
             #axis2.set_ylabel('demand [cms]',fontsize=20)
             #ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
             #ax.set_ylabel('Demand [cumsec]',fontsize=fs)
      handles, labels       = ax.get_legend_handles_labels()
      #handles2, labels2     = ax2.get_legend_handles_labels()
      #plt.legend(handles+handles2,labels+labels2,loc='upper center', bbox_to_anchor=(0.5,-0.15),fontsize=fs,ncol=3,framealpha=0.0)  
      fig.text(0.075, 0.94, '(b)', va='center',fontsize = fs)
      plt.legend(handles,labels,loc='upper center', bbox_to_anchor=(0.5,-0.15),fontsize=fs,ncol=3,framealpha=0.0) 
      ax.set_title(label=r,fontsize=fs)
      ax.set_xticks(np.arange(0,500,120))
      ax.set_xticklabels([1980,1990,2000,2010])
      ax.set_xlim(0,372)
      ax.set_xlabel('Time [month]',fontsize=fs)
      ax.set_ylabel('Discharge & Demand [cumsec]',fontsize=fs)
      plt.tight_layout(pad=1)
      
      ### Input of save location acquired
      plt.savefig(r'''Save Location (Directory)'''+r+run_name+".jpg")
      plt.close()
individual_plot()

def graphs_statistics_within_multi():
          L = 0.5
          plt.rcParams['font.sans-serif'] = ['Calibri', 'sans-serif']
          plt.rcParams.update({'font.size': 14})

          ### Read CSV
          ### Directory Required
          ls = pd.read_csv('''Directory''',delimiter=';')
          ls = ls.sort_values('Within_Multi_Year',ascending=True)
          setx       = 'KGE_'
          n          = len(ls['Name'])
          fig, ax     = plt.subplots(figsize=(8,n//4),dpi=600)
          
          width      = 0.2
          #ax.set_axisbelow(True)
          ax.grid(alpha=0.6)
          
          line1 = ls.loc[(ls['Within_Multi_Year'] =='within')]
          line1 = line1.sort_values('KGE_run4',ascending=True)
          line2 = ls.loc[(ls['Within_Multi_Year'] =='multi')]
          line2 = line2.sort_values('KGE_run4',ascending=True)
          indini     = np.arange(n)
          ind        = np.arange(len(line1['Name']))
          ind2       = np.arange(len(line1['Name']),len(line1['Name'])+len(line2['Name']))

          if setx =='KGE_':
                 y1 = np.arange(-1,1.1,0.1)
                 x1 = np.empty(len(y1))
                 x1.fill(19-width)
                 
                 ax.plot(y1,x1,color='black',linewidth=1.0)
                 
                 #fig.text(0.976, 0.72, 'Multi-Year',weight='bold', va='center',rotation=270)
                 #fig.text(0.976, 0.31, 'Within-Year',weight='bold', va='center',rotation=270)

                 y2 = np.arange(-1,1.1,0.1)
                 x2 = np.empty(len(y2))
                 x2.fill(5-width)
                 
                 ax.plot(y2,x2,'r--',color='black',linewidth=1.0)
                 
                 fig.text(0.96, 0.45, 'High', va='center',rotation=270,fontsize=11)
                 fig.text(0.96, 0.31, 'Moderate', va='center',rotation=270,fontsize=11)
                 fig.text(0.96, 0.23, 'Low', va='center',rotation=270,fontsize=11)

                 y3 = np.arange(-1,1.1,0.1)
                 x3 = np.empty(len(y2))
                 x3.fill(9-width)
                 
                 ax.plot(y3,x3,'r--',color='black',linewidth=1.0)

                 y4 = np.arange(-1,1.1,0.1)
                 x4 = np.empty(len(y4))
                 x4.fill(30-width)
                 
                 ax.plot(y4,x4,'r--',color='black',linewidth=1.0)
                 
                 fig.text(0.96, 0.92, 'High', va='center',rotation=270,fontsize=11)
                 fig.text(0.96, 0.82, 'Moderate', va='center',rotation=270,fontsize=11)
                 fig.text(0.96, 0.64, 'Low', va='center',rotation=270,fontsize=11)

                 y5 = np.arange(-1,1.1,0.1)
                 x5 = np.empty(len(y5))
                 x5.fill(37-width)
                 
                 ax.plot(y5,x5,'r--',color='black',linewidth=1.0)
                 
          n_color    = 4
          color=cm.Wistia(np.linspace(0.0,1.0,n_color))
          color2=cm.summer(np.linspace(0.0,0.9,n_color))       
          for c,c2,i in zip(color,color2,range(n_color)):
                 if i == 0:
                        p1 = ax.barh(ind,line1[setx+'run4'],width,color=c,label='4',edgecolor='black',linewidth=L)
                        q1 = ax.barh(ind2,line2[setx+'run4'],width,color=c2,label='4',edgecolor='black',linewidth=L)
                 elif i==1:
                        p2 = ax.barh(ind+width,line1[setx+'run3'],width,color=c,label='3',edgecolor='black',linewidth=L)
                        q2 = ax.barh(ind2+width,line2[setx+'run3'],width,color=c2,label='3',edgecolor='black',linewidth=L)
                 elif i==2:
                        p3 = ax.barh(ind+width+width,line1[setx+'run2'],width,color=c,label='2',edgecolor='black',linewidth=L)
                        q3 = ax.barh(ind2+width+width,line2[setx+'run2'],width,color=c2,label='2',edgecolor='black',linewidth=L)
                 elif i==3:
                        p4 = ax.barh(ind+width+width+width,line1[setx+'run1'],width,color=c,label='1',edgecolor='black',linewidth=L)
                        q4 = ax.barh(ind2+width+width+width,line2[setx+'run1'],width,color=c2,label='1',edgecolor='black',linewidth=L)

          if setx == 'KGE_':
              ax.set(yticks=indini + width, yticklabels=pd.concat([line1['Name'],line2['Name']]),ylim=[width, len(ls)], xticklabels =['<-1.0','-0.75','-0.5','-0.25','0','0.25','0.5','0.75','1.0'])
              #ax.set(yticks=ind + width, yticklabels=line1['Name'], xticklabels =['<-1.0','-0.75','-0.5','-0.25','0','0.25','0.5','0.75','1.0'])
              plt.xticks(np.arange(-1.0,1.25,step=0.25))
              plt.xlim(-1,1)
              fig.text(0.2, 0.97, '(a)', va='center')
              ax.set_title('KGE per Run')
              
          handles1, labels1 = ax.get_legend_handles_labels()

          first_legend = plt.legend(handles=[p4,p3,p2,p1],loc='upper center',bbox_to_anchor=(0.7, -0.03))
          first_legend.set_title('Within Year',prop={'weight': 'heavy'})
          ax = plt.gca().add_artist(first_legend)
          second_legend = plt.legend(handles=[q4,q3,q2,q1],loc='upper center',bbox_to_anchor=(0.35, -0.03))
          second_legend.set_title('Multi Year',prop={'weight': 'heavy'})
          #ax2 = plt.gca().add_artist(second_legend)
          
          plt.tight_layout()
          plt.savefig("additional_statistics/"+setx+"within_prac.jpg")
          plt.close()
#graphs_statistics_within_multi()


def graphs_statistics_hydropower():
          L = 0.5
          plt.rcParams['font.sans-serif'] = ['Calibri', 'sans-serif']
          plt.rcParams.update({'font.size': 14})
          
          ### Read CSV
          ls = pd.read_csv('''Directory Input''',delimiter=';')
          ls = ls.sort_values('Within_Multi_Year',ascending=True)
          setx       = 'KGE_'
          n          = len(ls['Name'])
          fig, ax     = plt.subplots(figsize=(8,n//4),dpi=600)
          
          width      = 0.2
          ax.set_axisbelow(True)
          ax.grid(alpha=0.6)
          

          line1 = ls.loc[(ls['Main Purpose'] =='H')]
          line1 = line1.sort_values('KGE_run4',ascending=True)
          line2 = ls.loc[(ls['Secondary Hydropower'] =='H')]
          line2 = line2.sort_values('KGE_run4',ascending=True)
          line3 = ls.loc[(ls['Main Purpose'] !='H')&(ls['Secondary Hydropower'] !='H')]
          line3 = line3.sort_values('KGE_run4',ascending=True)
          indini     = np.arange(n)
          ind        = np.arange(len(line1['Name']))
          ind2       = np.arange(len(line1['Name']),len(line1['Name'])+len(line2['Name']))
          ind3       = np.arange(len(line1['Name'])+len(line2['Name']),\
                                                        len(line1['Name'])+len(line2['Name'])+len(line3['Name']))
          
          if setx =='KGE_':
                 y1 = np.arange(-1,1.1,0.1)
                 x1 = np.empty(len(y1))
                 x1.fill(12-width)
                 
                 ax.plot(y1,x1,color='black',linewidth=1.0)
                 
                 #fig.text(0.976, 0.72, 'Multi-Year',weight='bold', va='center',rotation=270)
                 #fig.text(0.976, 0.31, 'Within-Year',weight='bold', va='center',rotation=270)

                 y2 = np.arange(-1,1.1,0.1)
                 x2 = np.empty(len(y2))
                 x2.fill(29-width)
                 
                 ax.plot(y2,x2,color='black',linewidth=1.0)
                 
                 fig.text(0.965, 0.35, 'H', va='center',fontsize=11)
                 fig.text(0.965, 0.26, 'M', va='center',fontsize=11)
                 fig.text(0.965, 0.21, 'L', va='center',fontsize=11)
                 
                 fig.text(0.965, 0.71, 'H', va='center',fontsize=11)
                 fig.text(0.965, 0.65, 'M', va='center',fontsize=11)
                 fig.text(0.965, 0.51, 'L', va='center',fontsize=11)

                 fig.text(0.965, 0.91, 'H', va='center',fontsize=11)
                 fig.text(0.965, 0.84, 'M', va='center',fontsize=11)
                 fig.text(0.965, 0.77, 'L', va='center',fontsize=11)

                 y3 = np.arange(-1,1.1,0.1)
                 x3 = np.empty(len(y2))
                 x4 = np.empty(len(y2))
                 x3.fill(2-width)
                 x4.fill(6-width)
                 ax.plot(y3,x3,'r--',color='black',linewidth=1.0)
                 ax.plot(y3,x4,'r--',color='black',linewidth=1.0)
                 x5 = np.empty(len(y2))
                 x5.fill(23-width)
                 x6 = np.empty(len(y2))
                 x6.fill(26-width)
                 ax.plot(y3,x5,'r--',color='black',linewidth=1.0)
                 ax.plot(y3,x6,'r--',color='black',linewidth=1.0)
                 x7 = np.empty(len(y2))
                 x7.fill(32-width)
                 x8 = np.empty(len(y2))
                 x8.fill(36-width)
                 ax.plot(y3,x7,'r--',color='black',linewidth=1.0)
                 ax.plot(y3,x8,'r--',color='black',linewidth=1.0)
                 
          n_color    = 4
          color=cm.Wistia(np.linspace(0.0,1.0,n_color))
          color2=cm.summer(np.linspace(0.0,0.9,n_color))
          color3 = cm.winter(np.linspace(0.0,0.9,n_color))
          for c,c2,c3,i in zip(color,color2,color3,range(n_color)):
                 if i == 0:
                        p1 = ax.barh(ind,line1[setx+'run4'],width,color=c,label='4',edgecolor='black',linewidth=L)
                        q1 = ax.barh(ind2,line2[setx+'run4'],width,color=c2,label='4',edgecolor='black',linewidth=L)
                        r1 = ax.barh(ind3,line3[setx+'run4'],width,color=c3,label='4',edgecolor='black',linewidth=L)
                 elif i==1:
                        p2 = ax.barh(ind+width,line1[setx+'run3'],width,color=c,label='3',edgecolor='black',linewidth=L)
                        q2 = ax.barh(ind2+width,line2[setx+'run3'],width,color=c2,label='3',edgecolor='black',linewidth=L)
                        r2 = ax.barh(ind3+width,line3[setx+'run3'],width,color=c3,label='3',edgecolor='black',linewidth=L)
                 elif i==2:
                        p3 = ax.barh(ind+width+width,line1[setx+'run2'],width,color=c,label='2',edgecolor='black',linewidth=L)
                        q3 = ax.barh(ind2+width+width,line2[setx+'run2'],width,color=c2,label='2',edgecolor='black',linewidth=L)
                        r3 = ax.barh(ind3+width+width,line3[setx+'run2'],width,color=c3,label='2',edgecolor='black',linewidth=L)
                 elif i==3:
                        p4 = ax.barh(ind+width+width+width,line1[setx+'run1'],width,color=c,label='1',edgecolor='black',linewidth=L)
                        q4 = ax.barh(ind2+width+width+width,line2[setx+'run1'],width,color=c2,label='1',edgecolor='black',linewidth=L)
                        r4 = ax.barh(ind3+width+width+width,line3[setx+'run1'],width,color=c3,label='1',edgecolor='black',linewidth=L)

          if setx == 'KGE_' or setx == 'R ':
              ax.set(yticks=indini + width, yticklabels=pd.concat([line1['Name'],line2['Name'],line3['Name']]),ylim=[width, len(ls)], xticklabels =['<-1.0','-0.75','-0.5','-0.25','0','0.25','0.5','0.75','1.0'])
              #ax.set(yticks=ind + width, yticklabels=line1['Name'], xticklabels =['<-1.0','-0.75','-0.5','-0.25','0','0.25','0.5','0.75','1.0'])
              plt.xticks(np.arange(-1.0,1.25,step=0.25))
              plt.xlim(-1,1)
              fig.text(0.2, 0.97, '(b)', va='center')
              ax.set_title('KGE per Run')
              
          handles1, labels1 = ax.get_legend_handles_labels()
          #leg = ax.legend(handles1[::1],labels1[::1],loc='upper center',bbox_to_anchor=(0.5, -0.03),ncol=4,fancybox=True,title='Runs:',handletextpad=0.5)
          #leg.set_title('Runs (Hydropower = H, Sec. Hydropower = SH, Non-Hydropower = NH)',prop={'weight': 'heavy'})
          #leg._legend_box.align = "left"
          
          first_legend = plt.legend(handles=[p4,p3,p2,p1],loc='upper center',bbox_to_anchor=(0.8, -0.03))
          first_legend.set_title('Hydropower',prop={'weight': 'heavy'})
          ax = plt.gca().add_artist(first_legend)
          second_legend = plt.legend(handles=[q4,q3,q2,q1],loc='upper center',bbox_to_anchor=(0.45, -0.03))
          second_legend.set_title('Sec. Hydropower',prop={'weight': 'heavy'})
          ax2 = plt.gca().add_artist(second_legend)
          third_legend = plt.legend(handles=[r4,r3,r2,r1],loc='upper center',bbox_to_anchor=(0.1, -0.03))
          third_legend.set_title('Non-Hydropower',prop={'weight': 'heavy'})
          
          plt.tight_layout()
          plt.savefig("additional_statistics/"+setx+"within_hydro.jpg")
          plt.close()
#graphs_statistics_hydropower()
