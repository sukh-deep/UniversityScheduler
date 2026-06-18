import json

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

courses = load_json("../data/courses.json")
rooms = load_json("../data/rooms.json")

# Example safe timeslots from Stage 2
colored_timeslots = {
    "CS101": "Monday 09:00",
    "CS102": "Monday 11:00",
    "CS103": "Tuesday 09:00",
    "CS104": "Monday 09:00",
    "CS105": "Monday 09:00",
    "CS106": "Monday 11:00",
    "CS107": "Tuesday 09:00",
    "CS108": "Tuesday 11:00",
    "CS109": "Monday 11:00",
    "CS110": "Tuesday 09:00"
}

optimized_schedule = []
room_usage = {}

for course in courses:

    course_id = course["id"]
    assigned_slot = colored_timeslots[course_id]

    best_room = None
    lowest_waste = None

    for room in rooms:

        room_key = (room["room_id"], assigned_slot)

        if room_key not in room_usage and room["capacity"] >= course["students"]:

            waste = room["capacity"] - course["students"]

            if lowest_waste is None or waste < lowest_waste:
                lowest_waste = waste
                best_room = room

    if best_room is not None:
        room_usage[(best_room["room_id"], assigned_slot)] = True

        optimized_schedule.append({
            "course": course_id,
            "time": assigned_slot,
            "room": best_room["room_id"],
            "students": course["students"],
            "capacity": best_room["capacity"],
            "wasted_seats": lowest_waste
        })

    else:
        optimized_schedule.append({
            "course": course_id,
            "time": assigned_slot,
            "room": "N/A",
            "students": course["students"],
            "capacity": "N/A",
            "wasted_seats": "N/A"
        })

print("\nRoom Optimization Result\n")

for item in optimized_schedule:
    if item["room"] == "N/A":
        print(f"Unscheduled {item['course']} | No suitable room")
    else:
        print(
            f"{item['course']} | {item['time']} | "
            f"{item['room']} | Waste: {item['wasted_seats']} seats"
        )