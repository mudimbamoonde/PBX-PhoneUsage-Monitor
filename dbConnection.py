import pymssql
import json


class Master:

    # connect = pymssql.connect(server=connections["ServerName"],user=connections["user"],
    #                                 password=connections["password"],database=connections["database"])
    def Connection(self,connect,connections):
        pass

    def GetData(self):
        connections = {
            "ServerName": "192.168.0.245\KAS",
            "user": "app_svc",
            "password": "XgHb][d8F'",
            "database": "call_accounts"
        }
        connect = pymssql.connect(server=connections["ServerName"], user=connections["user"],
                                  password=connections["password"], database=connections["database"])
        # print(connections["ServerName"])
        cursor = connect.cursor()
        cursor.execute("SELECT TOP(200) *FROM calls ORDER BY Call_Start DESC")
        row = cursor.fetchone()
        filledRow = {}
        container = []
        # filledRow.sort()
        while row:
            # print(str(row[0]), str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]))
            filledRow = {
                "ID": str(row[0]),
                "Caller_ID": str(row[1]),
                "Destination": str(row[2]),
                "Call_Start": str(row[3]),
                "Account_Code": str(row[4]),
                "Duration_Seconds": str(row[5]),
                "Disposition": str(row[6]),
            }

            container.append(filledRow)

            row = cursor.fetchone()
            Signal = json.dumps(filledRow)
            cover = json.loads(Signal)
            # print(Signal)
        return container

    def CalculateCost(self):
        connections = {
            "ServerName": "192.168.0.245\KAS",
            "user": "app_svc",
            "password": "XgHb][d8F'",
            "database": "call_accounts"
        }
        connect = pymssql.connect(server=connections["ServerName"], user=connections["user"],
                                  password=connections["password"], database=connections["database"])

        query = """SELECT TOP 200 Account_Code, SUM(Duration_Seconds) AS
         Duration_Seconds, SUM(CAST(Duration_Seconds AS decimal(10, 2))) / 60 * 10 AS Cost_ZKW, 
         MIN(Call_Start) AS From_Date, MAX(Call_Start) 
        AS ToDate FROM calls GROUP BY Account_Code ORDER BY Account_Code """
        cursor = connect.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        filledRow = {}
        container = []
        # filledRow.sort()
        while row:
            # print(str(row[0]), str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]))
            filledRow = {
                "Account_Code": str(row[0]),
                "Duration_Seconds": str(row[1]),
                "Cost_ZKW": str(row[2]),
                "From_Date": str(row[3]),
                "ToDate": str(row[4]),
            }

            container.append(filledRow)

            row = cursor.fetchone()
            Signal = json.dumps(filledRow)
            cover = json.loads(Signal)
            # print(Signal)
        return container

    def ChartDisplay(self):
        connections = {
            "ServerName": "192.168.0.245\KAS",
            "user": "app_svc",
            "password": "XgHb][d8F'",
            "database": "call_accounts"
        }
        connect = pymssql.connect(server=connections["ServerName"], user=connections["user"],
                                  password=connections["password"], database=connections["database"])

        query = """SELECT TOP 200 Account_Code, SUM(Duration_Seconds) AS
                Duration_Seconds, SUM(CAST(Duration_Seconds AS decimal(10, 2))) / 60 * 10 AS Cost_ZKW, 
                MIN(Call_Start) AS From_Date, MAX(Call_Start) 
               AS ToDate FROM calls GROUP BY Account_Code ORDER BY Account_Code """
        cursor = connect.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        pickedRow = {}
        container = []
        while row:
            pickedRow = {
                "Account_Code": str(row[0]),
                "Duration_Seconds": str(row[1]),
                "Cost_ZKW": str(row[2]),
                "From_Date": str(row[3]),
                "ToDate": str(row[4]),
            }

            container.append(pickedRow)
            row = cursor.fetchone()
        return container

    def AccontCode(self,accountName):
        connections = {
            "ServerName": "192.168.0.245\KAS",
            "user": "app_svc",
            "password": "XgHb][d8F'",
            "database": "call_accounts"
        }
        connect = pymssql.connect(server=connections["ServerName"], user=connections["user"],
                                  password=connections["password"], database=connections["database"])

        query="""SELECT TOP 200 Account_Code, SUM(Duration_Seconds) AS Duration_Seconds, SUM(CAST(Duration_Seconds AS 
                        decimal(10, 2))) / 60 * 10 AS Cost_ZKW, 
                        MIN(Call_Start) AS From_Date, MAX(Call_Start) 
                        AS ToDate FROM calls WHERE Account_Code='{}' GROUP BY Account_Code """.format(accountName)
        cursor = connect.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        filledRow = {}
        container = []
        # filledRow.sort()
     
        while row:
            # print(str(row[0]), str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]))
            filledRow = {
                "Account_Code": str(row[0]),
                "Duration_Seconds": str(row[1]),
                "Cost_ZKW": str(row[2]),
                "From_Date": str(row[3]),
                "ToDate": str(row[4]),
            }

            container.append(filledRow)

            row = cursor.fetchone()

            # print(Signal)
            print(container)
        return container

    def GroupOfMany(self,accountName):
            connections = {
                "ServerName": "192.168.0.245\KAS",
                "user": "app_svc",
                "password": "XgHb][d8F'",
                "database": "call_accounts"
            }
            connect = pymssql.connect(server=connections["ServerName"], user=connections["user"],
                                    password=connections["password"], database=connections["database"])

            query = "SELECT*FROM calls WHERE Account_Code='{}'".format(accountName)
            cursor = connect.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            filledRow = {}
            container = []
            # filledRow.sort()
        
            while row:
                # print(str(row[0]), str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]))
                filledRow = {
                        "ID": str(row[0]),
                        "Caller_ID": str(row[1]),
                        "Destination": str(row[2]),
                        "Call_Start": str(row[3]),
                        "Account_Code": str(row[4]),
                        "Duration_Seconds": str(row[5]),
                        "Disposition": str(row[6]),
                    }
                container.append(filledRow)

                row = cursor.fetchone()

                # print(Signal)
                # print(container)
            return container

    def InsertCode(self,accountName,fname,lname,location,dpt,date):
                connections = {
                    "ServerName": "192.168.0.245\KAS",
                    "user": "app_svc",
                    "password": "XgHb][d8F'",
                    "database": "call_accounts"
                }

                connect = pymssql.connect(server=connections["ServerName"], user=connections["user"],
                                        password=connections["password"], database=connections["database"])

                query = """INSERT INTO staff (Account_Code,Firstname,
                Surname,Location,Department,Date_Record_Created) VALUES('{}','{}','{}','{}','{}','{}') """.format(accountName,fname,lname,location,dpt,date)
                cursor = connect.cursor()
                cursor.execute(query)
                connect.commit()
                connect.close()
            
    def QueryCodes(self):
            connections = {
                "ServerName": "192.168.0.245\KAS",
                "user": "app_svc",
                "password": "XgHb][d8F'",
                "database": "call_accounts"
                    }
            connect = pymssql.connect(server=connections["ServerName"], user=connections["user"],
                                            password=connections["password"], database=connections["database"])

            query = """ SELECT TOP 200 *FROM staff """
            cursor = connect.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            filledRow = {}
            container = []
            # filledRow.sort()
        
            while row:
                # print(str(row[0]), str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]))
                filledRow = {
                        "ID": str(row[0]),
                        "Account_Code": str(row[1]),
                        "FirstName": str(row[2]),
                        "LastName": str(row[3]),
                        "Location": str(row[4]),
                        "Department": str(row[5]),
                        "Date_Record_Created": str(row[6]),
                    }
                container.append(filledRow)

                row = cursor.fetchone()

                # print(Signal)
                # print(container)
            return container


    def DeleteUser(self,id):
        connections = {
                    "ServerName": "192.168.0.245\KAS",
                    "user": "app_svc",
                    "password": "XgHb][d8F'",
                    "database": "call_accounts"
                }
        connect = pymssql.connect(server=connections["ServerName"], user=connections["user"],
        password=connections["password"], database=connections["database"])
        query = """DELETE FROM staff WHERE ID='{}'""".format(id)
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
        connect.close()

# tape = Master()
# data = tape.AccontCode('870')
# print(data)
