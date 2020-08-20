import sys
### Directory Input
sys.path.append(r'''Directory Input''')

import numpy as np
import matplotlib.pyplot as plt
from variable_list import variables
from Döll import doll

class plots_D(): 

   def __init__(self):
       self.res_name    = variables().res_name
              
   def plot_döll(self,run_name,ILTA,ILF,ISA,ISR,ITS,IIV,name): 
       print('Start the plot of Döll results')
       bins     = np.linspace(-5, 5, 100)
       print(len(name))       
       n        = 40
       fig,ax   = plt.subplots(figsize=(5,n//5),dpi=150)
       ind      = np.arange(n)
       width    = 0.2
       
       ax.set_title('ILTA & ILF',loc='left')
       ax.set_axisbelow(True)
       ax.grid(alpha=0.6)
       ax.barh(ind,ILTA['Observed'],width,color='red',alpha=1.0,label='ILTA Observed')
       ax.barh(ind+width,ILTA['Modelled'],width,color='black',alpha=1.0,label='ILTA Modelled')
       ax.barh(ind+width+width,ILF['Q90_observed'],width,color='orange',alpha=1.0,label='ILF Observed')
       ax.barh(ind+width+width+width,ILF['Q90_modelled'],width,color='blue',alpha=1.0,label='ILF Modelled')
       ax.set(yticks=ind + width, yticklabels=self.res_name, ylim=[2*width - 1, len(ILTA)])
       plt.legend(loc='upper center',bbox_to_anchor=(0.35, -0.05),\
                  ncol=2,fancybox=True)
       plt.xlabel('%')
       plt.xlim(-100,100)
       ax.xaxis.set_label_coords(1.0, -0.025)
       #plt.xlim(-0.5,1.5)
       #plt.xticks(np.arange(-0.5,1.75,step=0.25))
       plt.tight_layout()

       ### Directory Input
       plt.savefig(r'''Directory Input'''+run_name+"/ILTA_ILF.png")
       plt.close()

       fig,ax   = plt.subplots(figsize=(5,n//5),dpi=150)
       ind      = np.arange(n)
       width    = 0.2
       
       ax.set_title('ISA',loc='left')
       ax.set_axisbelow(True)
       ax.grid(alpha=0.6)
       ax.barh(ind,ISA['Observed_MAX'],width,color='red',alpha=1.0,label='ISA Obs. Max.')
       ax.barh(ind+width,ISA['Observed_MIN'],width,color='black',alpha=1.0,label=' ISA Obs. Min.')
       ax.barh(ind+width+width,ISA['Modelled_MAX'],width,color='orange',alpha=1.0,label='ISA Mod. Max.')
       ax.barh(ind+width+width+width,ISA['Modelled_MIN'],width,color='blue',alpha=1.0,label='ISA Mod. Min.')
       ax.set(yticks=ind + width, yticklabels=self.res_name, ylim=[2*width - 1, len(ISA)])
       plt.legend(loc='upper center',bbox_to_anchor=(0.35, -0.05),\
                 ncol=2,fancybox=True)
       plt.xlabel('%')
       plt.xlim(-100,100)
       ax.xaxis.set_label_coords(1.0, -0.025)
       #plt.xlim(-0.5,1.5)
       #plt.xticks(np.arange(-0.5,1.75,step=0.25))
       plt.tight_layout()

       ### Directory Input
       plt.savefig(r'''Directory Input'''+run_name+"/ISA.png")
       plt.close()

       fig,ax   = plt.subplots(figsize=(5,n//5),dpi=150)
       ind      = np.arange(n)
       width    = 0.2
       
       ax.set_title('IIV & ITS',loc='left')
       ax.set_axisbelow(True)
       ax.grid(alpha=0.6)
       ax.barh(ind,IIV['Observed'],width,color='red',alpha=1.0,label='IIV Observed')
       ax.barh(ind+width,IIV['Modelled'],width,color='black',alpha=1.0,label='IIV Modelled')
       ax.barh(ind+width+width,ITS['Observed'],width,color='orange',alpha=1.0,label='ITS Observed')
       ax.barh(ind+3*width,ITS['Modelled'],width,color='blue',alpha=1.0,label='ITS Modelled')
       ax.set(yticks=ind + width, yticklabels=self.res_name, ylim=[2*width - 1, len(IIV)])
       plt.legend(loc='upper center',bbox_to_anchor=(0.35, -0.05),\
                  ncol=2,fancybox=True)
       plt.xlabel('N months')
       plt.xlim(-12,12)
       ax.xaxis.set_label_coords(1.0, -0.025)
       #plt.xlim(-0.5,1.5)
       #plt.xticks(np.arange(-0.5,1.75,step=0.25))
       plt.tight_layout()

       ### Directory Input
       plt.savefig(r'''Directory Input'''+run_name+"/IIV.png")
       plt.close()

       fig,ax   = plt.subplots(figsize=(5,n//5),dpi=150)
       ind      = np.arange(n)
       width    = 0.2
       ax.set_title('ISR',loc='left')
       ax.set_axisbelow(True)
       ax.grid(alpha=0.6)
       ax.barh(ind,ISR['Observed'],width,color='red',alpha=1.0,label='ISR Observed')
       ax.barh(ind+width,ISR['Modelled'],width,color='black',alpha=1.0,label=' ISR Modelled')
       ax.set(yticks=ind + width, yticklabels=self.res_name, ylim=[2*width - 1, len(IIV)])
       plt.legend(loc='upper center',bbox_to_anchor=(0.35, -0.05),\
                  ncol=2,fancybox=True)
       plt.xlim(0,100)
       plt.xlabel('%')
       ax.xaxis.set_label_coords(1.0, -0.025)
       #plt.xlim(-0.5,1.5)
       #plt.xticks(np.arange(-0.5,1.75,step=0.25))
       plt.tight_layout()

       ### Directory Input
       plt.savefig(r'''Directory Input'''+run_name+"/ITS_ISR.png")
       plt.close()
       
       
