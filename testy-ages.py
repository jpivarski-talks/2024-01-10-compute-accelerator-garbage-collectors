import numpy as np

# shuffleA = list(range(16))
# shuffleB = list(range(16))
# shuffleC = list(range(16))
# shuffleD = list(range(16))
# shuffleE = list(range(16))
# random.shuffle(shuffleA)
# random.shuffle(shuffleB)
# random.shuffle(shuffleC)
# random.shuffle(shuffleD)
# random.shuffle(shuffleE)

shuffleA = [7, 6, 4, 10, 0, 15, 9, 8, 13, 5, 12, 14, 3, 11, 2, 1]
shuffleB = [3, 8, 0, 15, 11, 2, 6, 7, 12, 9, 1, 14, 5, 13, 4, 10]
shuffleC = [2, 13, 6, 7, 4, 5, 10, 3, 12, 15, 8, 9, 14, 1, 0, 11]
shuffleD = [7, 5, 9, 15, 4, 2, 13, 12, 0, 8, 11, 6, 3, 1, 10, 14]
shuffleE = [14, 11, 10, 8, 0, 6, 5, 1, 13, 9, 7, 4, 2, 12, 3, 15]

array = np.full(16**5, -1, dtype=np.int64)
ages = []
count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] == -1
                    array[i] = count
                    count += 1
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
assert np.all(array != -1)
print(f"shuffleE: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(16**5, -1, dtype=np.int64)
ages = []
count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] == -1
                    array[i] = count
                    count += 1
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
assert np.all(array != -1)
print(f"shuffleD shuffleE: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(16**5, -1, dtype=np.int64)
ages = []
count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] == -1
                    array[i] = count
                    count += 1
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
assert np.all(array != -1)
print(f"shuffleC shuffleD shuffleE: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(16**5, -1, dtype=np.int64)
ages = []
count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] == -1
                    array[i] = count
                    count += 1
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
assert np.all(array != -1)
print(f"shuffleB shuffleC shuffleD shuffleE: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(16**5, -1, dtype=np.int64)
ages = []
count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] == -1
                    array[i] = count
                    count += 1
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
assert np.all(array != -1)
print(f"shuffleA shuffleB shuffleC shuffleD shuffleE: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(16**5, -1, dtype=np.int64)
ages = []
count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] == -1
                    array[i] = count
                    count += 1
            for iE in shuffleE:
                for iD in shuffleD:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
assert np.all(array != -1)
print(f"shuffleE shuffleD: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(16**5, -1, dtype=np.int64)
ages = []
count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] == -1
                    array[i] = count
                    count += 1
        for iE in shuffleE:
            for iD in shuffleD:
                for iC in shuffleC:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
assert np.all(array != -1)
print(f"shuffleE shuffleD shuffleC: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(16**5, -1, dtype=np.int64)
ages = []
count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] == -1
                    array[i] = count
                    count += 1
    for iE in shuffleE:
        for iD in shuffleD:
            for iC in shuffleC:
                for iB in shuffleB:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
assert np.all(array != -1)
print(f"shuffleE shuffleD shuffleC shuffleB: {np.mean(ages)} ± {np.std(ages)}")

array = np.full(16**5, -1, dtype=np.int64)
ages = []
count = 0
for iA in shuffleA:
    for iB in shuffleB:
        for iC in shuffleC:
            for iD in shuffleD:
                for iE in shuffleE:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] == -1
                    array[i] = count
                    count += 1
for iE in shuffleE:
    for iD in shuffleD:
        for iC in shuffleC:
            for iB in shuffleB:
                for iA in shuffleA:
                    i = (((iE*16 + iD)*16 + iC)*16 + iB)*16 + iA
                    assert array[i] != -1
                    ages.append(count - array[i])
                    array[i] = count
                    count += 1
assert np.all(array != -1)
print(f"shuffleE shuffleD shuffleC shuffleB shuffleA: {np.mean(ages)} ± {np.std(ages)}")
