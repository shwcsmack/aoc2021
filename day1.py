def count_increase():
    with open("day1input.txt") as input:
        lineIndex = 0
        previousDeoth = 0
        increased = []
        for line in input:
            line = line.strip()
            if lineIndex == 0:
                print(line + " N/A")
            elif line > previousDeoth:
                print(line + " Increased")
                increased.append(line)
            elif line < previousDeoth:
                print(line + " Decreased")
            lineIndex += 1
            previousDeoth = line
        print(increased)
        print(len(increased))