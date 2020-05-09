print("Task 5 - Because why not?")
import pandas
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
maintenenceDataDest = "C:\\Users\\David\\Desktop\\DevOps2019\\systecon2020\\backend\\Back-End Task Data\\MaintenanceData\\maintenance_data.csv"
headers=['Item','System','Failure observation','Repair time']
dtypes = {'Item':'str','System':'str','Failure observation':'str','Repair time':'str'}
#dtypes = [str, str, datetime, float]


dateColumn = ['Failure observation']
df = pandas.read_csv(maintenenceDataDest, header=None, names=headers, dtype=dtypes)
df = df.iloc[1:]
#pandas.to_numeric(df['Repair time'], errors='coerce')
df['Repair time'] = df['Repair time'].astype(float)

print (df.head)

###Convert the Date Column into dates under a copy of the dataframe
df2= df.copy()
df2['Failure observation'] = [datetime.strptime(date, '%m/%d/%Y').date() for date in df2['Failure observation']]
print("Coverting to datetime... " )
print (df2.head)

##Do Components Grow Easier to Repair over time? Initial observations show little change?
itemFailTimeline = df2[['Item', 'Failure observation', 'Repair time']].sort_values(by='Failure observation', ascending=True)

####Let's do some clustering over the entire data set.
from scipy import stats
# ==LINEAR REGRESSION==
#x=(itemFailTimeline['Failure observation'] - itemFailTimeline['Failure observation'].iat[0]).days.reshape(-1,1)
#x =itemFailTimeline['Failure observation'].factorize()[0].reshape(-1,1)
allX =itemFailTimeline['Failure observation'].factorize()[0]
allY = itemFailTimeline['Repair time'].values
print(stats.linregress(allX,allY))
slope, intercept, rvalue, pvalue, stderr = stats.linregress(allX,allY)

#with these we can start making simple linear regression lines over time using the old formula y = mx + b
def fitLine(x):
    return slope * x + intercept

allFit = fitLine(allX)

fig = plt.plot_date(itemFailTimeline['Failure observation'], itemFailTimeline['Repair time'], color='red')

#plt.plot(slope, intercept, c='b')
plt.plot_date(itemFailTimeline['Failure observation'], allFit, c='b')
plt.ylabel("Hours to repair")
plt.title("Failures - All Items")
plt.show()
# Can we learn anything about these variances?


print("ITEM 1 DATASET")
item1FailTimeline = itemFailTimeline.query('Item =="Component 1"')
item1X = item1FailTimeline['Failure observation'].factorize()[0]
item1Y =  item1FailTimeline['Repair time'].values
slope, intercept, rvalue, pvalue, stderr = stats.linregress(item1X,item1Y)
item1Fit= fitLine(item1X)
plt.plot_date(item1FailTimeline['Failure observation'], item1Fit, c='g')

plt.show()