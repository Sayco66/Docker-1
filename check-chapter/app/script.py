import subprocess;
import time;

for i in range (9):
    process=subprocess.Popen(["powershell",f"docker run -d -p 8{i}:80 app"]);
    time.sleep(10)

