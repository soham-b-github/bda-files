import threading
import time
import traceback

# Define an inner function to print the stack trace
def inner_function(name):
    print(f"Stack trace from inner_function of thread {name}:")
    traceback.print_stack()

# Define the thread function
def print_numbers(name, delay, count):
    for i in range(1, count + 1):
        time.sleep(delay)
        print(f"Thread {name}: {i}")
    # Call the inner function to print the stack trace
    inner_function(name)

# Create two threads
thread1 = threading.Thread(target=print_numbers, args=("A", 1, 5))
thread2 = threading.Thread(target=print_numbers, args=("B", 0.5, 5))

# Start the threads
print("Starting threads...")
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Threads completed!")
