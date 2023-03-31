# Task-Killer
Task-Killer is a GitHub repository that automatically kills processes on a loop. It works by reading in a file called `processes.txt`, which contains a delay time followed by a list of processes to be killed. The code then loops through the list of processes, killing each one in turn, and then waits for the specified delay time before looping again. The code also prints out the process name and PID of each process that is killed. If no processes are found to be killed, it will print out a message notifying the user. 

## Usage
To use Task-Killer, you must first clone the repository and then run the `processes.txt` file. This file contains two chunks: a list of processes that will be automatically killed on a loop and a list of processes that will be excluded from the loop. The delay for each loop is set to 0.1.

For example, if you wanted to kill `sqlbrowser.exe`, `sqlwriter.exe`, and `sldworks_fs.exe` on a loop, you would add these processes to the list of processes that will be killed in the `processes.txt` file. Additionally, if you wanted to exclude `explorer.exe`, `taskmgr.exe`, `dwm.exe`, and `ctfmon.exe` from the loop, you would add these processes to the list of processes that will be excluded in the `processes.txt` file.

The code also handles exceptions that occur when attempting to kill a process. If a PermissionError is raised, it will extract the process ID from the error message and print it out. If any other exception is raised, it will print out the error message and continue. Finally, it will wait for two seconds before attempting to kill the process again.

## Processes to be Killed
The list of processes that will be killed on a loop includes:

- sqlbrowser.exe
- sqlwriter.exe
- sldworks_fs.exe
- gamingservices
- FNPLicensingService
- gameinputsvc
- AdobeCollabSync
- GameLibraryAppService
- remotesolverdispatcherservice
- Microsoft.Photos.exe
- Shadow Copy
- SearchApp
- StartMenuExperienceHost.exe
- LockApp
- TextInputHost
- armsvc.exe
- EwServer.exe
- TbtP2pShortcutService
- ThunderboltService
- WMIRegistrationService
- dispatcher.exe
- Zune
- Video.UI.exe
- DbxSvc.exe
- DropboxUpdate.exe
- WMI Performance Reverse Adapter

## Processes to be Excluded
The list of processes that will be excluded from the loop includes:

- explorer.exe
- taskmgr.exe
- dwm.exe
- ctfmon.exe
- msiexec.exe
- apphelp.exe
- taskhostw.exe
- conhost.exe
- wininit.exe
- winlogon.exe