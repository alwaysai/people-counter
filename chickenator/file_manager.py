
import json
import os
import pickle


def load(path, default):
    try:
        with open(path, "rb") as f:
            print("file_manager.py: load: loading object from file: {}".format(path))
            result = pickle.load(f)
    except Exception:
        result = default
        # If wanting to auto write default file
        # with open(path, "wb") as f:
        #     print(
        #         "file_manager.py: load: initializing new object to path: {}".format(path))
        #     pickle.dump(result, f)
    return result


def save(object, path):
    with open(path, 'wb') as output:  # Overwrites any existing file.
        print("file_manager.py: saved object to path: {}".format(path))
        pickle.dump(object, output, pickle.HIGHEST_PROTOCOL)


def loadJSON(path, default):
    try:
        with open(path, "rb") as data:
            print("file_manager.py: loadJSON: loading JSON from file: {}".format(path))
            result = json.load(data)
    except Exception:
        result = default
    return result


def saveJSON(object, path):
    with open(path, 'wb') as f:
        print("file_manager.py: saved JSON object to path: {}".format(path))
        json.dump(object, f)
