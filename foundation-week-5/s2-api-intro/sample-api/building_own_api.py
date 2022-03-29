from flask import Flask, jsonify, request
from flights_data import flights
from utils import search_flight, get_index

app = Flask(__name__)


# GETTING INFORMATION

@app.route('/')
def hello():
    return {'hello': 'Universe'}


@app.route('/flights')
def get_flights():
    return jsonify(flights)

# http://127.0.0.1:5000/flights


@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    flight = search_flight(id, flights)
    return jsonify(flight)

# http://127.0.0.1:5000/flights/555


# ADDING NEW FLIGHTS

@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()
    flights.append(flight)
    return flight


# UPDATING A FLIGHT


@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight_to_update = request.get_json()
    index = get_index(id, flights)
    flights[index] = flight_to_update
    return jsonify(flights[index])


# DELETING A FLIGHT


@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    index = get_index(id, flights)
    deleted = flights.pop(index)
    return jsonify(deleted), 200


if __name__ == '__main__':
    app.run(debug=True)
