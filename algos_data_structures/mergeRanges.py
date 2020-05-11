
def mergeRanges(meetings):
    # Sort meetings
    sorted_meetings = sorted(meetings)
    # print(sorted_meetings)

    # Initialize merged meetings with earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))   


    return merged_meetings

# Should return   [(0, 1), (3, 8), (9, 12)]
print(mergeRanges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))