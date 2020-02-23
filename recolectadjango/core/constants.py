
USER_TYPES = (
    ('waste_disposer', 'Waste Disposer'),
    ('waste_collector', 'Waste Collector'),
)

WORKING_TIMES = (
    ('morning', 'Mañana (6AM a 12M)'),
    ('afternoon', 'Tarde (12M a 6PM)'),
    ('night', 'Noche (6PM a 1AM)'),
    ('unavailable', 'No disponible'),
)

WEEKDAYS = (
    ('monday', 'Lunes'),
    ('tuesday', 'Martes'),
    ('wednesday', 'Miercoles'),
    ('thursday', 'Jueves'),
    ('friday', 'Viernes'),
    ('saturday', 'Sábado'),
    ('sunday', 'Domingo'),
)

PICKUP_TIMES = tuple(
    (f"{day[0]}_{wt[0]}", f"{day[1]} {wt[1]}")
    for day in WEEKDAYS for wt in WORKING_TIMES
    if wt[0] in ('morning', 'afternoon', 'night')
)
