import socket

import numpy as np

shuffleA = [7, 6, 4, 10, 0, 15, 9, 8, 13, 5, 12, 14, 3, 11, 2, 1]
shuffleB = [3, 8, 0, 15, 11, 2, 6, 7, 12, 9, 1, 14, 5, 13, 4, 10]
shuffleC = [2, 13, 6, 7, 4, 5, 10, 3, 12, 15, 8, 9, 14, 1, 0, 11]
shuffleD = [7, 5, 9, 15, 4, 2, 13, 12, 0, 8, 11, 6, 3, 1, 10, 14]
shuffleE = [14, 11, 10, 8, 0, 6, 5, 1, 13, 9, 7, 4, 2, 12, 3, 15]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

array = np.full(16**5, None, dtype=object)

try:
    count = 0
    while True:
        for iA in shuffleA:
            for iB in shuffleB:
                for iC in shuffleC:
                    for iD in shuffleD:
                        for iE in shuffleE:
                            array[(((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE] = tmp = []
                            tmp.append(tmp)
                            if count & 0x7ff == 0:
                                client.send(b".")
                            count += 1

        for iE in shuffleE:
            for iD in shuffleD:
                for iC in shuffleC:
                    for iB in shuffleB:
                        for iA in shuffleA:
                            array[(((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE] = tmp = []
                            tmp.append(tmp)
                            if count & 0x7ff == 0:
                                client.send(b".")
                            count += 1
except KeyboardInterrupt:
    client.send(b"X")
