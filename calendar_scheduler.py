def select_events(events):
    events.sort(key=lambda x: x[1])  # Sort by end time

    selected = []
    last_end_time = 0

    for start, end in events:
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end

    return selected

events = [(1, 3), (2, 4), (3, 5), (5, 7), (8, 9)]

print("Events:", events)
print("Selected Events:", select_events(events))