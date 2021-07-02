import mysql.connector
import configparser
import os
from datetime import datetime
import time
import shutil

### ALL PARAMS IS GLOBAL ###
############################

#set date
now=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#get config
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config", "app.ini"))

#config params
hostname=config["server"]["hostname"]
username=config["server"]["username"]
password=config["server"]["password"]
excludes=config["database"]["exclude"]

#backup folder validity
validity_format_options = {"second":1,"minute":60,"day":86400,"week":604800,"month":2592000,"year":31536000}

#get from config
validity_format_config = str(config["validity"]["format"])
validity_value_config = int(config["validity"]["value"])

#build validity value as integer
if validity_format_config in validity_format_options:
    validity = validity_value_config * validity_format_options[validity_format_config]
else:
    #set default as "day"
    validity_format_config = "day"
    validity = validity_value_config * validity_format_options["day"]

#backup params
base_path = os.path.join(os.path.dirname(__file__), "backup")
backup_path = os.path.join(base_path, now)

#mysql connection
mysql_conn = mysql.connector.connect(host=hostname,username=username,password=password)

### END PARAMS ####
###################

#clean old folder
for f in os.listdir(base_path):
    #get full path
    f=os.path.join(base_path, f)
    #remove older than validity params
    if os.stat(f).st_mtime < time.time() - validity:
        if os.path.isdir(f):
            print("deleting folder older than " + str(validity_value_config) + " " + validity_format_config +  " : " + f + "...")
            shutil.rmtree(f)
            print("folder " + f + " has been deleted.\n")

#create folder by date
os.mkdir(backup_path)

#get databases
def getDatabases():
    #mysql cursor
    cur = mysql_conn.cursor()
    #query
    sql_query = cur.execute("SHOW DATABASES")
    #result
    results = cur.fetchall()

    #output
    output = []
    
    for result in results:
        dbname = "".join(result)
        if dbname not in excludes:
            output.append(dbname)
    
    #return dbs
    print("total databases to backup = " + str(len(output)) + "\n")
    return output

#backup db
def backupDatabases(databases):
    #run query
    for db in databases:
        cmd="mysqldump -h " + hostname + " -u " + username + " -p" + password + " " + db + " > " + backup_path + "/" + db + ".sql"
        print("backup database " + db + " in progress...")
        os.system(cmd)
        print("backup database " + db + " done.")
    print("\nall databases has been backup.")

##RUN SCRIPT##
all_databases = getDatabases()
backupDatabases(all_databases)
