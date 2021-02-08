#!/usr/bin/python
import sys
import site

#site.addsitedir('/var/www/html/PBXPhoneUsageMonitor/lib/python3.6/site-packages')

sys.path.insert(0, "/var/www/html/PBXPhoneUsageMonitor/")

from app import app as application
