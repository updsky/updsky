#!/usr/bin/env python


f=open("/root/iptest.txt")
ip=[]
lines = f.readline()
while lines:
    ip.append("".join(lines.split()))
    lines = f.readline()
f.close()
print(ip)



                            