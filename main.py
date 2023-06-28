import pandas

filename = "Toggl_time_entries_2023-06-26_to_2023-07-02.csv"

df = pandas.read_csv(
    filename,
    parse_dates=[["Start date", "Start time"], ["End date", "End time"]],
)
# print(df)

projects = list(df["Project"])
start_dates = list(df["Start date_Start time"])
end_dates = list(df["End date_End time"])
descriptions = list(df["Description"])

for i in range(len(df)):
    print(projects[i], descriptions[i], start_dates[i], end_dates[i])
