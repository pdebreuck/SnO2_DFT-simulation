#!/usr/bin/expect -f

spawn ssh -XY tuto10@gwcism.cism.ucl.ac.be
expect "password:"
send "TONMOTDEPASSE\r"
expect "$ "
send "ssh -XY tuto10@manneback.cism.ucl.ac.be\r"
expect "password:"
send "TONMOTDEPASSE\r"
interact
