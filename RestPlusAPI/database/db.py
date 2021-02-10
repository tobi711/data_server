
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()



#Typ: Product 
def add(product):
    db.session.add(product)
    db.session.commit()

def reset():
    db.drop_all()
    db.create_all()
    
