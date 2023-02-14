#!/usr/bin/python

import time
import signal
import sys

def wait():
  try:
    print("Going to sleep now.", file=sys.stderr)
    time.sleep(30)
    print("Woke up.", file=sys.stderr)
  except:
    print("Caught an exception.", file=sys.stderr)

def signal_handler(sig, frame):
  print('Ctrl+C!')
  sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)
wait()
