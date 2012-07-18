#!/usr/bin/python
# Choice.py - 
#    because opening up ipython each time is a chore

import sys
from random import choice

args = sys.argv[1:]

try:
    if args == []:
        while True:
            inline = raw_input("?> ")
            if inline == "":
                print choice(args)
                sys.exit(0)
            else:
                args.append(inline)
        
    else:
        print choice(args)
        
except (KeyboardInterrupt, EOFError):
    print "\n", choice(args)
