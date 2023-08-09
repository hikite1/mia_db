#import basic flask application
from flask import Blueprint, jsonify, request
#import th db file to be used with this file
from .db import db
#template for generating a section of a web application applied to paramaters and creating an instance
bp=Blueprint('missing_person', __name__, url_prefix='/missing_person')

#GET query to return all records in database
@bp.route('', methods=['GET'])
def index():
    cur=db.cursor()
    cur.execute('SELECT * from missing_person_info')
    records=cur.fetchall()
    return jsonify(records)

#GET query for name in database
@bp.route('/<name>', methods=['GET'])
def mia_name(name):
    cur=db.cursor()
    cur.execute(f"SELECT * from missing_person_info WHERE name = '{name}'")
    records=cur.fetchall()
    return jsonify(records)

#POST query to add a name to database
@bp.route('', methods=['POST'])
def create():
    if 'mia_id' not in request.json or 'name' not in request.json:
        return abort(400)
    p = Person( #create a person model (defined in codebase) to create a new person insstance and import into this file
        mia_id=request.json['mia_id'],
        name=request.json['name']
    )
    db.session.add(p)
    db.session.commit()
    return jsonify(u.serialize())


#DELETE query to remove a person from the database
@bp.route('/missing_person_info/', methods=['DELETE'])
def delete(id):
    mia_id = request.json
    mia_id.delete(mia_id)
    return jsonify({'message': 'What once was lost now is found!'})

#paramaterize SQL queries to protect against SQL injection