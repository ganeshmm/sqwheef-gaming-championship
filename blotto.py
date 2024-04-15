setups = [[ 1,  1,  8,  1,  1,  1,  4, 21, 31, 31],
          [ 0, 10, 14,  0, 12, 14, 16, 16, 18,  0],
          [  3, 0, 11,  0, 18,  0, 35,  0, 33,  0],
          [ 0,  0,  6,  8, 11, 14, 17, 20, 24,  0],
          [ 0,  5,  6,  9, 12,  1, 27, 31,  2,  7],
          [ 1,  1,  1,  2, 16, 21, 21, 26, 10,  1]]


names = ["The Banglas", "Gujju Gang", "Korndapalli Farm Friends", "Dream Team", "Swaggy MAPY", "Triple-A"]

for i, setup in enumerate(setups):
    if sum(setup) != 100:
        print(f"Team {i+1} has an invalid setup.")

results = [0, 0, 0, 0, 0, 0]
for i in range(len(setups)-1):
    for j in range(i+1, len(setups)):
        i_score = 0
        for k in range(10):
            if setups[i][k] > setups[j][k]:
                i_score += k + 1
            elif setups[i][k] == setups[j][k]:
                i_score += (k + 1) / 2
        if i_score < 27.5:
            results[j] += 1
        elif i_score == 27.5:
            results[i] += 0.5
            results[j] += 0.5
        else:
            results[i] += 1

for i, res in enumerate(results):
    print(f"Team {names[i]}: {res}")