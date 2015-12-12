from flask import Flask, jsonify, render_template
from flask.ext.pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.debug = True

app.config.update(MONGO_DBNAME = 'items')
mongo = PyMongo(app)

@app.route('/')
def home_page():
    venues = mongo.db.venues.find()
    return render_template('index.html')

@app.route('/venues')
def venues():
    venues = mongo.db.venues.find({ 'lat': { '$exists': True }})
    to_return = []
    for venue in venues:
        to_return.append(json_util.dumps(venue, default=json_util.default))
    return jsonify({ 'venues': to_return })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
