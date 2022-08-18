#!/usr/bin/env python3
import pandas as pd
import os
class CSVReader:
    '''
    This class will pull all of the transactions from mint and export them as a 
    list of transaction objects (see transaction class)
    '''
    def __init__(self,baseDir=None,subDir=None):
        '''
        Will initialize and read all transactions in the sub directory
        Inputs:
            - baseDir: the base directory that holds all monthly transaction folders
            - subDir: the directory that we want to look at
        '''
        self.baseDir = baseDir
        self.subDir = subDir
    def readCSV(self):
        '''
        This method will read all of the CSVs in the sub directory and create a
        list of pandas dataframes
        output:
            -List of Pandas Dataframes containing the transaction data from
            the csv files
        '''
        completePath = os.path.join(self.baseDir,self.subDir)
        #Now we will cd into this directory
        os.chdir(completePath)
        #create a list to hold the data frames
        self.transactionFiles = []

        for file in os.listdir():
            #Now we will import the csv files
            self.transactionFiles.append(pd.read_csv(file))
        
        print(self.transactionFiles[0].head(10))
        return self.transactionFiles

if __name__ == '__main__':
    baseDir = '/Users/adish/Documents/Personal Finance/Expense Data'
    subDir = 'July2022'
    reader = CSVReader(baseDir=baseDir,subDir=subDir)
    reader.readCSV()
