import time, datetime

time.time()
print(f"Seconds since January 1, 1970: {time.time():,.4f} or {time.time():.2e} in scientific notation")
now = datetime.datetime.now()
print(f"{now.strftime("%b %d %Y")}")
