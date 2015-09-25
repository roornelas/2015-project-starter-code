from app import db, models, app
from flask import request


@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'

@app.route('/health', methods=['GET'])
def health():
    return 'OK!', 200

@app.route('/coordinates', methods=['POST'])
def coordinates():
    content = request.get_json(force=True)
    coors = content['coordinates']
    print coors
    for coor in coors:
        print coor
        db.session.add(models.Coordinates(coor["latitude"], coor["longitude"], coor["notes"]))
    db.session.commit()
    return 'OK 12' , 200


