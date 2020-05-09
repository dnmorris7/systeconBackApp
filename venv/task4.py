print("Task 4 say hiddy-ho...assuming your local instance of mySQL is up and running.")

import pandas as pd
from sqlalchemy import create_engine
import pymysql

dataInput="C:\\Users\\David\\Desktop\\DevOps2019\\systecon2020\\backend\\Back-End Task Data\\LsaParsing\\lsa_single_line.txt"
dataCSVOutput="C:\\Users\\David\\Desktop\\DevOps2019\\systecon2020\\backend\\Back-End Task Data\\LsaParsing\\output\\davidsingleLine.csv"
dataExcelOutput="C:\\Users\\David\\Desktop\\DevOps2019\\systecon2020\\backend\\Back-End Task Data\\LsaParsing\\output\\davidsingleExcelLine.xlsx"
dataSQLOutput="C:\\Users\\David\\Desktop\\DevOps2019\\systecon2020\\backend\\Back-End Task Data\\LsaParsing\\output\\davidsingleExcelLine.sql"


#define the headrow of the dataframe
headers=["pccn", "plisn", "cfi", "item_name","unit_price", "failure_rate", "next_higher_plisn", "qty_per_assembly"]
df = pd.DataFrame([headers])

try:
    f = open(dataInput)
    #Repeating ourselves doing this to skip the first line
    line=f.readline()
    line = f.readline()
    while line:
        #TODO need data validator. For now, just read from the second line
        #pccn = first six characters
        pccn = line[:6]
        #plisn = next 5 characters, starting from position 6 due to how python . Stripping it to remove white space.
        plisn = line[6:11].strip()
        #cfi should be at position 11 as a constant
        cfi=line[11]
        #item name is the next 12 characters, starting from character 12
        item_name=line[12:24].strip()
        #unit price will be next 8 characters.
        unit_price = line[24:32].strip()
        #failure rate is the next 8 characters
        failure_rate=line[32:40].strip()
        #next_higher_plisn is the next 5. Strip to remove whitespace
        next_higher_plisn = line[40:45].strip()
        #qty_per_assembly is the next 5. Strip to remove whitespace
        qty_per_assembly = line[45:50].strip()
        #now that I have my variables, I should insert them in order to my dataframe
        #first, define the row
        a_row=pccn,plisn,cfi,item_name,unit_price,failure_rate,next_higher_plisn,qty_per_assembly
    #dataframe the new row and concat
        row_df = pd.DataFrame([a_row])
        df = pd.concat([df, row_df], ignore_index=True)
        line = f.readline()

finally:
    print(df)

engineMySQL = create_engine('mysql+pymysql://root:abcd1234@localhost/systecontask', pool_recycle=3600)
df.to_sql('lsa_single_line', con=engineMySQL, if_exists='replace')
engineMySQL.execute("SELECT * FROM lsa_single_line").fetchall()
print(engineMySQL.execute("SELECT * FROM lsa_single_line").fetchall())