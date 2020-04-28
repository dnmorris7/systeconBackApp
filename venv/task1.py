print("Task 1 - This is fun")
import pandas
from datetime import datetime
maintenenceDataDest = "C:\\Users\\David\\Desktop\\DevOps2019\\systecon2020\\backend\\Back-End Task Data\\MaintenanceData\\maintenance_data.csv"
headers=['Item','System','Failure Observation','Repair Time']
dtypes = [str, str, datetime, float]

df = pandas.read_csv(maintenenceDataDest, header=None, names=headers, dtype=dtypes)
print (df.head)

###I - Provide some high level metrics such as...
##1 - number of observations
df.count
##2 - minimum, maximum, and mean values
print("#a - Earliest Failure Observation - '1/1/1990'")
df['Failure observation'].min()

print("#b.1 - shortest repair time - 5.01")
df['Repair time'].min()
print("#b.2 - longest repair time - 230.0")
df['Repair time'].max()
print("#b.3 - average repair time - 230")
df['Repair time'].mean()


print("#c - Latest repair - '9/9/2014'")
df['Failure observation'].max()
#d - Longest repair time - 230.0
df['Repair time'].max()



print("#Min, Max, and Average Repair Time per System")
df2 = df[['System', 'Repair time']]
df2.groupby('System').min()
df2.groupby('System').max()
df2.groupby('System').mean()

print("#e - other stuff")
df.Item.unique()
df['Failure observation'].unique()
