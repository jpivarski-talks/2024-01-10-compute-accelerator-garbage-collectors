import socket

import numpy as np

shuffle3 = [0, 2, 3]
shuffle7 = [1, 2, 0, 6, 4, 7, 5]
shuffle13 = [1, 2, 9, 13, 10, 12, 0, 6, 5, 11, 4, 8, 14]
shuffle31 = [21, 1, 17, 30, 11, 19, 24, 8, 14, 3, 0, 16, 18, 20, 31, 27, 22, 9, 28, 10, 5, 13, 2, 26, 12, 6, 15, 29, 25, 7, 4]
shuffle61 = [47, 51, 60, 44, 7, 5, 17, 25, 14, 63, 62, 37, 21, 9, 4, 56, 15, 3, 26, 28, 41, 6, 31, 52, 2, 1, 11, 10, 23, 59, 13, 8, 42, 39, 55, 54, 0, 27, 58, 16, 20, 38, 35, 45, 61, 12, 57, 30, 53, 32, 34, 29, 46, 50, 49, 33, 40, 48, 19, 43, 22]

# average +- std age of object being replaced
# shuffle3: 3.0 +- 0.0
# shuffle3 shuffle7: 21.0 +- 6.324555320336759
# shuffle3 shuffle7 shuffle13: 315.0 +- 123.50438588703369
# shuffle3 shuffle7 shuffle13 shuffle31: 9765.0 +- 3975.2148788880995
# shuffle3 shuffle7 shuffle13 shuffle31 shuffle61: 615195.0 +- 251128.1357501252

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

array = np.full(4 * 8 * 16 * 32 * 64, None, dtype=object)

try:
    count = 0
    while True:
        for i61 in shuffle61:
            for i31 in shuffle31:
                for i13 in shuffle13:
                    for i7 in shuffle7:
                        for i3 in shuffle3:
                            array[(((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3] = tmp = []
                            tmp.append(tmp)
                            if count & 0x7ff == 0:
                                client.send(b".")
                            count += 1

        for i3 in shuffle3:
            for i7 in shuffle7:
                for i13 in shuffle13:
                    for i31 in shuffle31:
                        for i61 in shuffle61:
                            array[(((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3] = tmp = []
                            tmp.append(tmp)
                            if count & 0x7ff == 0:
                                client.send(b".")
                            count += 1
except KeyboardInterrupt:
    client.send(b"X")
