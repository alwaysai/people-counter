import time

# { object_id : time }
ALL_USERS = {}
START = int(time.time())


def newLoop():
    global ACTIVE_IDs
    global START
    ACTIVE_IDs = []
    START = int(time.time())


def currentTimeFromStart():
    global START
    now = int(time.time())
    elapsed = now - START
    return elapsed


def addTimeFor(objectId):
    global ACTIVE_IDs
    global ALL_USERS
    elapsed = currentTimeFromStart()
    if not objectId in ALL_USERS:
        ALL_USERS[objectId] = elapsed
    else:
        ALL_USERS[objectId] += elapsed


def timeForId(objectId):
    return ALL_USERS[objectId]


def currentMetrics():
    global ALL_USERS
    times = []
    for _, time in ALL_USERS.items():
        times.append(time)
    if len(times) == 0:
        times.append(0)
    return {
        "min": min(times),
        "max": max(times),
        "avg": sum(times) / len(times),
        "total": sum(times),
        "count": len(ALL_USERS.items())
    }
