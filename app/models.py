from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    

    def __init__(self, id, title, price, category, description, image):
        self.id = id
        self.title = title
        self.price = price
        self.category = category
        self.description = description
        self.image = image
    
    
    def saveProduct(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'price' : self.price,
            'category' : self.category,
            'description' : self.description,
            'image' : self.image
        }