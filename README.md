# Advance-Process-Manager Project Report
# Due date : 10/29/2023

# Process Manager Project Report

## Table of Contents
- [Installation](#installation)
- [Introduction](#introduction)
- [Functionalities](#functionalities)
- [Test Results](#test-results)
- [Discussion](#discussion)


## Installation

### Clone the repository to your local machine using the following Git command:
```git clone <repository_url> ```

### Install the required dependencies using the following command:
```pip install -r requirements.txt ```

### Run the Process Manager using the following command:
```python3 main.py```

## Introduction

The Process Manager is a Python project that provides process creation, management, and synchronization functionalities. It allows users to create and manage processes and threads, perform inter-process communication (IPC), and demonstrate process synchronization using various mechanisms.

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
- Demonstrates the use of synchronization mechanisms to solve common synchronization problems (e.g., producer-consumer, reader-writer).

### Command-Line Interface (CLI)
- Provides a user-friendly interface for interacting with the Process Manager.
- Allows users to create processes, create threads, synchronize threads, and perform IPC operations.
- Offers clear and informative command syntax and options.

### Logging and Reporting
- Implements logging and reporting features to track and display the execution of processes and threads.
- Logs significant events, errors, and information related to process synchronization.

