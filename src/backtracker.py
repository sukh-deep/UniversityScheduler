import json

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

courses = load_json("../data/courses.json")
rooms = load_json("../data/rooms.json")
professors = load_json("../data/professors.json")

TIMESLOTS = [
    "Monday 09:00",
    "Monday 11:00",
    "Tuesday 09:00",
    "Tuesday 11:00",
    "Monday 8:30",
    "Thursday 11:00",
    "Wednesday 09:00"
]

def assign_course(index, courses, schedule, room_usage):

    if index == len(courses):
        return True

    course = courses[index]

    professor = next(
        p for p in professors
        if p["id"] == course["professor"]
    )

    for slot in TIMESLOTS:

        for room in rooms:

            if room["capacity"] >= course["students"] and slot in professor["availability"]:

                key = (room["room_id"], slot)

                if key not in room_usage:

                    schedule.append({
                        "course": course["id"],
                        "room": room["room_id"],
                        "timeslot": slot
                    })

                    room_usage[key] = True

                    if assign_course(
                        index + 1,
                        courses,
                        schedule,
                        room_usage
                    ):
                        return True

                    schedule.pop()
                    del room_usage[key]

    return False

schedule = []
room_usage = {}

success = assign_course(
    0,
    courses,
    schedule,
    room_usage
)

print("\nBacktracking Result\n")

if success:

    for item in schedule:

        print(
            f"{item['course']} | "
            f"{item['timeslot']} | "
            f"{item['room']}"
        )

else:

    print("No complete schedule found")
