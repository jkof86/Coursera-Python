import shutil
import psutil

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	print(free)
	return free > 10
#checks to see if base windows drive has more than 10% free storage space

def check_cpu_usage(interval):
	cpu = psutil.cpu_percent(interval)
	print(cpu)
	return cpu < 75
#checks to see if cpu usage is below 75%

if not check_disk_usage("/") or not check_cpu_usage(1):
	print("Storage or cpu error...")
else:
	print("System Status Check - Storage: OK | CPU: OK")