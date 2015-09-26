from app import db, models, app
from flask import request, render_template


@app.route('/', methods=['GET'])
def index():
    print models.Coordinates.query.all()
    return render_template('map_frontend.html', coordinates = models.Coordinates.query.all())

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


