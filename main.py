import os
import sys
import threading
import time
import multiprocessing
import logging
import psutil
import signal


logging.basicConfig(filename='process_manager.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

previous_choice = None
result = ""
running_processes = {}

choices = {
    "1": "Create Process",
    "2": "List Processes",
    "3": "Create Thread",
    "4": "IPC: Send Message",
    "5": "Process Synchronization",
    "6": "Exit"
}


def create_process(process_name, command):
    pid = os.fork()
    if pid == 0:
        try:
            os.execlp(command, command)
        except Exception as e:
            logging.error(f"Child process failed: {e}")
            print(f"Child process failed: {e}")
        os._exit(1)
    else:
        running_processes[pid] = process_name
        print(f"Process {process_name} created with PID {pid}")


def terminate_process(process_pid):
    try:
        os.kill(process_pid, signal.SIGTERM)
        del running_processes[process_pid]
        print(f"Terminated process with PID {process_pid}.")
    except ProcessLookupError:
        print(f"Process {process_pid} not found.")


def list_processes():
    print("List of running processes:")

    for proc in psutil.process_iter(attrs=['pid', 'name', 'status']):
        process_info = proc.info
        print(
            f"Process with PID: {process_info['pid']}, Name: {process_info['name']}, Status: {process_info['status']}")

    logging.info("List of running processes:")

    for proc in psutil.process_iter(attrs=['pid', 'name', 'status']):
        process_info = proc.info
        logging.info(
            f"Process with PID: {process_info['pid']}, Name: {process_info['name']}, Status: {process_info['status']}")


def create_thread(thread_name):
    thread = threading.Thread(target=thread_function, args=(thread_name,))
    thread.start()
    print(f"Thread '{thread_name}' started.")


def thread_function(thread_name):

    print(f"Thread '{thread_name}' running.")

    time.sleep(2)

    print(f"Thread '{thread_name}' finished.")

    logging.info(f"Thread '{thread_name}' running.")

    time.sleep(2)

    logging.info(f"Thread '{thread_name}' finished.")


def ipc_message_passing(message):
    print(f"Message received: {message}")
    logging.info(f"Message received: {message}")


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


if __name__ == '__main__':
    while True:

        print("Options:")
        for key, value in choices.items():
            print(f"{key}) {value}")

        choice = input("Enter choice: ")

        if choice == "6":
            break

        if choice == "1":
            process_name = input("Enter process name: ")
            command = input("Enter command: ")
            create_process(process_name, command)

        elif choice == "2":
            list_processes()

        elif choice == "3":
            thread_name = input("Enter thread name: ")
            create_thread(thread_name)

        elif choice == "4":
            message = input("Enter message: ")
            ipc_message_passing(message)

        elif choice == "5":
            process_synchronization()

        elif choice == "6":
            print("Exited successfully")
            exit(0)
