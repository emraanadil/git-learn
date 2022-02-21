import os
import shutil
import sys
from tabnanny import check

def check_reboot():
  """Returns True if computer has pending reboot"""
  return os.path.exists("run/reboot-required")
def check_disk_full(disk,min_gb,min_percent):
  """Checks the usage of disk in pc"""
  du = shutil.disk_usage(disk)
  percent_free= (du.free/du.total) * 100
  gigabytes_free = du.free/2**30
  if percent_free < min_percent or gigabytes_free < min_gb:
    return True
  return False

def check_root_full():
  """Return True if root partition is full, false otherwise """
  return check_disk_full('/',2, 10)


def main():
  """final main function"""
  checks = [
    (check_root_full, "Root Partition full")
    (check_reboot,"Pending reboot")
  ]
  true = True
  for check,msg in checks:
    if check():
      print(msg)
      true = False
  if not true:
    sys.exit(1)
  print("Everything OK")
  sys.exit(0)


main()
