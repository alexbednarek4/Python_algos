# A module is essentially a file containing a set of functions to be included in your application
#There are core python modules, modules you can install via pip package manager (including Django) as well as custom modules

#Core modules
import datetime
from datetime import date
import time

#Pip modules
from camelcase import CamelCase

# today = datetime.date.today()
time_stamp = time.time()
today = date.today()
c = CamelCase()
print(c.hump('hello there world'))
print(today)
print(time_stamp)

