import requests
from requests.exceptions import HTTPError
from database import Database
import pandas as pd
import csv
import os
from os import path
from datetime import datetime

filedir = "C:/Users/gabri/Desktop/Code/Projects/Entry-Level-Job-Search/"
filename = 'pending_job_approvals.csv'

def createFile():
    global filename, filedir

    columns = pd.DataFrame(columns=['JOB_TITLE', 'COMPANY', 'CITY', 'STATE', 'DESCRIPTION', 'URL', 'APPROVAL_STATUS', 'DATE', 'TIME'])
    columns.to_csv(filedir + filename)
    print("File created successfully.")

def checkFile():
    if path.exists(filedir + filename):
        pass
    else:
        print("File not found -- creating file...")
        createFile()

def insert_row(title, company, city, state, desc):
    job_url = "http://www.google.com" # HARDCODED FOR NOW -- CHANGE LATER

    global filename, filedir
    now = datetime.now()
    date = now.strftime("%m/%d/%Y")
    time = now.strftime("%H:%M:%S")

    data = {'JOB_TITLE':[title], 'COMPANY':[company], 'CITY':[city], 'STATE':[state], 'DESCRIPTION':[desc], 'URL':[job_url], 'APPROVAL_STATUS':['0'], 'DATE':[date], 'TIME':[time]}

    df = pd.DataFrame(data)

    try:
        df.to_csv(filedir + filename, mode='a', header=False)
        print("Row inserted successfully.")
    except Exception as e:
        print(e)

def main():
    pages = 50 # adjust as necessary

    banned = ['senior', 'sr', 'sr.', 'mid-level', 'staff', 'manager', 'lead', '3 years', 
    '4 years', '5 years', '6 years', '7 years', '8 years', '9 years', '10 years', '3+', '4+', 
    '5+', '6+', '7+', '8+', '9+', '10+', 'experienced', 'principal', '3+ years', '4+ years', 
    '5+ years', 'phd']
    # 'extensive' maybe... reaching a little?

    checkFile()

    for i in range(pages):
        try:
            response = requests.get(f'https://www.themuse.com/api/public/jobs?page={i+1}')
            response.raise_for_status()

            jsonResponse = response.json()
            
            for item in jsonResponse["results"]:
                contents = item["contents"].lower().split(' ')
                
                if any(term in item["contents"].lower() for term in banned) or any(term in item for item in contents for term in banned) or any(term in item["name"] for term in banned):
                    pass
                else:
                    job_title = item["name"]
                    company_name = item["company"]["name"]
                    job_location = item["locations"][0]["name"]
                    job_city = job_location.split(', ')[0]
                    job_state = job_location.split(', ')[1]
                    job_description = item["contents"]

                    insert_row(job_title, company_name, job_city, job_state, job_description)

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

if __name__=="__main__":
    main()