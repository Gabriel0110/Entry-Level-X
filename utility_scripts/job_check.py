import pandas as pd
import csv
import os
from os import path
from datetime import datetime
from database import Database

filedir = "C:/Users/gabri/Desktop/Code/Projects/Entry-Level-Job-Search/"
filename = 'pending_job_approvals.csv'
db = Database()

def insert_job(title, company, city, state, desc):
    global db
    job_id = db.getUniqueID()
    job_url = "http://www.google.com" # HARDCODED FOR NOW -- CHANGE LATER

    insertions = {}
    query = """INSERT INTO job_search_job VALUES (?, ?, ?, ?, ?, ?, ?);"""
    values = (int(job_id), str(title), str(company), str(city), str(state), str(job_url), str(desc))
    insertions[values] = query

    result = db.insert(insertions)
    if not result:
        print("Error with submitting new job entry into the database.")
        return
    else:
        print("Job inserted successfully.")

def checkFile():
    if path.exists(filedir + filename):
        print("File found.")
        return True
    else:
        print("File not found... exiting.")
        return False

def getApprovedJobs():
    df = pd.read_csv(filedir + filename)
    mask = df['APPROVAL_STATUS'] == 1

    new_df = pd.DataFrame(df[mask])
    df_list = new_df.values.tolist()

    return df_list

def main():
    # First check if there is a file
    if checkFile() == False:
        exit()
    else:
        # Open CSV and get job rows for all jobs with APPROVAL_STATUS of 1
        jobs = getApprovedJobs()
        for job in jobs:
            title = job[1]
            company = job[2]
            city = job[3]
            state = job[4]
            desc = job[5]
            insert_job(title, company, city, state, desc)

if __name__ == "__main__":
    main()