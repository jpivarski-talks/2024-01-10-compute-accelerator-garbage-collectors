import numpy as np

# shuffle3 = list(range(4))
# shuffle7 = list(range(8))
# shuffle13 = list(range(16))
# shuffle31 = list(range(32))
# shuffle61 = list(range(64))
# random.shuffle each and drop the last element
shuffle3 = [0, 2, 3]
shuffle7 = [1, 2, 0, 6, 4, 7, 5]
shuffle13 = [1, 2, 9, 13, 10, 12, 0, 6, 5, 11, 4, 8, 14]
shuffle31 = [21, 1, 17, 30, 11, 19, 24, 8, 14, 3, 0, 16, 18, 20, 31, 27, 22, 9, 28, 10, 5, 13, 2, 26, 12, 6, 15, 29, 25, 7, 4]
shuffle61 = [47, 51, 60, 44, 7, 5, 17, 25, 14, 63, 62, 37, 21, 9, 4, 56, 15, 3, 26, 28, 41, 6, 31, 52, 2, 1, 11, 10, 23, 59, 13, 8, 42, 39, 55, 54, 0, 27, 58, 16, 20, 38, 35, 45, 61, 12, 57, 30, 53, 32, 34, 29, 46, 50, 49, 33, 40, 48, 19, 43, 22]

array = np.full(4 * 8 * 16 * 32 * 64, -1, dtype=np.int64)
ages = []
count = 0
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] == -1
                    array[i] = count
                    count += 1
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
print(f"shuffle3: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(4 * 8 * 16 * 32 * 64, -1, dtype=np.int64)
ages = []
count = 0
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] == -1
                    array[i] = count
                    count += 1
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
print(f"shuffle7 shuffle3: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(4 * 8 * 16 * 32 * 64, -1, dtype=np.int64)
ages = []
count = 0
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] == -1
                    array[i] = count
                    count += 1
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
print(f"shuffle13 shuffle7 shuffle3: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(4 * 8 * 16 * 32 * 64, -1, dtype=np.int64)
ages = []
count = 0
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] == -1
                    array[i] = count
                    count += 1
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
print(f"shuffle31 shuffle13 shuffle7 shuffle3: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(4 * 8 * 16 * 32 * 64, -1, dtype=np.int64)
ages = []
count = 0
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] == -1
                    array[i] = count
                    count += 1
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
print(f"shuffle61 shuffle31 shuffle13 shuffle7 shuffle3: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(4 * 8 * 16 * 32 * 64, -1, dtype=np.int64)
ages = []
count = 0
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] == -1
                    array[i] = count
                    count += 1
            for i3 in shuffle3:
                for i7 in shuffle7:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
print(f"shuffle3 shuffle7: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(4 * 8 * 16 * 32 * 64, -1, dtype=np.int64)
ages = []
count = 0
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] == -1
                    array[i] = count
                    count += 1
        for i3 in shuffle3:
            for i7 in shuffle7:
                for i13 in shuffle13:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
print(f"shuffle3 shuffle7 shuffle13: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(4 * 8 * 16 * 32 * 64, -1, dtype=np.int64)
ages = []
count = 0
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] == -1
                    array[i] = count
                    count += 1
    for i3 in shuffle3:
        for i7 in shuffle7:
            for i13 in shuffle13:
                for i31 in shuffle31:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
print(f"shuffle3 shuffle7 shuffle13 shuffle31: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(4 * 8 * 16 * 32 * 64, -1, dtype=np.int64)
ages = []
count = 0
for i61 in shuffle61:
    for i31 in shuffle31:
        for i13 in shuffle13:
            for i7 in shuffle7:
                for i3 in shuffle3:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] == -1
                    array[i] = count
                    count += 1
for i3 in shuffle3:
    for i7 in shuffle7:
        for i13 in shuffle13:
            for i31 in shuffle31:
                for i61 in shuffle61:
                    i = (((i61*32 + i31)*16 + i13)*8 + i7)*4 + i3
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
print(f"shuffle3 shuffle7 shuffle13 shuffle31 shuffle61: {np.mean(ages)} ± {np.std(ages)}")
