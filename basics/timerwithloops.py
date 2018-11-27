import time
import sys


def countdown(n):
    while n > 0:
        mins, secs = divmod(n, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        sys.stdout.write('\r'+timeformat)
        sys.stdout.flush()
        # print(timeformat)
        time.sleep(1)
        n -= 1
    if n == 0:
        print('BLAST OFF!')


countdown(120)
