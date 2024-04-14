setups = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
          [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
          [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
          [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
          [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
          [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]

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
    print(f"Team {i+1}: {res}")