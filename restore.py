import mysql.connector
import configparser
import os
import sys
import re

### ALL PARAMS IS GLOBAL ###
############################

# get config
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config", "app.ini"))

# config params
hostname=config["server"]["hostname"]
username=config["server"]["username"]
password=config["server"]["password"]
restore=config["restore"]["source"]

# backup folder
folder_path = os.path.join(os.path.dirname(__file__), restore)

# mysql connection
mysql_conn = mysql.connector.connect(host=hostname,username=username,password=password)

# check folder
if not os.path.isdir(folder_path):
    sys.exit("ERROR: folder " + folder_path + " not exist.")


# list .sql
for sqlfile in os.listdir(folder_path):
    dbcount = 0

    if re.match(".*\.sql", sqlfile):
        dbname = str(sqlfile).replace(".sql","")
        
        # mysql cursor
        cur = mysql_conn.cursor()

        # create db if not exist
        print("create database " + dbname + " if not exist")
        cur.execute("CREATE DATABASE IF NOT EXISTS " + dbname)

        # restore database
        cmd = "mysql -u " + username + " -p" + password + " " + dbname + " < " + folder_path + "/" + sqlfile
        print("restore database " + dbname + " in progress...")
        os.system(cmd)
        print("restore database " + dbname + " done.")
        
        dbcount += 1

    if dbcount > 0:
        print("\nall databases has been restored")