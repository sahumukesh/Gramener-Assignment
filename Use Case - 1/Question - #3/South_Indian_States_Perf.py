import pandas as pd
import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
dataframe = pd.read_csv('nas-pupil-marks.csv')

#dataframe['total %']=dataframe['Maths %']+dataframe['Reading %']+dataframe['Science %']+dataframe['Social %']

'''
Considering the south Indian states like 
Andaman and Nicobar
Andhra Pradesh
Karnataka
Kerala
Pondicherry and 
Tamil Nadu
we need to find the average of the south Indian states (not considering the missing values) 
and compare it with the performance
from all over India considering only maths and science marks of the students!
'''


count_math=0 #Count of students w.r.t states
marks_math=0.00 #maths marks w.r.t. states
count_sci=0 #Count of students w.r.t states
marks_sci=0.00 #science marks w.r.t. states
south=['AP','AN','KA','KL','PY','TN']
marks_south_math=0.00 #maths marks w.r.t. south indian states
count_south_math=0 #Count of students w.r.t. south indian states
marks_south_sci=0.00 #science marks w.r.t. south indian states
count_south_sci=0 #Count of students w.r.t. south indian states

state=['AN','AP','AR','BR','CG','CH','DD','DL','DN','GA','GJ','HP','HR','JH','JK','KA','KL','MG','MH','MN','MP','MZ','NG','OR','PB','PY','RJ','SK','TN','TR','UK','UP','WB']

for i in range(0, len(dataframe)):
    if (math.isnan(dataframe.iloc[i]['Maths %']))==False:
            val=state.index(dataframe.iloc[i]['State'])#=='AN':
            count_math=count_math+1
            marks_math=marks_math+dataframe.iloc[i]['Maths %']
            if dataframe.iloc[i]['State'] in south:
                marks_south_math=marks_south_math+dataframe.iloc[i]['Maths %']
                count_south_math=count_south_math+1
    if (math.isnan(dataframe.iloc[i]['Science %']))==False:
            val=state.index(dataframe.iloc[i]['State'])#=='AN':
            count_sci=count_sci+1
            marks_sci=marks_sci+dataframe.iloc[i]['Science %']
            if dataframe.iloc[i]['State'] in south:
                marks_south_sci=marks_south_sci+dataframe.iloc[i]['Science %']
                count_south_sci=count_south_sci+1
                

print 'National Average marks in maths is - ',((marks_math/count_math))
print 'National Average marks in science is - ',((marks_sci/count_sci))
print '\n'
print 'Average maths marks of south indian states - ',((marks_south_math/count_south_math))
print 'Average science marks of south indian states - ',((marks_south_sci/count_south_sci))
print '\n'
print 'Thus the south indian states perform poorer in both maths and science as compared to the national average'
