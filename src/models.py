from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)
    mass = db.Column(db.String(120), unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    skin_color = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(120), unique=False, nullable=False)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(120), unique=False, nullable=False)
    surface_water = db.Column(db.String(120), unique=False, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    rotation = db.Column(db.String(120), unique=False, nullable=False)
    orbit = db.Column(db.String(120), unique=False, nullable=False)
    diameter = db.Column(db.String(120), unique=False, nullable=False)
    imgurl = db.Column(db.String(120), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "climate": self.climate,
            "rotation": self.rotation,
            "orbit": self.orbit,
            "diameter": self.diameter,
            "imgurl": self.imgurl
        }

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    classification = db.Column(db.String(120), unique=False, nullable=False)
    language = db.Column(db.String(120), unique=False, nullable=False)
    homeplanet = db.Column(db.String(120), unique=False, nullable=False)
    avg_height = db.Column(db.String(120), unique=False, nullable=False)
    avg_lifespan = db.Column(db.String(120), unique=False, nullable=False)
    imgurl = db.Column(db.String(120), unique=False, nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "language": self.language,
            "homeplanet": self.homeplanet,
            "avg_height": self.avg_height,
            "avg_lifespan": self.avg_lifespan,
            "imgurl": self.imgurl
        }

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=False)
    manufacturer = db.Column(db.String(120), unique=False, nullable=False)
    length = db.Column(db.String(120), unique=False, nullable=False)
    crew = db.Column(db.String(120), unique=False, nullable=False)
    passengers = db.Column(db.String(120), unique=False, nullable=False)
    vehicle_class = db.Column(db.String(120), unique=False, nullable=False)
    imgurl = db.Column(db.String(120), unique=False, nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "modal ": self.model,
            "manufacturer": self.manufacturer,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "vehicle_class": self.vehicle_class,
            "imgurl": self.imgurl
        }