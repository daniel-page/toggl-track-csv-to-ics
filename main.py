# https://track.toggl.com/reports/detailed/

import pandas
import icalendar as ical

# from datetime import datetime
# import pytz

cal = ical.Calendar()
cal.add("prodid", "-//My calendar product//example.com//")
cal.add("version", "2.0")

filename = "Toggl_time_entries_2023-06-26_to_2023-07-02.csv"

df = pandas.read_csv(
    filename,
    parse_dates=[
        ["Start date", "Start time"],
        ["End date", "End time"],
    ],  # Should this include timezone?
)
# print(df)

projects = list(df["Project"])
start_dates = list(df["Start date_Start time"])
end_dates = list(df["End date_End time"])
descriptions = list(df["Description"])

for i in range(len(df)):
    # print(projects[i], descriptions[i], start_dates[i], end_dates[i])

    event = ical.Event()
    # event.add("name", projects[i])
    event.add("summary", projects[i])
    event.add("description", "Imported from Toggl Track.")
    event.add("dtstart", start_dates[i])
    event.add("dtend", end_dates[i])
    cal.add_component(event)

f = open("output.ics", "wb")
f.write(cal.to_ical())
f.close()
