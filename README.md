# cisco-config-tftp [![Build Status](https://travis-ci.com/strohmy86/cisco-config-tftp.svg?branch=master)](https://travis-ci.com/strohmy86/cisco-config-tftp)
Tool to download and upload (using a tftp server) a running-config from/to a cisco switch using the snmp protocol.

## Compatability
This program is written in Python 3 (3.7.2) on Arch Linux and *should* work with any 3.x. I have not tested to verify this.

This program must be run with administrative privileges (sudo) in order to create the tftp server that's built into the program. The Linux version uses the [easysnmp](https://github.com/kamakazikamikaze/easysnmp) module, and the Mac version uses MacOS' built in TFTP server.

## Additional Info     
The binary executables in the repo are for Linux and Mac, made using [PyInstaller](http://www.pyinstaller.org/).

The module [easysnmp](https://github.com/kamakazikamikaze/easysnmp) doesn't build on Windows due to the lack of Net-SNMP. I didn't package this for Windows for this reason according to [net-snmp.org](http://www.net-snmp.org/download.html):
> IMPORTANT NOTE FOR WINDOWS USERS: the Net-SNMP Windows binaries have been built with OpenSSL version 0.9.8r. Since the OpenSSL 0.9 and 1.0 DLLs are incompatible, any attempt to install Net-SNMP on a system where OpenSSL 1.0 has been installed will fail. 

