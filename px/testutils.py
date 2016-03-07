import random
import datetime

import dateutil
import px_process

# An example time string that can be produced by ps
TIMESTRING = "Mon Mar 7 09:33:11 2016"
TIME = dateutil.parser.parse(TIMESTRING)
SECONDS_SINCE_EPOCH = (TIME - datetime.datetime(1970, 1, 1)).total_seconds()


def spaces(at_least=1, at_most=3):
    return " " * random.randint(at_least, at_most)


def create_process(pid=47536, ppid=1234,
                   timestring=TIMESTRING,
                   username="root",
                   cputime="0:00.03", mempercent="0.0",
                   commandline="/usr/sbin/cupsd -l"):

    psline = (spaces(at_least=0) +
              str(pid) + spaces() +
              str(ppid) + spaces() +
              timestring + spaces() +
              username + spaces() +
              cputime + spaces() +
              mempercent + spaces() +
              commandline)

    return px_process.ps_line_to_process(psline)
