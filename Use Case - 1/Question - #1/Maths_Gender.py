import pandas as pd
import math
dataframe = pd.read_csv('nas-pupil-marks.csv')

#dataframe['total %']=dataframe['Maths %']+dataframe['Reading %']+dataframe['Science %']+dataframe['Social %']

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
count_male=0
marks_male=0.00
count_female=0
marks_female=0.00

for i in range(0, len(dataframe)):
    if (math.isnan(dataframe.iloc[i]['Maths %']))==False:
        if dataframe.iloc[i]['Gender']==1:
            count_male=count_male+1
            marks_male=marks_male+dataframe.iloc[i]['Maths %']
        if dataframe.iloc[i]['Gender']==2:
            count_female=count_female+1
            marks_female=marks_female+dataframe.iloc[i]['Maths %']



print 'Average Percentage of Social Marks of Gender-Male - ',((marks_male/count_male))
print 'Average Percentage of Social Marks of Gender-Female - ',((marks_female/count_female))
