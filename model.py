from config import db
import enum 
from sqlalchemy import Enum 


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    deliveryAddress = db.Column(db.String(200),nullable=False)
    Contact = db.Column(db.String(200),nullable=False)
    active = db.Column(db.String(200),nullable=False)
    

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    weight = db.Column(db.Float,nullable=False)
    description = db.Column(db.String(200),nullable=False)
    
    #def getPriceForQuantity()

    #def getWeight():

class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    qty = db.Column(db.Integer,nullable=False)
    taxStatus = db.Column(db.String(200),nullable=False)
    
    def calculateSubTotal():
        pass
        
    
    def calculateWeight():
        pass

    
class OrderStatus(enum.Enum):
    CREATE = 0
    SHIPPING = 1
    DELIVERED = 2
    PAID = 3


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=True)
    amount = db.Column(db.Float,nullable=False)
    payment_mode = db.Column(db.String(200),nullable=False)
    

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    number = db.Column(db.Float,nullable=False)
    type = db.Column(db.String(200),nullable=False)
    expireDate = db.Column(db.Date,nullable=False)
   
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key= True,nullable=True)
    createDate=db.Column(db.Date,nullable=False)