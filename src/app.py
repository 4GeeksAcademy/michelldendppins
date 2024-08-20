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
from models import db, Planets, Characters, Vehicles, Starships, Species
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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




@app.route('/planets', methods=['GET'])
def get_planets():
    all_planets = Planets.query.all()
    all_planets_serialize = [planet.serialize() for planet in all_planets]    
    return jsonify(all_planets_serialize), 200


@app.route('/characters', methods=['GET'])
def get_characters():
    all_characters = Characters.query.all()
    all_characters_serialize = [character.serialize() for character in all_characters]    
    return jsonify(all_characters_serialize), 200

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    all_vehicles = Vehicles.query.all()
    all_vehicles_serialize = [vehicle.serialize() for vehicle in all_vehicles]    
    return jsonify(all_vehicles_serialize), 200


@app.route('/starships', methods=['GET'])
def get_starships():
    all_starships = Starships.query.all()
    all_starships_serialize = [starship.serialize() for starship in all_starships]    
    return jsonify(all_starships_serialize), 200

@app.route('/species', methods=['GET'])
def get_species():
    all_species = Species.query.all()
    all_species_serialize = [specie.serialize() for specie in all_species]    
    return jsonify(all_species_serialize), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
