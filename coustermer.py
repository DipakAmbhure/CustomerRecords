import datetime
import random
import mysql.connector
from PIL import ImageFont, ImageDraw , Image
import os
from datetime import date


#Coustemer class with coustemer attributes
class Coustemer():
    
    def __init__(self):
        self.Name=None
        self.MoNo=None
        self.Address=None
        self.CQuery = None
        self.Product = None
        self.paid = None
        self.Pending = None
        self.purdate = None
        self.paydate = None
        self.Remark = None
        self.uniqid = None


    def GIVEID(self,name):
        a = random.randint(200,1000)
        for i in name:
            a = a + ord(i)
        return a



    def set_cous(self,name, mono, address,cquery, product, paid, pending, purdate, paydate, remark ):
        self.Name = name.lower()
        self.MoNo = mono
        self.Address = address
        self.CQuery = cquery
        self.Product = product
        self.paid = paid
        self.Pending = pending
        self.purdate = purdate
        self.paydate = paydate
        self.Remark = remark
        self.uniqid = self.GIVEID(self.Name)

    def generate_reciept(self):
        image = Image.new('RGB',(600,1000), color='white')
        draw = ImageDraw.Draw(image)
        path=os.path.dirname(os.path.abspath(__file__))
        dirpath=path.replace("\\","/") 
        try:
            rep=f"{dirpath}/Receipts"
            os.mkdir(rep)
        except:
            pass      
        font = ImageFont.truetype(f"{dirpath}/fonts/ShutDownDemoShadow.ttf", 50)
        draw.text((170, 50), "SHOP NAME", font=font, fill=(0,0,0))
        y=250
        font = ImageFont.truetype(f"{dirpath}/fonts/LittleLordFontleroyNF.ttf", 35)
        draw.text((100, 150), "Name : {}".format(self.Name), font=font, fill=(0,0,0))
        draw.text((100, 200), "Your Uniquid is : {}".format(self.uniqid), font=font, fill=(0,0,0))

        if(self.MoNo!=None):
            draw.text((100, y), "Mobile : {}".format(self.MoNo), font=font, fill=(0,0,0))
            y+=50
        if(self.Address!=None):
            draw.text((100, y), "Address : {}".format(self.Address), font=font, fill=(0,0,0))
            y+=50
        y+=50
        font = ImageFont.truetype(f"{dirpath}/fonts/arial.ttf",30)
        draw.text((100, y), "Product : {}".format(self.Product), font=font, fill=(0,0,0))
        y+=50
        font = ImageFont.truetype(f"{dirpath}/fonts/digital-7.ttf", 30)
        draw.text((100, y), "Paid  : {}".format(self.paid), font=font, fill=(0,0,0))
        y+=50
        draw.text((100, y), "Pending  : {}".format(self.Pending), font=font, fill=(0,0,0))
        y+=100

        font = ImageFont.truetype(f"{dirpath}/fonts/arial.ttf",30)        
        if(self.CQuery!=None):
            draw.text((100, y), "Your Query : {}".format(self.CQuery), font=font, fill=(0,0,0))
            y+=50
        if(self.Remark!=None): 
            draw.text((100, y), "Remark : {}".format(self.Remark), font=font, fill=(0,0,0))
            y+=50

        y+=30
        font = ImageFont.truetype(f"{dirpath}/fonts/LittleLordFontleroyNF.ttf",30) 
        draw.text((100, y), "Thank You !!! : ", font=font, fill=(0,0,0))
      
        image.save(f"{dirpath}/Receipts/{self.Name}{str(random.randint(290,36389))}.png")

        return


