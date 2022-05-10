"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Species, Vehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/characters', methods=['GET'])
def my_characters():
    characters_query = Characters.query.all()
    all_characters = list(map(lambda character: character.serialize(), characters_query))
    return jsonify(all_characters), 200

@app.route('/characters/<int:characters_id>', methods=['GET'])
def character_by_id(characters_id):
    user1 = Characters.query.get(characters_id)
    return jsonify(user1.serialize()), 200


@app.route('/planets', methods=['GET'])
def get_planets():
    planets_query = Planets.query.all()
    all_planets = list(map(lambda planet: planet.serialize(), planets_query))
    return jsonify(all_planets), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def planet_by_id(planet_id):
    planet1 = Planets.query.get(planet_id)
    return jsonify(planet1.serialize()), 200


@app.route('/species', methods=['GET'])
def get_species():
    species_query = Species.query.all()
    all_species = list(map(lambda specie: specie.serialize(), species_query))
    return jsonify(all_species), 200

@app.route('/species/<int:specie_id>', methods=['GET'])
def specie_by_id(specie_id):
    specie1 = Species.query.get(specie_id)
    return jsonify(specie1.serialize()), 200


@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles_query = Vehicles.query.all()
    all_vehicles = list(map(lambda vehicle: vehicle.serialize(),vehicles_query))
    return jsonify(all_vehicles), 200

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def vehicle_by_id(vehicle_id):
    vehicle1 = vehicles.query.get(vehicle_id)
    return jsonify(vehicle1.serialize()), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
