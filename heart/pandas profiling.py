import pandas as pd 
from pandas_profiling import ProfileReport

df=pd.read_csv('heart.csv')

report=ProfileReport(df,title='pandas profiling')
report.to_file('heart.html')