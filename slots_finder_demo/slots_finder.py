import pandas

meetings = []
persons = []
duration_of_meeting = 60


def reading_csv_file(csv_path):
    df = pandas.read_csv(csv_path)
    tmp_meetings_for_person = []
    for index, row in df.iterrows():
        if row['Person name'] in persons:
            start_time = row['Event start time']
            start_time = start_time.replace(':', '')
            start_meeting_int = int(start_time)

            end_time = row['Event end time']
            end_time = end_time.replace(':', '')
            end_meeting_int = int(end_time)
            tmp_meetings_for_person.append((start_meeting_int, end_meeting_int))

        else:
            if tmp_meetings_for_person:
                meetings.append(tmp_meetings_for_person)

            persons.append(row['Person name'])
            tmp_meetings_for_person = []
            start_time = row['Event start time']
            start_time = start_time.replace(':', '')
            start_meeting_int = int(start_time)

            end_time = row['Event end time']
            end_time = end_time.replace(':', '')
            end_meeting_int = int(end_time)
            tmp_meetings_for_person.append((start_meeting_int, end_meeting_int))
    if tmp_meetings_for_person:
        meetings.append(tmp_meetings_for_person)


def get_meetings_free_slots(list_of_meetings):
    busy = {t for meets in list_of_meetings
            for start, end in meets
            for t in range(start - start // 100 * 40, end - end // 100 * 40)}

    free = [t not in busy for t in range(1440)]
    breaks = [i for i, (a, b) in enumerate(zip(free, free[1:]), 1) if b != a]
    result = [(s, e) for s, e in zip([420] + breaks, breaks + [1140]) if free[s]]
    return [(s + s // 60 * 40, e + e // 60 * 40) for s, e in result]


def clean_meetings_slots_by_duration(optionals_meetings_slots, duration_with_minutes):
    fixed_meetings_slots_after = []
    for slot in optionals_meetings_slots:
        free_time_period_in_min_base_60 = (slot[1] - slot[1] // 100 * 40) - (slot[0] - slot[0] // 100 * 40)

        if free_time_period_in_min_base_60 >= duration_with_minutes:
            fixed_meetings_slots_after.append(slot)

    return fixed_meetings_slots_after


reading_csv_file('calendar.csv')
optional_meetings_slots_without_meeting_duration = get_meetings_free_slots(meetings)
fixed_meetings_slots = clean_meetings_slots_by_duration(optional_meetings_slots_without_meeting_duration,
                                                        duration_of_meeting)
open_slots_optionals_final = ["-".join(f"{t // 100:02}:{t % 100:02}" for t in slot)
                              for slot in fixed_meetings_slots]

print("Free Time:")
print(*open_slots_optionals_final, sep="\n")
print('')
print("Optional Starting Meetings:")
for slot in open_slots_optionals_final:
    print(f"Available slot: {slot[:5]}")
