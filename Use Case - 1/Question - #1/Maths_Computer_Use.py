
import pandas as pd
import math
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


for i in range(0, len(dataframe)):
    if (math.isnan(dataframe.iloc[i]['Maths %']))==False:
        if dataframe.iloc[i]['Computer use']==1:
            count_1=count_1+1
            marks_1=marks_1+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Computer use']==2:
            count_2=count_2+1
            marks_2=marks_2+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Computer use']==3:
            count_3=count_3+1
            marks_3=marks_3+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Computer use']==4:
            count_4=count_4+1
            marks_4=marks_4+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Computer use']==5:
            count_5=count_5+1
            marks_5=marks_5+dataframe.iloc[i]['Maths %']
        


print 'Average Percentage of Maths Marks of Computer use 1 (No Computer)- ',((marks_1/count_1))
print 'Average Percentage of Maths Marks of Computer use 2 (Never use)- ',((marks_2/count_2))
print 'Average Percentage of Maths Marks of Computer use 3 (Once in Month)- ',((marks_3/count_3))
print 'Average Percentage of Maths Marks of Computer use 4 (Once in a Week)- ',((marks_4/count_4))
print 'Average Percentage of Maths Marks of Computer use 5 (Daily)- ',((marks_5/count_5))
