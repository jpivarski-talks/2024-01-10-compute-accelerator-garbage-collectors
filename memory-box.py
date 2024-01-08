import subprocess
import sys
import time

import psutil


memorymax, *arguments = sys.argv[1:]

proc = subprocess.Popen(
    [
        "systemd-run",
        "--user",
        "--scope",
        "-p",
        "MemoryMax=" + memorymax,
        "-p",
        "MemorySwapMax=0M",
    ]
    + list(arguments)
)
psproc = psutil.Process(proc.pid)


starttime = now = time.time()
while now - starttime < 60:
    if proc.poll() is None:
        print(f"MEASURE {now - starttime} {psproc.memory_full_info().uss}")
    else:
        print(f"MEASURE {now - starttime} 0")
        break

    time.sleep(0.1)
    now = time.time()

proc.terminate()
proc.kill()
