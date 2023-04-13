from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    

    def __init__(self, title, price, category, description, image):
        self.title = title
        self.price = price
        self.category = category
        self.description = description
        self.image = image
    
    
    def saveProduct(self):
        db.session.add(self)
        db.session.commit()