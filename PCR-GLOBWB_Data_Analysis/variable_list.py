import sys
### Set Path --> Directory Input
sys.path.append(r'''Set Path''')
from run_settings import run_settings
class variables():
   def __init__(self):       
      self.res_name         = ['Albeni Falls','American Falls','Bhumibol','Big Sandy Dike','Blue Mesa',\
                               'Buffalo Bill','Chardara','Charvak','Copeton','Fall River Lake',\
                               'Flaming Gorge','Fort Peck Dam','Garrison','Ghost','Grand Coulee',\
                               'International Amistad Dam','International Falcon Lake Dam','Joes Valley','Kayrakkum','Keystone Lake',\
                               'Lake Helena','Lake Kemp Dam','McPhee','Nurek','Oldman River Dam',\
                               'Oahe','Oroville','Powell','Rafferty','Red Fleet',\
                               'Ririe','Ross','Seminoe','Sirikit','Split Rock Dam',\
                               'St Mary','Thief Valley','Travers','Tuyen Quang','Waterton']
      self.reservoir_type   = ['HF','IHR','IHWF','H','H',\
                               'HWI','HI','HI','IWH','F',\
                               'WHF','FHIR','FHIR','H','IF',\
                               'IH','IHWF','IF(H)','HI','HI',\
                               'I','FWH','IHW','IH','IH',\
                               'FHIR','FHIWR','HW','IFWR',\
                               'IWR','FIR','HFR','IHR','IHWF',\
                               'IW','I','I','I','H','I']

      self.storCap          = [1424.7,2062,13462,67.1,923.2,\
                               746.0,6700,2000,1364,316.3,\
                               4336.3,23560,30220,132,6395.6,\
                               6330.0,3920.0,67.7,4160.0,2063.1,\
                               60.5,1282.8,282.5,10500,490.0,\
                               29110.0,4366.5,1620.0,632.4,\
                               29.6,99.3,1791.9,1255,9510.0,\
                               372.0,394.7,21.5,317.0,2245.0,\
                               172.7]
      
      self.latitude         = [83,94,145,95,103,\
                               91,97,96,239,104,\
                               98,83,85,77,84,\
                               121,126,101,99,107,\
                               86,112,105,103,80,\
                               90,100,105,81,98,\
                               92,82,96,144,240,\
                               81,89,79,136,81]
      self.longitude        = [126,134,557,141,145,\
                               141,495,499,662,167,\
                               141,147,157,130,122,\
                               158,161,137,499,167,\
                               136,161,142,498,132,\
                               158,116,137,153,141,\
                               136,117,146,560,661,\
                               133,124,134,569,132]
          
      self.seconds_in_year  = 365*24*3600
      self.time_variable               = [['Month','Day'],['Year','Month'],['Month'],['Year','Day'],['Year']]
      self.name_variable_statistics    = ['Daily','Yearly Monthly','Monthly','Yearly Daily','Year']                 ### Assigns the name of the .csv file of the statistics
      self.xlabel_variable             = ['Month,Day','Year,Month','Month','Year,Day','Year']                       ### Assigns the x label
      self.map_name                    = ['Daily','Yearly_monthly','Monthly','Annual','Year']
      self.demand_run_name             = ['run3','run4']
      #if run_settings().storage_results == True:
         #self.run_name        =['run2','run3','run4']
        
      self.run_name        = ['run1','run2','run3','run4']
      
      self.infColObs = 'IN_OBS'                       
      self.infColMod = 'OUT'                       
      self.outColObs = 'OUT_OBS'
      self.outColMod = 'OUT'                     
      self.stoColObs = 'STOR_OBS'
      self.stoColMod = 'OUT'
      
      self.qp90         = 0.1
      self.qplist       = [0.99,0.95,0.9,0.85,0.8,0.7,0.6,0.5,0.4,0.5,0.2,0.1,0.05,0.01]
      self.qp_reversed  = [99,95,90,85,80,70,60,50,40,30,20,10,5,1]

      ### Directory Input (7x)
      self.save_location_demand3    = '''Directory Input'''
      self.save_location_demand4    = '''Directory Input'''
      self.save_irr_withdrawal_loc  = '''Directory Input'''
      self.save_ind_dom_liv_loc     = '''Directory Input'''
      self.save_total_demand        = '''Directory Input'''

      self.load_location_statistics = '''Directory Input'''

      self.inflow_location          = '''Directory Input'''
