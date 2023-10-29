import os
import logging
import multiprocessing
import psutil
import ctypes
import ctypes.util
import sys

logging.basicConfig(filename='process_manager.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')
process_log = logging.getLogger('processes')
process_log.setLevel(logging.INFO)

shared_queue = multiprocessing.Queue()
mutex = multiprocessing.Lock()
process_threads = {}
threads = []

choices = {
    "1": "Create Process",
    "2": "List Processes",
    "3": "Create Thread",
    "4": "Terminate Thread",
    "5": "IPC: Send Message",
    "6": "IPC: Recieve Message",
    "7": "Process Synchronization",
    "8": "Exit"
}


def create_process(process_name):
    pid = os.fork()
    if pid == 0:
        try:
            pass
        except Exception as e:
            logging.error(
                f"Child process '{process_name}' with PID {os.getpid()} encountered an error: {str(e)}")
        os._exit(0)
    else:
        logging.info(f"Child process '{process_name}' with PID {pid} created.")
        process_function(process_name)


def list_processes():
    process_log.info("List of running processes:")
    processes = psutil.process_iter(attrs=['pid', 'ppid', 'name', 'status'])
    for process_info in processes:
        pid = process_info['pid']
        ppid = process_info['ppid']
        name = process_info['name']
        status = process_info['status']
        process_log.info(
            f"Process with PID: {pid}, Parent PID: {ppid}, Name: {name}, Status: {status}")
        print(
            f"Process with PID: {pid}, Parent PID: {ppid}, Name: {name}, Status: {status}")
    print('\n')


def process_function(process_name):
    process_log.info(
        f"Child process '{process_name}' with PID {os.getpid()} running")
    process_threads[os.getpid()] = []

    while True:
        print("Options within the process:")
        print("1. Create a thread")
        print("2. List threads")
        print("3. Exit process")
        choice = input("Select an option: ")

        if choice == "1":
            thread_name = input("Enter a name for the thread: ")
            create_thread(thread_name)
            print('\n')
        elif choice == "2":
            list_threads()
            print('\n')
        elif choice == "3":
            print("Exited process.")
            print('\n')
            break
        else:
            print("Invalid option. Try again.")
    return


def create_thread(thread_name):
    process_pid = os.getpid()
    thread_id = ctypes.c_long()

    def thread_function():
        logging.info(f"Thread '{thread_name}' running")

    thread_func_pointer = ctypes.CFUNCTYPE(None)(thread_function)
    libc = ctypes.CDLL(ctypes.util.find_library('c'))

    if libc.pthread_create(ctypes.byref(thread_id), None, thread_func_pointer, None) == 0:
        threads.append((thread_id, thread_name))
        process_threads.setdefault(process_pid, []).append(
            (thread_id, thread_name))
        logging.info(f"Thread '{thread_name}' created successfully")
    else:
        logging.error("Failed to create thread")


def list_threads():
    process_pid = os.getpid()
    threads = process_threads.get(process_pid, [])

    if not threads:
        print("No threads in this process.")
    else:
        print("Threads in this process:")
        for thread_id, thread_name in threads:
            print(f"Thread ID: {thread_id}, Name: {thread_name}")


def terminate_thread(thread_name):
    global threads
    threads_to_remove = []

    process_pid = os.getpid()
    libc = ctypes.CDLL(ctypes.util.find_library('c'))

    for thread_id, name in process_threads.get(process_pid, []):
        if name == thread_name:
            if libc.pthread_cancel(thread_id) == 0:
                print(f"Thread '{thread_name}' termination requested.")
                logging.info(f"Thread '{thread_name}' termination requested.")
                threads_to_remove.append((thread_id, name))
            else:
                logging.error(
                    f"Failed to request termination for thread '{thread_name}'")

    for thread_id, name in threads_to_remove:
        if libc.pthread_join(thread_id, None) == 0:
            print(f"Thread '{name}' terminated.")
            logging.info(f"Thread '{name}' terminated.")
    threads = [(t, n) for t, n in threads if (t, n) not in threads_to_remove]


def ipc_send_message(message):
    with multiprocessing.Lock():
        # Using a multiprocessing.Pipe for IPC
        parent_conn, child_conn = multiprocessing.Pipe()
        child_conn.send(message)
        print(f"Message sent over IPC: {message}")
        logging.info(f"Message sent over IPC: {message}")


def ipc_receive_message():
    log_file_path = 'process_manager.log'
    received_messages = []

    if not os.path.exists(log_file_path):
        return ["Log file not found"]

    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()
        for line in lines:
            if "Message sent over IPC: " in line:
                message = line.split("Message sent over IPC: ")[1].strip()
                received_messages.append(message)

    if received_messages:
        return received_messages
    else:
        return ["No message available"]


def process_synchronization():

    print("Demonstrating process synchronization using multiprocessing:")

    logging.info(
        "Demonstrating process synchronization using multiprocessing:")

    # Producer function
    def producer(q):
        for item in range(5):
            q.put(item)
            print(f"Producing item {item}")
            logging.info(f"Producing item {item}")

    # Consumer function
    def consumer(q):
        for item in iter(q.get, None):
            print(f"Consuming item {item}")
            logging.info(f"Consuming item {item}")

    q = multiprocessing.Queue()
    producer_process = multiprocessing.Process(target=producer, args=(q,))
    consumer_process = multiprocessing.Process(target=consumer, args=(q,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()

    q.put(None)

    consumer_process.join()

    print("Process synchronization demonstration complete.")
    logging.info("Process synchronization demonstration complete.")


def main():
    while True:

        print("Options:")
        for key, value in choices.items():
            print(f"{key}) {value}")

        choice = input("Enter choice: ")

        if choice == "1":
            process_name = input("Enter process name: ")
            create_process(process_name)

        elif choice == "2":
            list_processes()

        elif choice == "3":
            thread_name = input("Enter thread name: ")
            create_thread(thread_name)

        elif choice == "4":
            thread_name = input("Enter thread name: ")
            terminate_thread(thread_name)

        elif choice == "5":
            message = input("Enter message: ")
            ipc_send_message(message)

        elif choice == "6":
            received_messages = ipc_receive_message()
            if received_messages:
                print('\nReceived messages:')
                for message in received_messages:
                    print(f"- {message}")
            else:
                print("No messages received.")
            print('\n')

        elif choice == "7":
            process_synchronization()

        elif choice == "8":
            print("Exited successfully")
            sys.exit(0)

        else:
            print("Invalid option. Try again.", '\n')


if __name__ == "__main__":
    main()  # Call main function
