GRADE_POINTS = {
    'A': 5.0,
    'B': 4.0,
    'C': 3.0,
    'D': 2.0,
    'E': 1.0,
    'F': 0.0,
}

def calculate_gp(courses):
    total_weight = 0
    total_units = 0
    for course in courses:
        grade_point = GRADE_POINTS.get(course['grade'].upper(), 0)
        units = int(course['units'])
        total_weight += grade_point * units
        total_units += units
    if total_units == 0:
        return 0, 0
    gp = round(total_weight / total_units, 2)
    return gp, total_units