#class to do some operations on particular coustemer
class coustemers(Coustemer):

    def __init__(self):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="useme",database="crecords")
        mycursor=mydb.cursor()
        mycursor.execute("Select * from records")
        self.r = mycursor.fetchall()
        return

    def check_in_database(self,c):
        d=0
        if(c.uniqid!=None):
            try:
                b=c.uniqid.strip("")
                d=int(b)
            except:
                return 0
        for row in self.r:    
            if(row[0]==d):
                return row[0]
            if(c.Name!=None):
                sor = row[1].strip("").split(" ")
                des = c.Name.strip("").split(" ")
                n = len(sor)
                flag=0
            

                for j in sor:
                    if j in des:
                        flag+=1
                if(flag==n and n==len(des)):
                    return row[0]

            if(row[2]!=None and c.MoNo !=None and (row[2] in c.MoNo or c.MoNo in row[2])):
                        return row[0]
        return 0
                


    def show_all_of_coustermer(self,coust):
        r=[]
        for row in self.r:
            if(row[0]==coust.uniqid):
                r.append(row)
        p=tuple(r)
        return p


    def generate_reciept(self,coust):
        r=self.show_all_of_coustermer(coust)
        if(len(r)==0):
            return 0
        unid = r[0][0]
        Name = r[0][1]
        MoNo = None
        Address = None
        producttimes=[]
        totalpaid,totalpending = 0,0
        for i in r:
            if(i[3]!=None):
                Address = i[3]
                break

        flag1,flag2=0,0
        for i in r:
            if(not flag1 and i[2]!=None):
                MoNo =  i[2]
                flag1=1
            if(not flag2 and i[3]!=None):
                Address = i[3]
                flag2=1
            if(flag1 and flag2):
                break

        for i in r:
            producttimes.append((i[5],i[6],i[7],i[4],i[8],i[9],i[10]))
            totalpaid += i[6]
            totalpending += i[7]

        ppt = tuple(producttimes)
        #reciept = (unid,Name,MoNo,Address,ppt,totalpaid,totalpending)

        
        path=os.path.dirname(os.path.abspath(__file__))
        dirpath=path.replace("\\","/") 
        try:
            rep=f"{dirpath}/Coustemer"
            os.mkdir(rep)
        except:
            pass 
        
        image = Image.new('RGB',(1600,2500), color='white')
        draw = ImageDraw.Draw(image)
             
        font = ImageFont.truetype(f"{dirpath}/fonts/ShutDownDemoShadow.ttf", 55)
        draw.text((600, 50), "SHOP NAME", font=font, fill=(0,0,0))

        font = ImageFont.truetype(f"{dirpath}/fonts/LittleLordFontleroyNF.ttf", 35)
        draw.text((400, 150), "Name : {}".format(Name), font=font, fill=(0,0,0))
        draw.text((400, 200), "UID : {}".format(unid), font=font, fill=(0,0,0))
        y=250
        if(MoNo!=None):
            draw.text((400, y), "Mobile : {}".format(MoNo), font=font, fill=(0,0,0))
            y+=50
        if(Address!=None):
            draw.text((400, y), "Address : {}".format(Address), font=font, fill=(0,0,0))
            y+=50
        y+=50

        font = ImageFont.truetype(f"{dirpath}/fonts/LittleLordFontleroyNF.ttf", 35)           
        draw.text((1, y), "Product", font=font, fill=(0,0,0))
        draw.text((200, y), "Paid", font=font, fill=(0,0,0))
        draw.text((400, y), "Pending", font=font, fill=(0,0,0))
        draw.text((600, y), "Query", font=font, fill=(0,0,0))
        draw.text((900, y), "Pur.Date", font=font, fill=(0,0,0))
        draw.text((1100, y), "Pay.Date", font=font, fill=(0,0,0))
        draw.text((1300, y), "Remark", font=font, fill=(0,0,0))
        i=0
        y+=60
        font = ImageFont.truetype(f"{dirpath}/fonts/arial.ttf",20)
        for row in ppt:
            flag=1    
            draw.text((1, y), f"{row[0]}", font=font, fill=(0,0,0))
            draw.text((200, y), f"{row[1]}", font=font, fill=(0,0,0))
            draw.text((400, y), f"{row[2]}", font=font, fill=(0,0,0))
            draw.text((600, y), f"{row[3]}", font=font, fill=(0,0,0))
            draw.text((900, y), f"{row[4][:10]}", font=font, fill=(0,0,0))
            draw.text((1100, y), f"{row[5][:10]}", font=font, fill=(0,0,0))
            draw.text((1300, y), f"{row[6]}", font=font, fill=(0,0,0))
            y+=40
            if(y>2300):
                image.save(f"{dirpath}/Coustemer/{Name}{unid}{i}.png")
                i+=1
                image = Image.new('RGB',(1600,2500), color='white')
                draw = ImageDraw.Draw(image)
                    
                font = ImageFont.truetype(f"{dirpath}/fonts/ShutDownDemoShadow.ttf", 55)
                draw.text((800, 50), "SHOP NAME", font=font, fill=(0,0,0))
                    
                font = ImageFont.truetype(f"{dirpath}/fonts/LittleLordFontleroyNF.ttf", 35)           
                draw.text((1, 150), "Product", font=font, fill=(0,0,0))
                draw.text((200, 150), "Paid", font=font, fill=(0,0,0))
                draw.text((400, 150), "Pending", font=font, fill=(0,0,0))
                draw.text((600, 150), "Query", font=font, fill=(0,0,0))
                draw.text((900, 150), "Pur.Date", font=font, fill=(0,0,0))
                draw.text((1100, 150), "Pay.Date", font=font, fill=(0,0,0))
                draw.text((1300, 150), "Remark", font=font, fill=(0,0,0))
                y=200
                flag=0
                font = ImageFont.truetype(f"{dirpath}/fonts/arial.ttf",20)

        if(flag):
            image.save(f"{dirpath}/Coustemer/{Name}{unid}{i}.png")
    
     

        return 1




        