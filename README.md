# Advance-Process-Manager Project Report

## Table of Contents
- [Installation](#installation)
- [Introduction](#introduction)
- [Functionalities](#functionalities)
- [Test Results](#test-results)
- [Discussion](#discussion)

## Installation

### Clone the repository to your local machine using the following Git command:
```bash 
git clone <repository_url> 
```

### Install the required dependencies using the following command:
```bash 
pip install -r requirements.txt 
```

### Run the Process Manager using the following command:
```bash 
python3 main.py
```

## Introduction
The goal of this project is to design and implement an advanced Process Manager with an emphasis on process synchronization. This Process Manager will allow users to create, manage, and synchronize processes in a multi-threaded environment. It will provide a command-line interface for process creation, management, and synchronization, and it will use system calls for process and thread control.

## Functionalities 

The Process Manager project includes the following functionalities:
- Process Creation
- Process Management
- Thread Support
- Inter-Process Communication (IPC)
- Process Synchronization
- Command-Line Interface (CLI) for user interaction
- Logging and Reporting

### Process Creation
- Implements a process creation mechanism using system calls (e.g., fork, exec) to allow users to create new processes.

### Process Management
- Provides functionalities to list, terminate, and monitor running processes.
- Allows users to view information about each process, such as its process ID (PID), parent process ID, and state.

### Thread Support
- Extends the Process Manager to support multiple threads within a process.
- Implements thread creation, termination, and synchronization mechanisms.
- Uses system calls for thread creation (e.g., pthread_create) and synchronization (e.g., mutexes, semaphores).

### Inter-Process Communication (IPC)
- Implements IPC mechanisms to allow processes and threads to communicate and share data.
- Supports methods like message passing, shared memory, or pipes for IPC.
- Uses system calls for IPC operations (e.g., pipe, msgget, shmget).

### Process Synchronization
- Implements synchronization primitives such as mutexes and semaphores.
- Demonstrates the use of synchronization mechanisms to solve common synchronization problems (e.g., producer-consumer).

### Command-Line Interface (CLI)
- Provides a user-friendly interface for interacting with the Process Manager.
- Allows users to create processes, create threads, synchronize threads, and perform IPC operations.
- Offers clear and informative command syntax and options.

### Logging and Reporting
- Implements logging and reporting features to track and display the execution of processes and threads.
- Logs significant events, errors, and information related to process synchronization.

## Test Results
### Create Process
These screenshots demonstrates the creation of a new process. Users can input a process name, and the Process Manager successfully creates a new process with the provided name and assigns a unique Process ID (PID). Within the process, users can create threads, and list them. The Process Manager also logs the creation of the process and threads of the process in the Process Manager.log file.

![Alt text](/imgs/image-0.png)
![Alt text](/imgs/image.png)
![Alt text](/imgs/image-1.png)

### List Processes
In this screenshot, the "List Processes" functionality is showcased. It displays process made by user, list of all running processes on your PC, including their PID, parent PID, name, and status. Users can easily monitor the running processes.
![Alt text](/imgs/image-2.png)
![Alt text](/imgs/image-3.png)

### Create Thread
This image illustrates the creation of a new thread within a process. Users can specify a thread name, and the Process Manager creates a new thread successfully.
![Alt text](/imgs/image-4.png)

### Terminate Thread
In this screenshot, the termination of a thread is demonstrated. Users can provide the thread name, and the Process Manager requests the termination of the specified thread, followed by a successful termination message. 
![Alt text](/imgs/image-5.png)

### IPC: Send Message
This section showcases the inter-process communication (IPC) feature. Users can send a message using IPC, and the Process Manager delivers the message successfully.
![Alt text](/imgs/image-6.png)
![Alt text](/imgs/image-7.png)

### IPC: Receive Message
Here, the Process Manager demonstrates the capability to receive messages through IPC. It displays the received messages from the log file, allowing users to retrieve and view them.

![Alt text](/imgs/image-8.png)

### Process Synchronization
The screenshot presents the demonstration of process synchronization using multiprocessing. It shows the producer-consumer pattern, where items are produced and consumed with synchronization. The Process Manager logs the synchronization events in the Process Manager.log file.
![Alt text](/imgs/image-9.png)

## Process Manager.log file
The screenshot below shows the Process Manager.log file, which logs all the events, errors, and information related to process synchronization.
![Alt text](/imgs/image-10.png)