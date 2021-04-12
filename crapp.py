from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
import tkinter as tk
from tkinter import filedialog
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.popup import Popup
from coustermer import Coustemer,coustemers
from datetime import datetime
from datetime import date
from mysqldatabase import database
from owner import owner
from PIL import ImageFont, ImageDraw, Image
import os
import random


#window size when app will run
Window.size=(350,600)

#loading mykeevi.kv file which contain all code of user interface
Builder.load_file('D:/College/2nd year/IV semister/RPPOOP/Project/mykeevi.kv')


#clas of main screen to add new coustemer and generate receipt
class MainScreen(Screen):
    


    def value(self):
        db=database()
        #use all input here
        if(self.cname.text=="" or self.cproduct.text=="" or self.cpaid.text=="" or self.cpending.text==""):
            layout = BoxLayout(orientation='vertical')
            label = MDLabel(text="Plese fill all * marked fields !!", theme_text_color="Primary")
            layout.add_widget(label)
            popup = Popup(title="Failed",content=layout,size_hint=(None,None),size=(200,100))
            popup.open()
            return

        self.c=Coustemer()
        mobile=self.cmobile.text
        address=self.caddress.text
        cqueery=self.cquery.text
        cremark=self.cremark.text
        if(mobile==''):
            mobile=None
        if(address==''):
            address=None
        if(cqueery==''):
            cqueery=None
        if(cremark==''):
            cremark=None

        self.c.set_cous(self.cname.text,mobile,address,cqueery,self.cproduct.text,self.cpaid.text,self.cpending.text,datetime.now(),datetime.now(),cremark)
        db.add_coustemer(self.c)
        layout = BoxLayout(orientation='vertical')
        label = MDLabel(text="Saved Successfully !!", theme_text_color="Primary")
        layout.add_widget(label)
        popup = Popup(title="Success",content=layout,size_hint=(None,None),size=(200,100))
        popup.open()        
        self.cname.text=""
        self.cmobile.text=""
        self.caddress.text=""
        self.cpaid.text=""
        self.cpending.text=""
        self.cquery.text=""
        self.cremark.text=""
        self.cproduct.text=""
        #popup.dismiss()
        
        return

    def show_receipt(self):
        try:
            layout=BoxLayout(orientation='vertical')
            label1=MDLabel(text=f"Name  :  {self.c.Name}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.6})
            label2=MDLabel(text=f"Products : {self.c.Product}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.4})
            label3=MDLabel(text=f"Paid : {self.c.paid}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':3})
            label4=MDLabel(text=f"Pending : {self.c.Pending}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.2})
            label5=MDLabel(text=f"UID :  {self.c.uniqid}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':0.1,'y':5})
            button = MDFlatButton(text="Download",size=(100,50),pos_hint={'center_x':.5 , 'center_y':.2 },text_color=(0,1,0,1),md_bg_color=(.23,0,0.34,0.5))
            button.bind(on_press=self.downloadreceipt)
            layout.add_widget(label1)
            layout.add_widget(label5)
            layout.add_widget(label2)
            layout.add_widget(label3)
            layout.add_widget(label4)
            layout.add_widget(button)
            popup=Popup(content=layout,title='Coutemer_receipt',size_hint=(None,None),size=(280,400))
            popup.open()
        except:
            pass
        finally:
            return


    def downloadreceipt(self,obj):
        self.c.generate_reciept()
        path=os.path.dirname(os.path.abspath(__file__))
        dirpath=path.replace("\\","/") 
        layout = BoxLayout(orientation='vertical')
        label = MDLabel(text=f"Receipt Saved at loaction {dirpath}/Receipts/", theme_text_color="Primary")
        layout.add_widget(label)
        popup = Popup(title="Success",content=layout,size_hint=(None,None),size=(300,200))
        popup.open() 
        
        
        return


#class for owner screen with operations on reports and overall data 
class OwnerScreen(Screen):

    def dayreport(self):
        o=owner()
        layout=BoxLayout(orientation='vertical')
        label1=MDLabel(text=f"Date  :  {date.today()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.6})
        label3=MDLabel(text=f"TotalIncome : {o.todayincome()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':5})
        label2=MDLabel(text=f"TotalCoustemers : {o.totalcost}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.55})
        label4=MDLabel(text=f"TotalPending : {o.todaypending()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.45})
        #button = MDFlatButton(text="Download",size=(100,50),pos_hint={'center_x':.5 , 'center_y':.2 },text_color=(0,1,0,1),md_bg_color=(.23,0,0.34,0.5))
        #button.bind(on_press=self.downloadreceipt)
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(label4)
        #layout.add_widget(button)
        popup=Popup(content=layout,title='Coutemer_receipt',size_hint=(None,None),size=(280,400))
        popup.open()
        return

    def weekreport(self):
        o=owner()
        layout=BoxLayout(orientation='vertical')
        label1=MDLabel(text=f"Date  :  {date.today()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.6})
        label3=MDLabel(text=f"TotalIncome : {o.weekincome()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':5})
        label2=MDLabel(text=f"TotalCoustemers : {o.totalcost}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.55})
        label4=MDLabel(text=f"TotalPending : {o.weekpending()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.45})
        #button = MDFlatButton(text="Download",size=(100,50),pos_hint={'center_x':.5 , 'center_y':.2 },text_color=(0,1,0,1),md_bg_color=(.23,0,0.34,0.5))
        #button.bind(on_press=self.downloadreceipt)
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(label4)
        #layout.add_widget(button)
        popup=Popup(content=layout,title='Week_Report',size_hint=(None,None),size=(280,400))
        popup.open()
        return

    def monthreport(self):
        o=owner()
        layout=BoxLayout(orientation='vertical')
        label1=MDLabel(text=f"Date  :  {date.today()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.6})
        label3=MDLabel(text=f"TotalIncome : {o.monthincome()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':5})
        label2=MDLabel(text=f"TotalCoustemers : {o.totalcost}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.55})
        label4=MDLabel(text=f"TotalPending : {o.monthpending()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.45})
        #button = MDFlatButton(text="Download",size=(100,50),pos_hint={'center_x':.5 , 'center_y':.2 },text_color=(0,1,0,1),md_bg_color=(.23,0,0.34,0.5))
        #button.bind(on_press=self.downloadreceipt)
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(label4)
        #layout.add_widget(button)
        popup=Popup(content=layout,title='Month_Report',size_hint=(None,None),size=(280,400))
        popup.open()
        return

    def overallreport(self):
        o=owner()
        layout=BoxLayout(orientation='vertical')
        label1=MDLabel(text=f"Date  :  {date.today()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.6})
        label3=MDLabel(text=f"TotalIncome : {o.allincome()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':5})
        label2=MDLabel(text=f"TotalCoustemers : {o.totalcost}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.55})
        label4=MDLabel(text=f"TotalPending : {o.allpending()}",theme_text_color="Primary",font_style="Body1",pos_hint={'x':.1,'y':.45})
        #button = MDFlatButton(text="Download",size=(100,50),pos_hint={'center_x':.5 , 'center_y':.2 },text_color=(0,1,0,1),md_bg_color=(.23,0,0.34,0.5))
        #button.bind(on_press=self.downloadreceipt)
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(label4)
        #layout.add_widget(button)
        popup=Popup(content=layout,title='Overall_report',size_hint=(None,None),size=(280,400))
        popup.open()
        return

    def downloadreport(self):
        o=owner()
        path=os.path.dirname(os.path.abspath(__file__))
        dirpath=path.replace("\\","/") 
        try:
            rep=f"{dirpath}/Owner"
            os.mkdir(rep)
        except:
            pass 
        
        image = Image.new('RGB',(2000,2500), color='white')
        draw = ImageDraw.Draw(image)
             
        font = ImageFont.truetype(f"{dirpath}/fonts/ShutDownDemoShadow.ttf", 55)
        draw.text((1000, 50), "SHOP NAME", font=font, fill=(0,0,0))
            
        font = ImageFont.truetype(f"{dirpath}/fonts/LittleLordFontleroyNF.ttf", 35)           
        draw.text((1, 150), "UID", font=font, fill=(0,0,0))
        draw.text((200, 150), "Name", font=font, fill=(0,0,0))
        draw.text((400, 150), "Mobile", font=font, fill=(0,0,0))
        draw.text((600, 150), "Address", font=font, fill=(0,0,0))
        draw.text((900, 150), "Product", font=font, fill=(0,0,0))
        draw.text((1100, 150), "Paid", font=font, fill=(0,0,0))
        draw.text((1300, 150), "Pending", font=font, fill=(0,0,0))
        draw.text((1500, 150), "Date", font=font, fill=(0,0,0))
        draw.text((1700, 150), "Remark", font=font, fill=(0,0,0))
        y=200
        i=0
        font = ImageFont.truetype(f"{dirpath}/fonts/arial.ttf",20)
        for row in o.r:
            flag=1    
            draw.text((1, y), f"{row[0]}", font=font, fill=(0,0,0))
            draw.text((200, y), f"{row[1]}", font=font, fill=(0,0,0))
            draw.text((400, y), f"{row[2]}", font=font, fill=(0,0,0))
            draw.text((600, y), f"{row[3]}", font=font, fill=(0,0,0))
            draw.text((900, y), f"{row[5]}", font=font, fill=(0,0,0))
            draw.text((1100, y), f"{row[6]}", font=font, fill=(0,0,0))
            draw.text((1300, y), f"{row[7]}", font=font, fill=(0,0,0))
            draw.text((1500, y), f"{row[8][:10]}", font=font, fill=(0,0,0))
            draw.text((1700, y), f"{row[10]}", font=font, fill=(0,0,0))
            y+=40
            if(y>2300):
                image.save(f"{dirpath}/Owner/image{i}.png")
                i+=1
                image = Image.new('RGB',(2000,2500), color='white')
                draw = ImageDraw.Draw(image)
                    
                font = ImageFont.truetype(f"{dirpath}/fonts/ShutDownDemoShadow.ttf", 55)
                draw.text((1000, 50), "SHOP NAME", font=font, fill=(0,0,0))
                    
                font = ImageFont.truetype(f"{dirpath}/fonts/LittleLordFontleroyNF.ttf", 35)           
                draw.text((1, 150), "UID", font=font, fill=(0,0,0))
                draw.text((200, 150), "Name", font=font, fill=(0,0,0))
                draw.text((400, 150), "Mobile", font=font, fill=(0,0,0))
                draw.text((600, 150), "Address", font=font, fill=(0,0,0))
                draw.text((900, 150), "Product", font=font, fill=(0,0,0))
                draw.text((1100, 150), "Paid", font=font, fill=(0,0,0))
                draw.text((1300, 150), "Pending", font=font, fill=(0,0,0))
                draw.text((1500, 150), "Date", font=font, fill=(0,0,0))
                draw.text((1700, 150), "Remark", font=font, fill=(0,0,0))
                y=200
                flag=0
                font = ImageFont.truetype(f"{dirpath}/fonts/arial.ttf",20)

        if(flag):
            image.save(f"{dirpath}/Owner/image{i}.png")
     
        layout = BoxLayout(orientation='vertical')
        label = MDLabel(text=f"Receipt Saved at loaction {dirpath}/Owner/", theme_text_color="Primary")
        layout.add_widget(label)
        popup = Popup(title="Success",content=layout,size_hint=(None,None),size=(300,200))
        popup.open() 

        return




#class of coustemer class
class CoustemerScreen(Screen):

    def show(self):
        if(self.cname.text=="" and self.cmobile.text=="" and self.cuid.text==""):
            layout = BoxLayout(orientation='vertical')
            label = MDLabel(text="Plese fill atleast one of the field !!", theme_text_color="Primary")
            layout.add_widget(label)
            popup = Popup(title="Failed",content=layout,size_hint=(None,None),size=(200,100))
            popup.open()
            return

        c_o=coustemers()
        c=Coustemer()
        if(self.cname.text!=""):
            c.Name=self.cname.text
            self.cname.text=""
        if(self.cmobile.text!=""):
            c.MoNo=self.cmobile.text
            self.cmobile.text=""
        if(self.cuid.text!=""):
            c.uniqid=self.cuid.text
            self.cuid.text=""

        uid=c_o.check_in_database(c)
        if(uid!=0):
            c.uniqid=uid


        path=os.path.dirname(os.path.abspath(__file__))
        dirpath=path.replace("\\","/") 
        layout = BoxLayout(orientation='vertical')
        if(c_o.generate_reciept(c)):       
            label = MDLabel(text=f"Receipt Saved at loaction {dirpath}/Coustemers/", theme_text_color="Primary")
            layout.add_widget(label)
            popup = Popup(title="Success",content=layout,size_hint=(None,None),size=(300,200))
            popup.open() 
            return

        label = MDLabel(text=f"Coustemer Not found", theme_text_color="Primary")
        layout.add_widget(label)
        popup = Popup(title="Failed",content=layout,size_hint=(None,None),size=(300,200))
        popup.open() 
        return

        

        


class ContentNavigationDrawer(BoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    pass



#main class of APP with build method
class CRapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Cyan"
        self.theme_cls.theme_style = "Dark"
        self.sm=ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(OwnerScreen(name = 'owner'))
        self.sm.add_widget(CoustemerScreen(name = 'coustmer'))
        return self.sm

    
