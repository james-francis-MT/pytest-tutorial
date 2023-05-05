def findMostCals(input_array):
    if input_array[-1] != '':
        input_array.append('')
        
    totalCals = {}
    elf = 1
    runningTotal = 0
    for line in input_array:
        if line == '':
            totalCals[elf] = runningTotal
            elf += 1
            runningTotal = 0
            continue
        
        runningTotal += int(line)


    elfWithMost = max(totalCals, key=totalCals.get)

    print('The elf with the most calories is elf number: ' + str(elfWithMost) + ' with: ' + str(totalCals[elfWithMost]) + ' calories')

    return totalCals[elfWithMost]


file = open('advent_of_code_day_1/input.txt', 'r')
arrayOfLines = file.readlines()

arrayOfLines = [x.strip('\n') for x in arrayOfLines]

findMostCals(arrayOfLines)

file.close()