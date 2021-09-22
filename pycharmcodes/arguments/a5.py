import argparse
from configparser import ConfigParser
import shlex

parser = argparse.ArgumentParser(description='simple app',
                                 fromfile_prefix_chars='@')

parser.add_argument('-a',action='store_true', default=False)
parser.add_argument('-b',action='store', dest='b')
parser.add_argument('-c',action='store', dest='c', type=int)

print(parser.parse_args(['@abc.txt']))