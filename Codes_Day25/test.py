import package1.module1

print(package1.module1.random_usernames())

from package1 import module1

print(module1.random_usernames())

from package1.module1 import *

print(random_usernames())


from package2.module2 import f1
from package2.package3.module3 import f2

f1()
f2()
