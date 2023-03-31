# Task-Killer

Task-Killer is a GitHub repository that automates the process of killing processes on a loop. It contains a single Python script, `end_processes.py`, which reads the `processes.txt` and `processes2.txt` files and terminates each process in the list.

## Usage

Using the Task-Killer code is straightforward. First, you'll need to identify which processes you want to kill and add them to the appropriate file (either `processes.txt` or `processes2.txt`). The `processes.txt` file includes a delay of 0.1 and a list of processes that may be killed, such as `sqlbrowser.exe`, `sqlwriter.exe`, `sldworks_fs.exe`, `gamingservices`, `FNPLicensingService`, `gameinputsvc`, `AdobeCollabSync`, `GameLibraryAppService`, `remotesolverdispatcherservice`, `Microsoft.Photos.exe`, `SearchApp`, `StartMenuExperienceHost.exe`, `LockApp`, `TextInputHost`, `armsvc.exe`, `EwServer.exe`, `TbtP2pShortcutService`, `ThunderboltService`, `WMIRegistrationService`, `dispatcher.exe`, `Zune`, `Video.UI.exe`, `DbxSvc.exe`, `DropboxUpdate.exe`, and `WMI Performance Reverse Adapter`. The `processes2.txt` file includes a delay of 0.1 and a list of processes that may be killed, such as `RTHDCPL.exe`, `RtHDVCpl.exe`, `rtHDVRpl.exe`, `rtHDVBpl.exe`, `rtHDVPl.exe`, `rtHDVCl.exe`, `rtHDVSL.exe`, `rtHDVFl.exe`, `rtHDVBl.exe`, `rtHDVGl.exe`, `rtHDVUl.exe`, `rtHDVYl.exe`, `rtHDVAl.exe`, `rtHDVCl.exe`, `rtHDVPl.exe`, `rtHDVSl.exe`, `rtHDVFl.exe`, `rtHDVBl.exe`, `rtHDVGl.exe`, `rtHDVUl.exe`, `rtHDVYl.exe`, `rtHDVAl.exe`, `rtHDVCl.exe`, `rtHDVPl.exe`, `rtHDVSl.exe`, `rtHDVFl.exe`, `rtHDVBl.exe`, `rtHDVGl.exe`, `rtHDVUl.exe`, and `rtHDVYl.exe`.

Once you have identified the processes to be killed and added them to the appropriate file, you can then run the `end_processes.py` script. The script will read the `processes.txt` or `processes2.txt` file and create a list of processes to be terminated. For each process in the list, it will terminate the process and print a message with the process name, PID, and start time. Lastly, the script will sleep for the specified delay and repeat the loop. If the process cannot be terminated due to an access denied error, the script will sleep for the specified delay and then try again.

#### Example

Let's say you have a `processes.txt` file that contains the following:

```
process1, 5
process2, 10
```

This file tells the `end_processes.py` script to terminate `process1` and `process2`, and to wait 5 and 10 seconds, respectively, between each loop. When you run the script, it will terminate `process1`, wait 5 seconds, terminate `process2`, wait 10 seconds, and then repeat the loop.

## Conclusion

Task-Killer is a GitHub repository that automates the process of killing processes on a loop. It contains a single Python script, `end_processes.py`, which reads the `processes.txt` and `processes2.txt` files and terminates each process in the list. To use Task-Killer, first create a `processes.txt` or `processes2.txt` file that contains a list of processes to be killed, along with the delay between each loop. Then, run the `end_processes.py` script. The script will read the file and create a list of processes to be terminated. For each process in the list, it will terminate the process and print a message with the process name, PID, and start time. Lastly, the script will sleep for the specified delay and repeat the loop. If the process cannot be terminated due to an access denied error, the script will sleep for the specified delay and then try again.