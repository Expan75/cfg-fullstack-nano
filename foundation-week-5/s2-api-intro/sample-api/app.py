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


@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    print('the id passed to get_flight_by_id:', id)
    flight = search_flight(id, flights)
    return jsonify(flight)


@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()
    print("before added new, flights len(): ", len(flights))
    flights.append(flight)
    print("before added new, flights len(): ", len(flights))
    return flight


@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight_to_update = request.get_json()
    index = get_index(id, flights)
    print('flight before update: ', flights[index])
    flights[index] = flight_to_update
    print('flight after update: ', flights[index])
    return jsonify(flights[index])


@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    index = get_index(id, flights)
    deleted = flights.pop(index)
    return jsonify(deleted), 200

if __name__ == '__main__':
    app.run(debug=True)