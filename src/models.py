from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    favorites = db.relationship("Favorites", backref="user")

    def __repr__(self):
        return '<User %r' % self.username
    
    def serialize(self):
        return{
            "id": self.id,
            "email": self.email,
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    favorites = db.relationship("Favorites", backref="people")


    def serialize(self):
        return{
            
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'birth_year': self.birth_year,
            'gender': self.gender,
            'favorites': [favorite.serialize() for favorite in self.favorites]

        }



class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    manufacturer = db.Column(db.String(45))
    orbital_period = db.Column(db.Integer)
    length = db.Column(db.Float)
    gravity = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    surface_water = db.Column(db.Integer)
    favorites = db.relationship("Favorites", backref="planets")

def serialize(self):
        return {
             'id': self.id,
            'name': self.name,
            'url': self.url,
            'diameter': self.diameter,
            'rotation_period': self.rotation_period,
            'manufacturer': self.manufacturer,
            'orbital_period': self.orbital_period,
            'length': self.length,
            'gravity': self.gravity,
            'population': self.population,
            'climate': self.climate,
            'terrain': self.terrain,
            'surface_water': self.surface_water
        }




class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    model = db.Column(db.String(50))
    vehicle_class = db.Column(db.String(45))
    manufacturer = db.Column(db.String(50))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Float)
    crew = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(50))
    favorites = db.relationship("Favorites", backref="vehicles")


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'model': self.model,
            'vehicle_class': self.vehicle_class,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'crew': self.crew,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables
        }


class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def serialize(self):
        return {
            'id': self.id,
            'people_id': self.people_id,
            'vehicles_id': self.vehicles_id,
            'planets_id': self.planets_id,
            'user_id': self.user_id
        }
