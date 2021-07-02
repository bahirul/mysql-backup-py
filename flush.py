import os
import shutil

### ALL PARAMS IS GLOBAL ###
############################

#backup params
tmp_path = os.path.join(os.path.dirname(__file__), "backup")

### END PARAMS ####
###################

#clean old folder
for f in os.listdir(tmp_path):
    #get full path
    f=os.path.join(tmp_path, f)
    #remove all folder
    if os.path.isdir(f):
            shutil.rmtree(f)
        