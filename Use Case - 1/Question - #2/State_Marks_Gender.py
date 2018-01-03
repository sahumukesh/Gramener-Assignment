import pandas as pd
import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
dataframe = pd.read_csv('nas-pupil-marks.csv')

#dataframe['total %']=dataframe['Maths %']+dataframe['Reading %']+dataframe['Science %']+dataframe['Social %']

'''
Considering maths as a subject. We need to ignore the missing data.
Considering the maths marks from differnet states w.r.t the gender we
find the average of the marks w.r.t. each state!
'''
df=dataframe.rename(columns={'Maths %':'Maths'})
var = df['Maths'].groupby([df['State'],df['Gender']]).mean()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('State')
ax1.set_ylabel('Maths')
ax1.set_title("State wise marks based on Gender")
var.plot(kind='bar')

count_male=np.empty(33) # Count of students w.r.t states
count_male.fill(0)
marks_male=np.empty(33) # Maths marks of male w.r.t states
marks_male.fill(0.00)
count_female=np.empty(33) # Count of students w.r.t states
count_female.fill(0)
marks_female=np.empty(33) # Maths marks of female w.r.t states
marks_female.fill(0.00)
state=['AN','AP','AR','BR','CG','CH','DD','DL','DN','GA','GJ','HP','HR','JH','JK','KA','KL','MG','MH','MN','MP','MZ','NG','OR','PB','PY','RJ','SK','TN','TR','UK','UP','WB']

for i in range(0, len(dataframe)):
    if (math.isnan(dataframe.iloc[i]['Maths %']))==False:
            val=state.index(dataframe.iloc[i]['State'])#=='AN':
            if dataframe.iloc[i]['Gender']==1:
                count_male[val]=count_male[val]+1
                marks_male[val]=marks_male[val]+dataframe.iloc[i]['Maths %']
            if dataframe.iloc[i]['Gender']==2:
                count_female[val]=count_female[val]+1
                marks_female[val]=marks_female[val]+dataframe.iloc[i]['Maths %']

boys_outperform=0   #number of outperforming boys
girls_outperform=0 #number of outperforming girls
maxdiff=0.00 #maximum difference between the girls and boys marks across states
st=''

for i in range(0,len(state)):
    print 'Average Percentage of Maths marks of Gender-Male in ',state[i],'is - ',((marks_male[i]/count_male[i]))
    print 'Average Percentage of Maths marks of Gender-Female in ',state[i],'is - ',((marks_female[i]/count_female[i]))
    v1=(marks_male[i]/count_male[i])
    v2=(marks_female[i]/count_female[i])
    if abs(v2-v1)>maxdiff:
        maxdiff=abs(v2-v1)
        st=state[i]
    if  v1> v2:
        boys_outperform=boys_outperform+1
    else :
        girls_outperform=girls_outperform+1
    print '\n'

print 'Number of states where boys outperform ',boys_outperform
print 'Number of states where girls outperform ',girls_outperform    
print 'The maximum difference between the performance of girls and boys is - ',maxdiff,' which is in the state ',st