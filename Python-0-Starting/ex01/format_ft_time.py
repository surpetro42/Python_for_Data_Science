import time, datetime

# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
print(time.time())
print(f"Seconds since January 1, 1970: {time.time():.4e} or {time.time():.2e} in scientific notation")
now = datetime.datetime.now()
print(f"{now.strftime("%d, %b, %Y")}")