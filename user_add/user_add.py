#!/usr/bin/env python

import os
import pwd
import spwd
import crypt
import getpass
import subprocess

if os.geteuid() != 0:
    exit("You need to be root to add a user to the system, try sudo?")

username = raw_input("Enter username: ")
password = getpass.getpass("Enter password:")

# I know this isn't great programming practice, however pwd breaks when
# not in a try/catch, even in an if case. So janky code it is.
try:
    pwd.getpwnam(username)
    print "[!] This user exists, exiting..."
    exit()
except KeyError:
    print "[+] Creating user..."

    hash_type = spwd.getspnam('root')[1][:3]
    salt = spwd.getspnam('root')[1].partition('$')[-1].rpartition('$')[0][2:]
    hashed_pw = crypt.crypt(password, hash_type+salt)

    command = 'useradd -m -p %s %s' % (hashed_pw, username)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
