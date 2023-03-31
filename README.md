# Task-Killer

Task-Killer is a GitHub repository designed to automatically terminate processes on a loop. It reads in a `processes.txt` file which contains a list of processes to be killed and a delay time. It then iterates through the list and terminates them one by one, printing out the name of the process and its PID and the time it was started. Finally, it returns the number of processes terminated and the delay time. 

## Usage

The main code is located in the `end_processes.py` file. The `end_processes_loop()` function reads in the `processes.txt` file, which contains a list of processes to be killed and a delay time. It then iterates through the list of processes and terminates them one by one. It also prints out the name of the process and its PID and the time it was started. Finally, it returns the number of processes terminated and the delay time. 

The `main()` function prints out the current time and then runs `end_processes_loop()`, sleeps for the delay time, and repeats. It also handles AccessDenied errors by printing out the error and sleeping for the delay time. 

The code attempts to end processes using the `os.kill` command, and catches any errors that may occur. If an error is encountered, the code prints the error and waits two seconds before trying again. In the case of a `PermissionError`, the code grabs the process ID (pid) from the error message and prints it. It does not actually kill the process, however, as the `os.kill` command is commented out.

### Example

Let's say the `processes.txt` file contains the following:

```
chrome.exe, 10
notepad.exe, 5
```

This means that the `end_processes_loop()` function will attempt to terminate the `chrome.exe` and `notepad.exe` processes, and will wait 10 and 5 seconds respectively before attempting to terminate them again. The `main()` function will then print the current time and run the `end_processes_loop()` function, sleep for the delay time, and repeat. 

If any errors are encountered, the code will print the error and wait two seconds before trying again. If a `PermissionError` is encountered, the code will grab the process ID (pid) from the error message and print it, but will not actually kill the process.

## Usage

To use Task-Killer, first clone the repository to your local machine. Then, edit the `processes.txt` file to include the processes you want to terminate and the delay time between terminations. Finally, run the `end_processes.py` file to begin the process of terminating the processes. 

The code will attempt to terminate the processes, and if any errors are encountered, it will print the error and wait two seconds before trying again. If a `PermissionError` is encountered, the code will grab the process ID (pid) from the error message and print it, but will not actually kill the process.