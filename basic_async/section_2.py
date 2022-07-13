import threading

def hello_world():
    print(f"Hello world from {threading.current_thread()}")

hello_thread = threading.Thread(target=hello_world)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name


print(f'Python is currently running {total_threads} thread(s)')
print(f'The current thread is {thread_name}')
hello_thread.join()