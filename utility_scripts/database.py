import sqlite3
from sqlite3 import Error
import os
import pyautogui
from datetime import datetime, timedelta

class Database:
    def __init__(self):

        self.conn = self.create_connection("C:\\Users\\gabri\\Desktop\\Code\\Projects\\Entry-Level-Job-Search\\db.sqlite3")

        if self.conn is None:
            print("Error -- no database connection found.")
            exit()

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Database connection successful!")
            return conn
        except Error as e:
            print(e) 
        return conn

    def insert(self, insertions):
        c = self.conn.cursor()

        # Loop through all records (entries), inserting each into the database
        for values, query in insertions.items():
            try:
                c.execute(query, values)
                print("Insertion successful!")
            except Error as e:
                print(e)
                return False
        self.conn.commit()
        return True

    def getUniqueID(self):
        ids = self.getJobIDs()

        # Get a free ID slot by checking against IDs in database
        idx = 1
        while True:
            if idx in ids:
                #print(f"ID {idx} already found in DB -- incrementing...")
                idx += 1
            else:
                return idx

    def getJobIDs(self):
        c = self.conn.cursor()
        try:
            id_col = c.execute("""SELECT id FROM job_search_job""").fetchall()
            ids = [idx[0] for idx in id_col]
            #print(ids)
            return ids
        except Error as e:
            print("Could not get database IDs: {}".format(e))
            return

    def getAllData(self):
        c = self.conn.cursor()
        try:
            data = c.execute("""SELECT * from job_search_job""").fetchall()
            return data
        except Error as e:
            print(e)

    def getTableColumnDescriptions(self):
        c = self.conn.cursor()
        try:
            data = c.execute("""SELECT * from job_search_job""")
            names = list(map(lambda x: x[0], data.description))
            return names
        except Error as e:
            print(e)