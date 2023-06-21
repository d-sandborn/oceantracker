#!/usr/bin/env python
# coding: utf-8

# # Output files
# 
# [This note-book is in oceantracker/tutorials_how_to/]
# 
# After running OceanTacker, output files are in the files are the folder given by parameters ./"root_output_dir"/"output_file_base"
# 
# The main files are:
# 
#    *   **users_params_*.json**, a copy of the parameters as supplied by the user, useful in debugging or re-running.
# 
#    *  **_runInfo.json** holds 
#       
#          * file names of case  files
# 
#          * information on computer used
#          
#          * code version, including git commit ID to enable rerunning with exactly the same version
#     
#    * **_caseInfo.json** files, have all the output files for each parallel case run (only 1 case in examples give so far), plus information about the run and data useful in plotting. Eg. 
# 
#       * full set of working parameters with defaults used
# 
#       * timings of parts of code
# 
#       * output_files, the names of all output files generated by the run separated by type.
# 
#       * information about the hindcast, eg start date, end date, time step, ...
#       
#       * basic information from each class used in the computational pipeline
# 
#    * **_caseLog_log.txt** has a copy of what appeared on the screen during the run 
# 
#    * **_tracks.nc** holds the particle tracks in a netcdf file, see below for code example on reading the tracks
# 
#    * **_grid_outline.json** are the boundaries of hydrodynamic model's domain and islands, useful in plotting
# 
#    * **_grid.nc** a netcdf of the hydo-model's grid and other information, useful in plotting and analysis
#    * **_events.nc** a netcdf output from events classes, which only writes output when events occur, eg. a particle entering or exiting given polygons.
#    
#    
# Time variables in these file are in seconds since 1970-01-01
#   
# Below list the files after running the minimal example. 
#     

# In[1]:


# show a list of output files after running  minimal_example
import glob
for f in glob.glob('output/minimal_example/*'):
    print(f) 



# ## Reading particle tracks

# In[ ]:


# example of reading tracks file


# In[ ]:





# 