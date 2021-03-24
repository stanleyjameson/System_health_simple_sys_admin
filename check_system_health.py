import shutil
import psutil

def check_disk_usage(disk):

    du = shutil.disk_usage("/")
    percentage  = du.free/du.total * 100
    return percentage > 20

def check_cpu():


    usage = psutil.cpu_percent(0.1)
    return usage<75


if not check_disk_usage("/"):
    print("Error")

else:
    print("Everthing is ok")

