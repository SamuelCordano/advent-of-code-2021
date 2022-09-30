def q1(input_list):
    gammaRateBinary = []
    epsilonRateBinary = []
    for index_column in range(len(input_list[0])):
        countOfZeroes = 0
        countOfOnes = 0
        for index_row in range(len(input_list)):
            if input_list[index_row][index_column] == "0":
                countOfZeroes += 1
            else:
                countOfOnes += 1
        # Once all rows have been counted
        if countOfZeroes > countOfOnes:
            gammaRateBinary.append("0")
            epsilonRateBinary.append("1")
        else:
            gammaRateBinary.append("1")
            epsilonRateBinary.append("0")

    gammaRateBinary = int("".join(gammaRateBinary), 2)
    epsilonRateBinary = int("".join(epsilonRateBinary), 2)
    result = gammaRateBinary * epsilonRateBinary
    print(f"Q1 result: {result}")


def q2_oxygen_rating(input_list):
    gammaRateBinary = []
    epsilonRateBinary = []
    for index_column in range(len(input_list[0])):
        countOfZeroes = 0
        countOfOnes = 0
        for index_row in range(len(input_list)):
            if input_list[index_row][index_column] == "0":
                countOfZeroes += 1
            else:
                countOfOnes += 1
        # Once all rows have been counted
        if countOfZeroes > countOfOnes:
            gammaRateBinary.append("0")
            epsilonRateBinary.append("1")
        else:
            gammaRateBinary.append("1")
            epsilonRateBinary.append("0")

    gammaRateBinary = int("".join(gammaRateBinary), 2)
    epsilonRateBinary = int("".join(epsilonRateBinary), 2)
    result = gammaRateBinary * epsilonRateBinary
    print(f"Q1 result: {result}")


if __name__ == "__main__":
    with open("day3/input.txt") as input:
        inputLines = [str(line.strip()) for line in input]

    input_list = []
    for line in inputLines:
        input_line = []
        currentInput = line.strip()
        for character in currentInput:
            input_line.append(character)
        input_list.append(input_line)

    q1(input_list)
