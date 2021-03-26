import random

N_SAMPLES = 50
THRESHOLD = 0.95

if __name__ == "__main__":
    select_from = {}

    with open("../trained_models/swappedBinOperands/poss_anomalies.txt", "r") as an:
        for line in an:
            if (float(line[8:line.find("|")])) <= THRESHOLD:
                break
            project = "/".join(line.split("/")[3:5])
            if project not in select_from:
                select_from[project] = []
            select_from[project].append(line)

    print(f"Samples to choose from {len(select_from)} ")

    # First choose projects
    sampled = random.sample(list(select_from.keys()), N_SAMPLES)
    result = []
    # Then choose sample from project
    for sample in sampled:
        result.append(random.choice(select_from[sample]))

    with open("sampled.csv", "w+") as out:
        print(f"Sampled values: {N_SAMPLES}")
        for i in result:
            print(i, end="", file=out)
