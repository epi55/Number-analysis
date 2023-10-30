# IMPORTS
import os
import csv
import pandas as pd
import numpy as np

# ENGINES
def runEngine():
    inputFolder = r"Number analysis\Inputs"
    outputFolder = r"Number analysis\Outputs"

    for filename in os.listdir(inputFolder):
        documentPath = os.path.join(inputFolder, filename)
        dfData = extractEngine(filename, documentPath)
        analysisEngine(dfData)

def extractEngine(filename, documentPath):
    df = pd.read_csv(documentPath)
    draw_cols = [col for col in df.columns if 'NUMBER DRAWN' in col]
    df = df.filter(items=['DRAW DATE'] + draw_cols)
    return df

def analysisEngine(dfData):
    dfDataMode = dfData.drop('DRAW DATE', axis=1)
    modeValues = dfDataMode.mode(axis=0)
    print(modeValues)

def outputEngine(allData, outputPath):
    outputPath = os.path.join(outputFolder, "output_data.xlsx")
    allData.to_excel(outputPath, sheet_name="Draw analysis", index=False)
    print("Data saved to:", outputPath)    

# RUN
runEngine()