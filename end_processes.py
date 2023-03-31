import os
import psutil
import time
from datetime import datetime

# Get the exe name
# Every line in processes.txt is a search
# Everything in the search is killed
#Format:
# delay:[delay]
# proc1
# proc2
# etc

def end_processes_loop():
    process_names = []

    with open("processes.txt", 'r') as file:
        lines = file.readlines()
        lines = [line for line in lines if line != '' and not line[0] in "# .\n"]
        delay = float(lines[0].replace('\n','').replace(' ','').split(':')[1])
        process_names = [x.replace('\n','') for x in lines[1:]]

    process_names = [process for process in process_names if process != '' and not process[0] in "# .\n"]

    print("Terminating processes:",process_names)

    processes_terminated = 0
    for process_name in process_names:
        procObjList = [procObj for procObj in psutil.process_iter() if process_name.lower() in procObj.name().lower() ]
        for process in procObjList:
            create_time = datetime.fromtimestamp(int(process.create_time()))
            msg = f"Terminated {process.name()} PID {process.pid} started @ {create_time}"
            
            try:
                process.terminate()
            except:
                process.kill()
            processes_terminated += 1
            print(msg)
    return [processes_terminated, delay]
            

if __name__ == "__main__":
    print()
    while 1:
        try:
            time_now = datetime.fromtimestamp(int(time.time()))
            print(time_now)
            processes_terminated, delay = end_processes_loop()
            if processes_terminated == 0:
                print("No processes to terminate.\n")
            else:
                print("Processes terminated:", processes_terminated, "\n")
            time.sleep(delay)
        except psutil.AccessDenied as e:
            #pid = e.split('=')[1].replace(')','')
            pid = e.pid
            #print(pid)
            print("Access Denied:", e)
            time.sleep(2)
            continue
        except PermissionError as e:
            pid = e.split('=')[1].replace(')','')
            #os.kill(pid)
            print(pid)
            time.sleep(2)
            continue
        except Exception as e:
            print("Error:", e, "\n")
            time.sleep(2)
            continue
        






