import sys
from sys import argv
from cparser import Parser
from interpreter import Interpreter
try:
    argv[1]
except:
    sys.exit()
scriptpath = argv[1]
if not scriptpath.endswith(".co"):
    sys.exit()

def main(path):
    script = open(path).read()
    parser = Parser(script)
    try:
        if argv[2] == "--transpile":
            return '\n'.join([a for a in parser.out if a])
        else:
            Interpreter('\n'.join([a for a in parser.out if a]))
    except:
        Interpreter('\n'.join([a for a in parser.out if a]))
out = main(scriptpath)
if out:
    print(out)
