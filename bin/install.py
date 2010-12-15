#!/usr/bin/env python
# fetch the drupal module and unzip 
import subprocess
import sys
print sys.argv[1]
input =sys.argv[1]
result =input[(sys.argv[1].rfind("/")+1):]
print result
subprocess.call("wget "+input+ "&& tar -vzxf " +result+" &&rm "+result, shell=True)
