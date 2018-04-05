#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import subprocess as sp
import os
import json
import shutil

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]
# Note: The first argument is the script's path

for arg in sys.argv[1:]:
    my_command = ["convert", "-resize", "1440", arg, arg]
    sp.check_output(my_command, env=my_env)