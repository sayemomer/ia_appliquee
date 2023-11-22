#import libraries to import data 

import pandas as pd


#import libraries to plot the data
import matplotlib.pyplot as plt

#load the crick_data
crick_data = pd.read_csv('../crick_data/Batting/t20.csv')

#print the first 5 rows of the crick_data
print(crick_data.head())

#print the batsman whose ave is greater than 40
print(crick_data[crick_data['Ave'] > '40'])

#plot the histogram of the runs
crick_data.hist(column='Runs', bins=50)
