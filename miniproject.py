import sys
import time
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: python task_timer.py <task_name>")
    input("Press Enter...")
    sys.exit()

task = sys.argv[1]

start = datetime.now()
print("Task:", task)
print("Start time:", start.strftime("%d-%m-%Y %H:%M:%S"))

print("\nWorking... Press Enter when finished")
input()

end = datetime.now()
duration = end - start

print("\nEnd time:", end.strftime("%d-%m-%Y %H:%M:%S"))
print("Time spent:", duration)

input("\nPress Enter to exit...")
