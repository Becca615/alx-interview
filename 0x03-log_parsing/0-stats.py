#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


counter = 0
file_size = 0
status = [200, 301, 400, 401, 403, 404, 405, 500]
dict = {200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0}


def printCode(dict, file_size):
    """print status"""
    print("File size: {}".format(file_size))
    for i in status:
        if dict[i] != 0:
            print("{}: {}".format(i, dict[i]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            if counter != 0 and counter % 10 == 0:
                printCode(dict, file_size)
            lst = line.split(' ')
            if len(lst) != 9:
                continue
            counter += 1
            try:
                file_size += int(lst[-1])
                stat = int(lst[-2])
            except Exception:
                pass
            if stat in status:
                dict[stat] += 1
        printCode(dict, file_size)
    except KeyboardInterrupt:
        printCode(dict, file_size)
        raise