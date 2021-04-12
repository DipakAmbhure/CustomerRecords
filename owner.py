import mysqldatabase
import mysql.connector
from datetime import datetime

#owner class containg all owner operations 
class owner():

    def __init__(self):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="useme",database="crecords")
        mycursor=mydb.cursor()
        mycursor.execute("Select * from records")
        self.r = mycursor.fetchall()
        self.totalcost=0
        return

    

    def todayincome(self):
        day=datetime.now()
        day=str(day)
        day=day[:10]
        income=0
        for row in self.r:
            rd=row[8]
            rd=rd[:10]
            if(day==rd):
                income+=row[6]
                self.totalcost+=1
        
        return income

    def todaypending(self):
        day=datetime.now()
        day=str(day)
        day=day[:10]
        pending=0
        for row in self.r:
            rd=row[8]
            rd=rd[:10]
            if(day==rd):
                pending+=row[7]
                
        
        return pending

    def decide(self,d):
        y=d[:4]
        y=int(y)
        m=d[8:10]
        m=int(m)
        if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
            return 31
        if(m==4 or m==6 or m==9 or m==11):
            return 30
        if((y%4==0 and y%100!=0) or y%400==0):
            return 29
        return 28
        


    def weekincome(self):
        day=datetime.now()
        day=str(day)
        year=day[:4]
        month=day[8:10]
        day=day[5:7]
        day=int(day)
        income=0
        for row in self.r:
            rd=row[8]
            ry=rd[:4]
            rm=rd[8:10]
            rd=rd[5:7]
            rd=int(rd)
            if((rd+7)%self.decide(row[8])>=day):
                income+=row[6]
                self.totalcost+=1

        return income
    
    def weekpending(self):
        day=datetime.now()
        day=str(day)
        year=day[:4]
        month=day[8:10]
        day=day[5:7]
        day=int(day)
        pending=0
        for row in self.r:
            rd=row[8]
            ry=rd[:4]
            rm=rd[8:10]
            rd=rd[5:7]
            rd=int(rd)
            if((rd+7)%self.decide(row[8])>=day):
                pending+=row[7]

        return pending

    def monthincome(self):
        day=datetime.now()
        day=str(day)
        y=day[:4]
        month=day[6:8]
        income=0
        for row in self.r:
            rd=row[8]
            ry=rd[:4]
            rm=rd[6:8]
            if(y==ry and month==rm):
                income+=row[6]
                self.totalcost+=1

        return income


    def monthpending(self):
        day=datetime.now()
        day=str(day)
        y=day[:4]
        month=day[6:8]
        pending=0
        for row in self.r:
            rd=row[8]
            ry=rd[:4]
            rm=rd[6:8]
            if(y==ry and month==rm):
                pending+=row[7]
        
        return pending


    def allincome(self):
        income=0
        for row in self.r:
            income+=row[6]
            self.totalcost+=1
        return income

    def allpending(self):
        pending = 0
        for row in self.r:
            pending+=row[7]
        
        return pending







