from datetime import datetime, date, time, timedelta, timezone

# NOW & TODAY

print(date.today())
print(datetime.now())

# CREATING DATES AND TIMES

d = date(2026, 5, 26)
t = time(14, 30, 45)
dt = datetime(2026, 5, 26, 14, 30, 45)

print(d)
print(t)
print(dt)

# ACCESSING PARTS

now = datetime.now()
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
print(now.weekday())  # 0 = Monday, 6 = Sunday

# FORMATTING (date -> string)

dt = datetime(2026, 5, 26, 14, 30)
print(dt.strftime("%Y-%m-%d"))  # 2026-05-26
print(dt.strftime("%d/%m/%Y"))  # 26/05/2026
print(dt.strftime("%B %d, %Y"))  # May 26, 2026
print(dt.strftime("%H:%M"))  # 14:30
print(dt.strftime("%I:%M %p"))  # 02:30 PM

# PARSING (string -> date)

parsed = datetime.strptime("2026-05-26", "%Y-%m-%d")
print(parsed)

# ISO FORMAT (preferred for APIs)

now = datetime.now()
print(now.isoformat())
print(datetime.fromisoformat("2026-05-26T14:30:00"))

# TIMEDELTA (date arithmetic)

today = date.today()
print(today + timedelta(days=1))  # tomorrow
print(today - timedelta(days=1))  # yesterday
print(today + timedelta(weeks=2))  # 2 weeks later

# DIFFERENCE BETWEEN DATES

start = date(2026, 1, 1)
end = date(2026, 5, 26)
diff = end - start
print(diff.days, "days")

# TIMEZONES WITH ZONE INFO (Python 3.9+)

from zoneinfo import ZoneInfo

utc_now = datetime.now(ZoneInfo("UTC"))
ist_now = utc_now.astimezone(ZoneInfo("Asia/Kolkata"))
ny_now = utc_now.astimezone(ZoneInfo("America/New_York"))

print(utc_now.strftime("%H:%M %Z"))
print(ist_now.strftime("%H:%M %Z"))
print(ny_now.strftime("%H:%M %Z"))

# UNIX TIMESTAMP

now = datetime.now(timezone.utc)
ts = now.timestamp()
print(ts)
print(datetime.fromtimestamp(ts, tz=timezone.utc))
