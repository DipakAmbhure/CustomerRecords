import mysql.connector
import coustermer

#class database to create database and add coustemers to it in tabel 
#name of database = CRecords
#tabel name = records
#host = localhost
#user = root
#passwd = useme
class database(coustermer.Coustemer):

    def __init__(self):
        return

    def create_database(self):
        start = mysql.connector.connect(host="localhost",user="root",passwd="useme")
        mycursor = start.cursor()
        try:
            mycursor.execute("Create database crecords")
            mydb = mysql.connector.connect(host = "localhost", user="root", passwd="useme", database = "crecords")
            cursorpoint = mydb.cursor()
            cursorpoint.execute("Create table records(uniqid int,name varchar(255), mobile varchar(20), address varchar(255), cqueery varchar(255), product varchar(255), paid int , pending int , purdate varchar(255), paydate varchar(255), remark varchar(255))")
        except:
            pass
        finally:
            mycursor.close()
            start.close()
    
    def add_coustemer(self,C):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="useme",database="crecords")
        mycursor = mydb.cursor()

        self.makeuniqueidright(C)

        mycursor.execute("""INSERT INTO records
                            values 
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(C.uniqid,C.Name,C.MoNo,C.Address,C.CQuery,C.Product,C.paid,C.Pending,C.purdate,C.paydate,C.Remark)
                        )
        mydb.commit()
        return

    def get_coustemers(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="useme", database = "crecords")
        mycursor =  mydb.cursor()
        mycursor.execute("select * from records")
        r = mycursor.fetchall()
        return r


    def delete_database(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="useme")
        mycursor = mydb.cursor()
        mycursor.execute("Drop database crecords")
        return

    #method to make uniqueid same for same user 
    def makeuniqueidright(self,c):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="useme",database="crecords")
        mycursor=mydb.cursor()
        mycursor.execute("Select * from records")
        r = mycursor.fetchall()
        des = c.Name
        for row in r:
            sor = row[1].strip("").split(" ")
            des = c.Name.strip("").split(" ")
            n = len(sor)
            flag=0
            if(row[2]!=None and c.MoNo !=None and (row[2] in c.MoNo or c.MoNo in row[2])):
                        c.uniqid = row[0]

            for j in sor:
                if j in des:
                    flag+=1
            if(flag==n and n==len(des)):
                c.uniqid = row[0]
        return






