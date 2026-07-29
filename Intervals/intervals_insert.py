def insert_interval(intervals, newInterval):

    answer = []

    for current in intervals:

        # Current interval is before new interval
        if current[1] < newInterval[0]:
            answer.append(current)

        # Current interval is after new interval
        elif current[0] > newInterval[1]:
            answer.append(newInterval)
            newInterval = current

        # Overlapping intervals
        else:
            newInterval[0] = min(newInterval[0], current[0])
            newInterval[1] = max(newInterval[1], current[1])

    answer.append(newInterval)

    return answer


intervals = [[1,3],[6,9]]
newInterval = [2,5]

print(insert_interval(intervals, newInterval))