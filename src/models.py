from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planets(db.Model):
    __tablename__= 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
         return '<Planets %r>' % self.name 

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    __tablename__= 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
         return '<Characters %r>' % self.name 

    def serialize(self):

        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }    
    
class Vehicles(db.Model):
    __tablename__= 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
         return '<Vehicles %r>' % self.name 

    def serialize(self):

        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }     
    
class Starships(db.Model):
    __tablename__= 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
         return '<Starships %r>' % self.name 

    def serialize(self):

        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }        
    
class Species(db.Model):
    __tablename__= 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
         return '<Species %r>' % self.name 

    def serialize(self):

        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }     