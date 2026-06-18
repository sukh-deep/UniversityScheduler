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
rooms = load_json("../data/rooms.json")
professors = load_json("../data/professors.json")

courses.sort(
    key=lambda x: x["students"],
    reverse=True
)

schedule = []
room_usage = {}

for course in courses:

    assigned = False

    for slot in TIMESLOTS:

        for room in rooms:

            professor = next(
                p for p in professors
                if p["id"] == course["professor"]
            )

            if room["capacity"] >= course["students"] and slot in professor["availability"]:

                key = (room["room_id"], slot)

                if key not in room_usage:

                    schedule.append({
                        "course": course["id"],
                        "students": course["students"],
                        "room": room["room_id"],
                        "capacity": room["capacity"],
                        "timeslot": slot,
                        "wasted_seats": room["capacity"] - course["students"]
                    })

                    room_usage[key] = True
                    assigned = True
                    break

        if assigned:
            break

    if not assigned:
        schedule.append({
            "course": course["id"],
            "students": course["students"],
            "room": "N/A",
            "capacity": "N/A",
            "timeslot": "N/A",
            "wasted_seats": "N/A",
            "status": "Unscheduled"
        })

print("\n" + "=" * 70)
print("GREEDY SCHEDULING RESULTS")
print("=" * 70)

for item in schedule:

    if item["room"] == "N/A":

        print(
            f"❌ {item['course']} could not be scheduled"
        )

    else:

        print(
            f"✅ Course: {item['course']}"
            f" | Time: {item['timeslot']}"
            f" | Room: {item['room']}"
            f" | Waste: {item['wasted_seats']} seats"
        )

print("=" * 70)