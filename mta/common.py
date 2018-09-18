from csv import DictReader


class Stop(namedtuple(
    'Stop',
    [
        'id',
        'code',
        'name',
        'description',
        'latitude',
        'longitude',
        'zone_id',
        'url',
        'location_type',
        'parent_station',
    ],
)):
    MAPPING = {
        'id': 'stop_id',
        'code': 'stop_code',
        'name': 'stop_name',
        'description': 'stop_desc',
        'latitude': 'stop_lat',
        'longitude': 'stop_lon',
        'zone_id': 'zone_id',
        'url': 'stop_url',
        'location_type': 'location_type',
        'parent_station': 'parent_station',
    }


def parse_stops(filename):
    with open(filename, 'r') as file:
        reader = DictReader(file)
        return {
            row['stop_id']: Stop(**{
                k: row[v] for k, v in Stop.MAPPING.items()
            }) for row in reader
        }


class StopTime(namedtuple(
    'StopTime',
    [
        'id',
        'arrival_time',
        'departure_time',
        'stop_id',
        'stop_sequence',
        'stop_headsign',
        'pickup_type',
        'drop_off_type',
        'shape_dist_traveled',
    ],
)):
    MAPPING = {
        'id': 'trip_id',
        'arrival_time': 'arrival_time',
        'departure_time': 'departure_time',
        'stop_id': 'stop_id',
        'stop_sequence': 'stop_sequence',
        'stop_headsign': 'stop_headsign',
        'pickup_type': 'pickup_type',
        'drop_off_type': 'drop_off_type',
        'shape_dist_traveled': 'shape_dist_traveled',
    }


class Route(namedtuple(
    'Route',
    [
        'id',
        'agency_id',
        'short_name',
        'long_name',
        'description',
        'type',
        'url',
        'color',
        'text_color',
    ],
)):
    MAPPING = {
        'id': 'route_id',
        'agency_id': 'agency_id':
        'short_name': 'route_short_name',
        'long_name': 'route_long_name',
        'description': 'route_desc',
        'type': 'route_type',
        'url': 'route_url',
        'color': 'route_color',
        'text_color': 'route_text_color',
    }


def parse_routes(filename):
    with open(filename, 'r') as file:
        reader = DictReader(file)
        return {
            row['route_id']: Route(**{
                k: row[v] for k, v in Route.MAPPING.items()
            }) for row in reader
        }
