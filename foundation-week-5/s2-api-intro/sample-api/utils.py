def search_flight(fid, flights):
    return [element for element in flights if element['flight_id'] == fid]


def get_index(fid, flights):
    for i, flight in enumerate(flights):
        if flight['flight_id'] == fid:
            return i
    return -1
