if __name__ == "__main__":
    with open("day2/inputText.txt") as input:
        inputLines = [str(line.strip()) for line in input]

    # Q1
    positionHorizontal = 0
    positionDepth = 0
    for line in inputLines:
        if line[0] == "f":
            positionHorizontal += int(line[-1])
        elif line[0] == "u":
            positionDepth -= int(line[-1])
        elif line[0] == "d":
            positionDepth += int(line[-1])

    print(f"Answer Q1: {positionHorizontal*positionDepth}")

    # Q2
    positionHorizontal = 0
    positionDepth = 0
    aim = 0
    for line in inputLines:
        if line[0] == "f":
            positionHorizontal += int(line[-1])
            positionDepth += aim * int(line[-1])
        elif line[0] == "u":
            aim -= int(line[-1])
        elif line[0] == "d":
            aim += int(line[-1])

    print(f"Answer Q2: {positionHorizontal*positionDepth}")
