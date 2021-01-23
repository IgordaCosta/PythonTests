import sqlite3
import os



def ChangeStartupDirectory(Folder):
        
        # curentWorkingDirectory = os.getcwd()
        # print(curentWorkingDirectory)
        # print("curentWorkingDirectory")
        
        home = os.path.expanduser('~')
        
        # print(home)
        
        location = os.path.join(home, 'Documents', Folder)
        
        # print(location)
        
        # folder_check = os.path.isdir(location)
        
        # print(folder_check)
        
        if not os.path.exists(location):
            os.makedirs(location)
            # print('folder created')
        else:
            # print("folder exists")
            pass
         
        os.chdir(location)
        
        # curentWorkingDirectory = os.getcwd()
        # print(curentWorkingDirectory)
        # print("New curentWorkingDirectory")


def GetAllTableNamesFromDatabase(Database):
    Exists=os.path.isfile(Database)

    if Exists:
        conn = sqlite3.connect(Database) 
        c = conn.cursor() 

        c.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'") 
        conn.commit() 

        rows = c.fetchall()

        TableList=[]
        for row in rows:
            value=list(row)[0]
            print(value)
            TableList.append(value)

        print(TableList)
        print("Done Database Read")

        c.close() 
        conn.close()

        return TableList

    else:
        print("could not find file!")

def GetTableDataFromTable(Database,TableName='',TableNumber=''):
    

    if TableNumber !='':
        TableList=GetAllTableNamesFromDatabase(Database)
        TableName=TableList[TableNumber]
        print(TableName,"TableName used")
    
    if TableName !='':
        Datalist, names= '',''

        conn = sqlite3.connect(Database) 
        c = conn.cursor() 

        try:
            c.execute("SELECT * FROM "+ TableName)

            names = [description[0] for description in c.description]

            rows = c.fetchall()

            Datalist=[]
            for row in rows:
                # print(row)
                Datalist.append(list(row))

            print(Datalist)

            print(Datalist[0][4])

            print('Datalist')

            print(names)

            print("names")

        except Exception as e:
            print(e)

        c.close() 
        conn.close() 


        return Datalist, names

def DropSqlTable(Database, TableName):

    conn  = sqlite3.connect(Database)

    c      = conn.cursor()

    dropTableStatement = "DROP TABLE "+TableName

    try:
        c.execute(dropTableStatement)
        print("Table Dropped Sucessfully")
    except Exception as e:
        print(e)

    c.close() 
    conn.close() 


    


Database='pythonDB.db'

# Database='AutoFormFiller.db'

# TableName='RecordONE'

# TableName='KEY_file2'

TableName='Recordfive5'




# ChangeStartupDirectory(Folder='AutoFormFillerKey')


# GetAllTableNamesFromDatabase(Database=Database)


# GetTableDataFromTable(Database=Database,TableName=TableName)


GetTableDataFromTable(Database=Database,TableNumber=-1)


# DropSqlTable(Database=Database,TableName=TableName)




