while True:
    try: 
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt):")
        filenametxt = filename + ".txt"
        f = open(filenametxt)
    except:
        print("File cannot be found.")
    else:
        print("Successfully opened", filenametxt)
        break
print("**** ANALYZING ****")
file = f.read()
responses = file.split("\n")
invalidans = 0 
validans = 0
validresponses = [] 

for each in responses:
    data = each.split(",")
    count = 0
    incorrect = 0
    for ans in data:
        if count == 0:
            if ans[0] != "N" or len(ans) != 9 or ans[1:].isnumeric() == False:
                print("Invalid line of data: N# is invalid")
                print(data)
                invalidans +=1
                incorrect +=1
        count +=1
    validans +=1
    
    if count != 26:
        print("Invalid line of data: does not contain exactly 26 values:")
        print(data)
        incorrect +=1
        invalidans +=1

    if incorrect == 0:
        validresponses.append(data)
        
if invalidans == 0:
    print("No errors found!")

print("**** REPORT ****")
print("Total valid lines of data:", validans - invalidans)
print("Total invalid lines of data:", invalidans)

answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answerkey.split(",")
grades = []
for input in validresponses:
    correct = 0
    for i in range(len(input)-1):
        if input[i+1] == answer_key[i]:
            correct +=4
        elif input[i+1] == "":
            correct +=0
        elif input[i+1] != answer_key[i]:
            correct -=1
    grades.append(correct)

averagescore = (sum(grades) / len(grades))
highestscore = max(grades)
lowestscore = min(grades)
rangescore = (highestscore - lowestscore)
print("Mean (average) score: " + str("{:.2f}".format(averagescore)))
print("Highest score: " + str(highestscore))
print("Lowest score: " + str(lowestscore))
print("Range of scores: " + str(rangescore))

median = []
for num in grades:
    median.append(num)
median.sort()
m = len(median)

if m % 2 == 0:
    median1 = median[m//2]
    median2 = median[m//2 - 1]
    medianfinal = (median1 + median2)/2
else:
    medianfinal = median[m//2]
print("Median score: " + str(medianfinal))

final_grades = []
for each in responses:
    data = each.split(",")
    final_grades.append(data[0])
    
f = open(filename + "_grades.txt", "x")
for i in range(len(grades)):
    f.write(str(final_grades[i]) + "," + str(grades[i]) + "\n")

