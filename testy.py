# import gc
import socket

import numpy as np

shuffleA = [7, 6, 4, 10, 0, 15, 9, 8, 13, 5, 12, 14, 3, 11, 2, 1]
shuffleB = [3, 8, 0, 15, 11, 2, 6, 7, 12, 9, 1, 14, 5, 13, 4, 10]
shuffleC = [2, 13, 6, 7, 4, 5, 10, 3, 12, 15, 8, 9, 14, 1, 0, 11]
shuffleD = [7, 5, 9, 15, 4, 2, 13, 12, 0, 8, 11, 6, 3, 1, 10, 14]
shuffleE = [14, 11, 10, 8, 0, 6, 5, 1, 13, 9, 7, 4, 2, 12, 3, 15]
shuffleF = [10, 5, 4, 6, 15, 1, 9, 13, 7, 2, 11, 12, 0, 8, 3, 14]
shuffleG = [5, 12, 6, 14, 4, 13, 3, 0, 7, 9, 15, 2, 11, 8, 1, 10]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8087))

array = np.zeros(16**7, dtype=np.int32)
# array = np.full(16**7, None, dtype=object)

# gc.disable()
# gc.collect()

count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    for iF in shuffleF:
                        for iG in shuffleG:
                            array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG] = count
                            # array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG] = (None,) * 100
                            # array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG] = tmp = []
                            # tmp.append(tmp)
                            if count & 0x7ff == 0:
                                client.send(b"1")
                            count += 1

            for iD in shuffleD:
                for iE in shuffleE:
                    for iF in shuffleF:
                        for iG in shuffleG:
                            array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG] = count
                            # array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG] = (None,) * 100
                            # array[(((((iA*16 + iB)*16 + iC)*16 + iD)*16 + iE)*16 + iF)*16 + iG] = tmp = []
                            # tmp.append(tmp)
                            if count & 0x7ff == 0:
                                client.send(b"2")
                            count += 1
