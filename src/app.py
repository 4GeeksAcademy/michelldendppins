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



#GET METHOD PLANETS#########################
@app.route('/planets', methods=['GET'])
def get_planets():
    all_planets = Planets.query.all()
    all_planets_serialize = [planet.serialize() for planet in all_planets]    
    return jsonify(all_planets_serialize), 200
#GET METHOD PLANETS ID
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planets_id(planet_id):
    callOnePlanet = Planets.query.get(planet_id)
    return jsonify(callOnePlanet.serialize()), 200
#POST METHOD PLANETS
@app.route('/planets', methods=['POST']) 
def create_planets():
    body = request.get_json() #esta linea lo que hace es capturar la informacion del front o del thunder
    new_planet = Planets(name = body['name'])
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({'msg': new_planet.serialize()}), 200
#DELETE METHOD PLANETS
@app.route('/planets/<int:id>', methods= ['DELETE'])
def deletePlanet(id):
    planet = Planets.query.get(id)
    db.session.delete(planet)
    db.session.commit()
    response_body = {"msg": "borrado"}
    return jsonify(planet.serialize())


#GET METHOD CHARACTERS #####################
@app.route('/characters', methods=['GET'])
def get_characters():
    all_characters = Characters.query.all()
    all_characters_serialize = [character.serialize() for character in all_characters]    
    return jsonify(all_characters_serialize), 200
#GET METHOD CHARACTER ID
@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character_id(character_id):
    callOneCharacter = Characters.query.get(character_id)
    return jsonify(callOneCharacter.serialize()), 200
#POST METHOD CHARACTERS
@app.route('/characters', methods=['POST']) 
def create_characters():
    body = request.get_json() #esta linea lo que hace es capturar la informacion del front o del thunder
    new_character = Characters(name = body['name'])
    db.session.add(new_character)
    db.session.commit()
    return jsonify({'msg': new_character.serialize()}), 200
#DELETE METHOD CHARACTERS
@app.route('/characters/<int:id>', methods= ['DELETE'])
def deleteCharacter(id):
    character = Characters.query.get(id)
    db.session.delete(character)
    db.session.commit()
    response_body = {"msg": "borrado"}
    return jsonify(character.serialize())









#GET METHOD VEHICLES
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    all_vehicles = Vehicles.query.all()
    all_vehicles_serialize = [vehicle.serialize() for vehicle in all_vehicles]    
    return jsonify(all_vehicles_serialize), 200



#GET METHOD STARSHIPS
@app.route('/starships', methods=['GET'])
def get_starships():
    all_starships = Starships.query.all()
    all_starships_serialize = [starship.serialize() for starship in all_starships]    
    return jsonify(all_starships_serialize), 200


#GET METHOD SPECIES
@app.route('/species', methods=['GET'])
def get_species():
    all_species = Species.query.all()
    all_species_serialize = [specie.serialize() for specie in all_species]    
    return jsonify(all_species_serialize), 200












# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
