import sys
import platform
import sysconfig
import os
import time
from time import gmtime, strftime
import datetime


print(platform.node())
print()
print("Kernel: " + platform.machine() + " " + platform.version().split(':')[0])
print()
print("OS: " + platform.platform())
print()
print("System: " + platform.system())
print()
ts = time.time()
print(gh_imgui.text("%.1f sec" % ts))

