questions = 'file/questions.txt'
nswers = 'file/nswers.txt'
choices = 'file/choices.txt'
with open(questions) as qus:
    qulist = qus.readlines()
with open(nswers) as ns:
    nslist = ns.readlines()
with open(choices) as chs:
    chlist = chs.readlines()
grade = 0
addsp = 10
qudlis = []
andlis = []
chdlis = []
mistakes = []
index = 0
active = True
print("The total score for this test is "+str(len(qulist)*addsp))
while active:
    index + 1
    try:
        que = qulist.pop(index)
        cho = chlist.pop(index)
        nsw = nslist.pop(index)
        print(que)
        print(cho)
        usput = input("Please enter your choice:")
        if usput.lower() == nsw.rstrip():
            grade += addsp
            qudlis.append(que)
            chdlis.append(cho)
            andlis.append(nsw)
        else:
            mistakes.append(que)
            chdlis.append(cho)
            andlis.append(nsw)
    except IndexError:
        active = False
print("\nOK!  Your grade is " + str(grade))
if mistakes:
    print("Your mistakes are : ")
    for mistake in mistakes:
            print('\t'+mistake.rstrip())
else:
    print("Congratulations! You got all the questions right!")
print("\n")
input("Thanks for your play!  Enter anything to Exit!")
