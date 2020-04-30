print("Task 1 - This is fun")
import pandas
from datetime import datetime
import numpy as np
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


###I - Provide some high level metrics such as...
##1 - number of observations
df.count
print(df.count)
##2a - minimum, maximum, and mean values
#a - Earliest Failure Observation - '1/1/1990'"
earliestObs = df['Failure observation'].min()
print("#a - Earliest Failure Observation - "+ earliestObs)
#b.1 - shortest repair time - 5.01"
print ('b - Shortest Repair time - '+str(df['Repair time'].min()))
print(df['Repair time'].min())
#b.2 - longest repair time - 230.0"

print("#b.2 - longest repair time - "+ str(df['Repair time'].max()))
#Mean
print("#b.3 - average repair time - "+ str(df['Repair time'].mean()))

#First Repair
print("#c - First repair - '")
print(df2['Failure observation'].min())
#Last Repair
print("#c - Latest repair - '")
print(df2['Failure observation'].max())
#d - Longest repair time - 230.0
df['Repair time'].max()



print("#Min, Max, and Average Repair Time per System")
df3System = df[['Item', 'System', 'Repair time']]
print("MINIMUM REPAIR PER SYSTEM")
print(df3System.groupby('System').min())
print("MAXIMUM REPAIR PER SYSTEM")
print(df3System.groupby('System').max())
print("AVERAGE REPAIR PER SYSTEM")
print(df3System.groupby('System').mean())

df3Item = df[['System','Item', 'Repair time']]
print("MINIMUM REPAIR PER COMPONENT")
print(df3Item.groupby('Item').min())
print("MAXIMUM REPAIR PER COMPONENT")
print(df3Item.groupby('Item').max())
print("AVERAGE REPAIR PER COMPONENT")
print(df3Item.groupby(['Item', 'System']).mean())



print("#e - other stuff")
print(df.Item.unique())
print(df['System'].unique())

##4 Generate Interarrival times##
print("#Generate Interarrival times for all systems")

#need to sort the calender first
#dateData = df2['Failure observation']
print(df2['Failure observation'].diff())
print("Average failure is : ")
print(df2['Failure observation'].diff().mean())

print("##Generate Interarrival times for each ###")
df4=df2[['System', 'Item', 'Failure observation']]
print(df4.head())
print(df4.groupby('System'))

print('Analysis: "Component 10 and 2 appear to be the lesser bottlenecks per system. Component 4 and 9 appear to be the primary bottlenecks per system. Each system itself falls within the same average parameters. With one system breaking everyday, and with it taking approximately three days to repair a system, investigation as to how to potentially '
      'phase out Component 10 and 2 should prove worthwhile."')

#dfSyst1 = df2.loc['System 01']


#5 Create a histogram
import matplotlib.pyplot as plt



itemFailTimeline = df2[['Item', 'Failure observation', 'Repair time']]
item4FailTimeline = itemFailTimeline.query('Item =="Component 4"')
fig = plt.plot_date(item4FailTimeline['Failure observation'], item4FailTimeline['Repair time'], color='red')
plt.ylabel("Hours to repair")
plt.title("Item 4 Failures")
plt.show()

item10FailTimeline = itemFailTimeline.query('Item =="Component 10"')
fig =plt.plot_date(item10FailTimeline['Failure observation'], item10FailTimeline['Repair time'], color='red')
plt.label("Hours to repair")
plt.title("Item 10 Failures")
print(item10FailTimeline)
plt.show()
#print(df4.groupby('System'))