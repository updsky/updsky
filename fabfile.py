#!/usr/bin/env python

from fabric.api import *
from fabric.colors import *

f=open("/root/iptest.txt")
ip=[]
env.host=[]
lines = f.readline()
while lines:
    ip.append("".join(lines.split()))
    lines = f.readline()
f.close()

env.user = 'root'
#env.user = input('请输入用户名：')
env.hosts = ip
wip = len(ip)
env.password = input('请输入密码：')

#检查设备时间
@task
def time():
    with hide('running'):
    	run('echo 服务器时间;date -R')

#检查设备空间状态
@task
def df():
#    run("echo 系统盘剩余空间;df -h | awk 'NR==2'{'print $4'}")
    run("echo 系统盘剩余空间;df -h ")
    with cd("/var/log"):
       run('echo 系统日志大小;du -sh')

#检查设备所有状态信息
@task
def status():
    run('echo 服务器时间;date -R')
    run("echo 系统盘剩余空间;df -h ")
    with cd("/var/log"):
       run('echo 系统日志大小;du -sh ')

#检查设备时间同步服务
@task
def ntp():
    run('service ntpd restart')

#批量执行
@task
def com():
    with hide('running'):
    	run('yum update -y yum-plugin-fastestmirror yum-plugin-security yum-utils')
    print(green("执行成功！"))

