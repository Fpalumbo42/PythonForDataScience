import time
from datetime import datetime

current_time = time.time()
scientific_notation = f"{current_time:.2e}"
formatted_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {current_time:,.4f} or {scientific_notation} in scientific notation$")
print(f"{formatted_date}$")
