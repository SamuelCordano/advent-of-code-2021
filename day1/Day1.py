if __name__ == "__main__":
    with open("day1/inputText.txt") as input:
        inputLines = [int(line.strip()) for line in input]

    #Q1
    counter = 0
    for index in range(len(inputLines)-1):
        if inputLines[index+1]>inputLines[index]:
            counter+=1
    print(f"Answer Q1: {counter}")

    #Q2
    counter = 0
    for index in range(2,len(inputLines)-1):
        if inputLines[index+1]>inputLines[index-2]:
            counter+=1
    print(f"Answer Q2: {counter}")
