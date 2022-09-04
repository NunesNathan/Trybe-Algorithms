from types import NoneType


def study_schedule(permanence_period, target_time):
    if isinstance(target_time, NoneType):
        return None
    logons = int()
    for (login, logout) in permanence_period:
        if not isinstance(login, int) or not isinstance(logout, int):
            return None
        if target_time in range(login, logout + 1):
            logons += 1

    return logons
