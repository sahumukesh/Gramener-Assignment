
import pandas as pd
import math
import numpy
import scipy
import matplotlib.pyplot as plt
dataframe = pd.read_csv('nas-pupil-marks.csv')

#dataframe['total %']=dataframe['Maths %']+dataframe['Reading %']+dataframe['Social %']+dataframe['Social %']

'''
Considering maths as a subject. We need to ignore the missing data.
The factors that influence the marks of student in maths would be :
gender, age, category, sibling, handicap, father edu, mother edu,
father occu, mother occu, BPL, use calculator, use internet, use dictionary,
read other books, number of books read, distance,  computer use, library use,
like the school or not, give math HW, help in studies,
private tuition, Private tuition, Maths is difficult, Solve Maths, Solve Maths in groups,
Draw geometry, Explain answers, Watch TV, Play games, Help in household
'''

df=dataframe.rename(columns={'Maths %':'Maths'})
var = df.groupby("Father occupation").Maths.mean()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Father occupation')
ax1.set_ylabel('Maths')
ax1.set_title("Father occupation wise Maths marks")
var.plot(kind='bar')

count_1=0
marks_1=0.00
count_2=0
marks_2=0.00
count_3=0
marks_3=0.00
count_4=0
marks_4=0.00
count_5=0
marks_5=0.00
count_6=0
marks_6=0.00
count_7=0
marks_7=0.00
count_8=0
marks_8=0.00
count_9=0
marks_9=0.00


for i in range(0, len(dataframe)):
    if (math.isnan(dataframe.iloc[i]['Maths %']))==False:
        if dataframe.iloc[i]['Father occupation']==0:
            count_1=count_1+1
            marks_1=marks_1+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Father occupation']==1:
            count_2=count_2+1
            marks_2=marks_2+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Father occupation']==2:
            count_3=count_3+1
            marks_3=marks_3+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Father occupation']==3:
            count_4=count_4+1
            marks_4=marks_4+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Father occupation']==4:
            count_5=count_5+1
            marks_5=marks_5+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Father occupation']==5:
            count_6=count_6+1
            marks_6=marks_6+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Father occupation']==6:
            count_7=count_7+1
            marks_7=marks_7+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Father occupation']==7:
            count_8=count_8+1
            marks_8=marks_8+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Father occupation']==8:
            count_9=count_9+1
            marks_9=marks_9+dataframe.iloc[i]['Maths %']
        
maxx=max((marks_1/count_1),(marks_2/count_2),(marks_3/count_3),(marks_4/count_4),(marks_5/count_5),(marks_6/count_6),(marks_7/count_7),(marks_8/count_8),(marks_9/count_9))
minn=min((marks_1/count_1),(marks_2/count_2),(marks_3/count_3),(marks_4/count_4),(marks_5/count_5),(marks_6/count_6),(marks_7/count_7),(marks_8/count_8),(marks_9/count_9))

print 'Average Percentage of Maths marks of Father occupation 0 (Not Applicable)- ',((marks_1/count_1))
print 'Average Percentage of Maths marks of Father occupation 1 (Unemployed)- ',((marks_2/count_2))
print 'Average Percentage of Maths marks of Father occupation 2 (Labourer)- ',((marks_3/count_3))
print 'Average Percentage of Maths marks of Father occupation 3 (Farmer)- ',((marks_4/count_4))
print 'Average Percentage of Maths marks of Father occupation 4 (Clerk)- ',((marks_5/count_5))
print 'Average Percentage of Maths marks of Father occupation 5 (Skilled Worker)- ',((marks_6/count_6))
print 'Average Percentage of Maths marks of Father occupation 6 (Business)- ',((marks_7/count_7))
print 'Average Percentage of Maths marks of Father occupation 7 (Teacher/Lecturer)- ',((marks_8/count_8))
print 'Average Percentage of Maths marks of Father occupation 8 (Professional)- ',((marks_9/count_9))
print 'Difference between the maximum and the minimum value is - ',((maxx-minn))
