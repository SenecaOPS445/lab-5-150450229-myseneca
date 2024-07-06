#!/usr/bin/env python3
# METHOD 1
f = open('data.txt', 'r')
method1 = list(f)
f.close()
print(method1)

# METHOD 2
f = open('data.txt', 'r')
method2 = f.readlines()
f.close()
print(method2)
