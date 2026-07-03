import sched
import time
import threading
import traceback

def print_stack_trace():
    """Prints the current thread name and stack trace."""
    print(f"Thread Name: {threading.current_thread().name}")
    print("Stack Trace:")
    for line in traceback.format_stack():
        print(line.strip())

def callback():
    print("Scheduler callback executed!")
    print_stack_trace()

scheduler = sched.scheduler(time.time, time.sleep) # Eta synonymous to mapper
scheduler.enter(10, 5, callback)  # Schedule callback after 5 seconds # synonymous to reducer
print("Main thread details before scheduler.run():")
print_stack_trace()
scheduler.run()
