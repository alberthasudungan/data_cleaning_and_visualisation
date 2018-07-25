#import the libraries 
import pandas
import numpy 
import seaborn

#reading the data
data= pandas.read_csv('[your csv survey data]', low_memory=False)

#Data management (deleting missing value)
polidata['W1_P15']=polidata['W1_P15'].replace (-1, numpy.nan)
polidata['W1_P15']=polidata['W1_P15'].astype('category')

#Reordering and modifying two of those variables (yes or no)
recode1={1:1,2:0}
polidata['W1_P15']=polidata['W1_P15'].map(recode1)

#reordering employment status to be in reverse order 
recode2={1:7,2:6,3:5,4:4,5:3,6:2,7:1}
polidata['PPWORK']=polidata['PPWORK'].map(recode2)

#creating uni variate graph for each variable, examining their central and spread [STEP 1] 
eaborn.countplot(x='W1_P15', data=polidata)
plt.xlabel ('invest or not')
plt.title ('Any stock investment/asset')

#visualising employment indicator
seaborn.countplot(x='PPWORK', data=polidata)
plt.xlabel ('Employment status')
plt.title ('Employment indicator')

#Performing descriptive statistics
runfile('your current python project file', wdir='your python pathway file')
