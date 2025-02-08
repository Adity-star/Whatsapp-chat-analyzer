import re
import pandas as pd


def preprocess(data):

    pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}),\s*(\d{1,2}:\d{2}\s*[APap][Mm])\s*-\s*([^:]+):\s*(.*)"

    data  = data.replace("\u202f", " ")

    messages = re.findall(pattern, data)[1:]
    dates = re.findall(pattern,data)

    df = pd.DataFrame(messages, columns=["date", "time", "sender", "message"])

    df["date"] = pd.to_datetime(df["date"], format="%m/%d/%y", errors="coerce")

    df["datetime"] = df["date"].dt.strftime("%Y-%m-%d") + " " + df["time"]
    df["datetime"] = pd.to_datetime(df["datetime"], format="%Y-%m-%d %I:%M %p", errors="coerce")
    df['datetime'] = df['datetime'].dt.strftime("%Y-%m-%d %I:%M %p")
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')


    df = df.drop(columns=['date', 'time'])

    df['only_date'] = df['datetime'].dt.date
    df['year'] = df['datetime'].dt.year
    df['month_num'] = df['datetime'].dt.month
    df['month'] = df['datetime'].dt.month_name()
    df['day'] = df['datetime'].dt.day
    df['day_name'] = df['datetime'].dt.day_name()
    df['hour'] = df['datetime'].dt.hour
    df['minute'] = df['datetime'].dt.minute

    df = df[['datetime', 'sender', 'message', 'year', 'month', 'day', 'hour', 'minute','month_num','day_name','only_date']]

    period = []

    for hour in df['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df