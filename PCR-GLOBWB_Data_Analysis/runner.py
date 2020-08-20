import sys
### Set Path --> Directory Input
sys.path.append(r'''Set Path''')
from _init_ import runner
from plots import plots
import time

start   = time.time()
run     = runner().nc_reader_runner()
end     = time.time()
print(end-start)


start   = time.time()
results = runner().results()
end     = time.time()
print(end-start) 

run_comparison = runner().analyis_run()      

start   = time.time()
doll    = runner().flow_duration()
end     = time.time()
print(end-start) 

start   = time.time()
doll    = runner().doll_process()
end     = time.time()
print(end-start) 

start   = time.time()
fdc     = plots().individual_res_plots()
end     = time.time()
print(end-start)
