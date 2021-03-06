from gtfs_util import constants
from gtfs_util.static.models import (
    FILENAME_MODEL_MAPPING,
    agency,
    service,
    service_update,
    route,
    point,
    stop_time,
    stop,
    transfer,
    trip,
)


def to_model(raw_data):
    data = {}

    for k, v in raw_data:
        model = FILENAME_MODEL_MAPPING[k]
        data[k] = [model(x) for x in v]

    return data


def to_json(raw_data):
    raise NotImplementedError()
