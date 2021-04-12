from crapp import CRapp
from mysqldatabase import database


#class to start app with initilizing database and CRapp
#on start it will run app and will create database if not exists
class Application():
    
    def __init__(self):
        self.database=database()
        self.app=CRapp()
        return

    def start(self):    
        self.database.create_database()
        self.app.run()
        return

