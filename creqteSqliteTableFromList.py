
import sqlite3 
  
# conn = sqlite3.connect('pythonDB.db') 
# c = conn.cursor() 
  
def create_table(Database,ColumnsList,TableName,TypeList=[]): 
    conn = sqlite3.connect(Database) 
    c = conn.cursor() 

    if TypeList==[]:
        string=" ( id integer PRIMARY KEY,"
        for i in range(len(ColumnsList)):
            print(i)
            string=string+ColumnsList[i] +" TEXT, "
            print(string)
        string = string[:-2]
        string=string+")"

        c.execute('CREATE TABLE IF NOT EXISTS '+ TableName+string) 
        print('CREATE TABLE IF NOT EXISTS '+ TableName+string) 

    else:
        string=" ( id integer PRIMARY KEY,"
        for i in range(len(ColumnsList)):
            print(i)
            string=string+ColumnsList[i] +" "+ TypeList[i] +", "
            print(string)
        string = string[:-2]
        string=string+")"

        c.execute('CREATE TABLE IF NOT EXISTS '+ TableName+string) 
        print('CREATE TABLE IF NOT EXISTS '+ TableName+string) 







  
def data_entry(Database,TableName,ColumnsList,ValuesList): 
    conn = sqlite3.connect(Database) 
    c = conn.cursor() 

    # if Dictionary!={}:

    #     ColumnsList, ValuesList = zip(*Dictionary.items())


    if ColumnsList!=[]:
        string1=" ( "
        string2=" VALUES ( "
        for i in range(len(ColumnsList)):
            print(i)
            string1=string1+ColumnsList[i] +", "

            string2=string2+"'"+ValuesList[i]+"'"+", "
            print(string1)
            print(string2)
        string1 = string1[:-2]
        string1=string1+")"

        string2 = string2[:-2]
        string2=string2+")"

        commandMade="INSERT INTO "+TableName+string1+string2
        print(commandMade)
        c.execute(commandMade) 
        conn.commit() 

    
  
# create_table() 
# data_entry() 
  
# c.close() 
# conn.close() 





def CreateTableAndInsertValues(Database,TableName,TypeList ,ColumnsList=[],ValuesList=[],Dictionary={}):
    # conn = sqlite3.connect('pythonDB.db') 
    conn = sqlite3.connect(Database) 
    c = conn.cursor() 


    if Dictionary!={}:

        ColumnsList, ValuesList = zip(*Dictionary.items())


    create_table(Database=Database,ColumnsList=ColumnsList, TableName=TableName,TypeList=TypeList)
    data_entry(Database=Database,TableName=TableName,ColumnsList=ColumnsList, ValuesList=ValuesList)
    print("Done database write")
    c.close() 
    conn.close() 

    # print("Done database write")



TableName='Recordfive5'

ColumnsList=["Number", "Name", "JobName", "City", "State", "Country", "Address"]


TypeList=["text","text","text","text","text","text","text"]


ValuesList=["Value1","Value2","Value3","Value4","Value5","Value6","Value7"]

Database='pythonDB.db'


Dictionary={'name': 'Han Solo', 'firstname': 'Han', 'lastname': 'Solo', 'age': '37', 'score': '100', 'yrclass': '10'}


# CreateTableAndInsertValues(Database=Database,TableName=TableName,ColumnsList=ColumnsList,ValuesList=ValuesList,TypeList=TypeList)


CreateTableAndInsertValues(Dictionary=Dictionary ,Database=Database,TableName=TableName,TypeList=TypeList)
