import json
TIMESLOTS = [
    "Monday 09:00",
    "Monday 11:00",
    "Tuesday 09:00",
    "Tuesday 11:00"
]

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
courses = load_json("../data/courses.json")
student_groups = load_json("../data/student_groups.json")
conflict_graph = {}

for course in courses:
    conflict_graph[course["id"]] = []

    CS101: []
    CS102: []
    CS103: []

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):

        course_a = courses[i]
        course_b = courses[j]

        if course_a["professor"] == course_b["professor"]:
            conflict_graph[course_a["id"]].append(course_b["id"])
            conflict_graph[course_b["id"]].append(course_a["id"])
for group in student_groups:
    group_courses = group["courses"]

    for i in range(len(group_courses)):
        for j in range(i + 1, len(group_courses)):

            course_a = group_courses[i]
            course_b = group_courses[j]

            if course_b not in conflict_graph[course_a]:
                conflict_graph[course_a].append(course_b)

            if course_a not in conflict_graph[course_b]:
                conflict_graph[course_b].append(course_a)

        print("\nConflict Graph\n")

        for course, conflicts in conflict_graph.items():
            print(f"{course} conflicts with {conflicts}")

# Welsh-Powell Graph Coloring

sorted_courses = sorted(
    conflict_graph,
    key=lambda course: len(conflict_graph[course]),
    reverse=True
)

color_assignment = {}

for course in sorted_courses:

    used_colors = []

    for conflict in conflict_graph[course]:
        if conflict in color_assignment:
            used_colors.append(color_assignment[conflict])

    color = 0

    while color in used_colors:
        color += 1

    color_assignment[course] = color

    print("\nGraph Coloring Result\n")

    for course, color in color_assignment.items():
        timeslot = TIMESLOTS[color]
        print(f"{course} -> Color {color} -> {timeslot}")

def get_colored_timeslots():
    result = {}

    for course, color in color_assignment.items():
        result[course] = TIMESLOTS[color]

    return result

print("\nFinal Timeslot Assignment\n")

colored_timeslots = get_colored_timeslots()

for course, slot in colored_timeslots.items():
    print(f"{course} -> {slot}")
