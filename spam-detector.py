from tkinter import *

window = Tk()

window.title("Spam Detector Lite")

window.geometry('490x280')
lbl = Label(window, text="Please wait till training is complete.." , font=("Arial",14))
lbl.grid(column=0, row=2)

print("Welcome to Spam Detection service\nLoading Training Sets...")
# Univesal Dictionary
dictionary = {}
countdict = {}
# Declaring basic location
location = 'C:\\spam_detection\\trainingset\\X'
inputfile = ""
spamset = []
hamset = []
# intro to neglect beverb
beverb = ["be", "am", "is", "are", "was", "were", "been", "being", "have", "has", "had", "could", "should", "would",
          "may", "might", "must", "shall", "can", "will", "do", "did", "does", "having", "dont"]
# Iteration for spamset
for i in range(1, 30):
    inputfile = location.replace("X", "spam({0}).txt".format(str(i)))
    with open(inputfile) as f:
        a = str(f.read())
        a = a.replace(",", "")
        a = a.replace(".", "")
        tempset = a.split()
        spamset = spamset + tempset
# Iteration for hamset
for i in range(1, 90):
    inputfile = location.replace("X", "ham({0}).txt".format(str(i)))
    with open(inputfile) as f:
        a = str(f.read())
        a = a.replace(",", "")
        a = a.replace(".", "")
        tempset = a.split()
        hamset = hamset + tempset
# Removing duplicates in ham and spam
tempset = set(spamset)
spamset = list(tempset)
tempset = set(hamset)
hamset = list(tempset)
# print(spamset)
# print(hamset)
for i in spamset:
    if ((len(i) != 1) and i not in beverb and i[:len(i) - 1] not in spamset):
        if i not in dictionary:
            dictionary.update({i: 1})
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
for i in hamset:
    if ((len(i) != 1) and i not in beverb and i[:len(i) - 1] not in hamset):
        if i not in dictionary:
            dictionary.update({i: 1})
        else:
            dictionary[i] = dictionary[i] - 1
            if (dictionary[i] < 0):
                dictionary[i] = 0
# only for testing purpose
"""
for x in hamset:
    print(x, " ", end="")
print()
for x in spamset:
    print(x, " ", end="")
print()
print(dictionary)
print()

"""
sampleset = []
tempset = set()
tmpset = set()

head1 = Label(window, text="Welcome to Spam Detection service" , font=("Arial",14))
head1.grid(column=0, row=0)
head2 = Label(window, text="✔Loading Our Dataset..." , font=("Arial",14))
head2.grid(column=0, row=1)
lbl.configure(text="Training was successful ,Enter your email below : ")
txt = Entry(window, width=80,bd=3)
txt.grid(column=0, row=3)
lbl1 = Label(window, text="", font=("Arial",12))
lbl1.grid(column=0, row=6)
def clicked():
    # Input case as either manual input or from text file
    temp1 = str(txt.get())
    sampleset = temp1.split()
    # to be removed . , ....
    soldict = {}
    for i in sampleset:
        if i not in countdict.keys():
            countdict.update({i: 1})
        else:
            countdict[i] = countdict[i] + 1
    for x in sampleset:
        soldict.update({x: 0})
    for i in sampleset:
        if i in spamset:
            soldict.update({i: soldict[i] + 1})
    for i in soldict:
        # print(soldict[i])
        temp = soldict[i] / countdict[i]
        soldict.update({i: temp})
    solution = 0
    for i in soldict:
        solution = solution + soldict[i]
    if len(soldict):
        solution = solution / len(soldict)
    solution = solution * 100
    lbl2.configure(text="Result : ")
    if (solution > 80):
        print("The mail is mostly spam!!! [ probability : {0}% ]".format(round(solution, 1)))
        lbl1.configure(text="The mail is mostly spam!!! [ probability : {0}% ]".format(round(solution, 1)))
    elif (solution > 55):
        print("The mail may be a spam [ probability : {0}% ]".format(round(solution, 1)))
        lbl1.configure(text="The mail may be a spam [ probability : {0}% ]".format(round(solution, 1)))
    elif (solution > 30):
        print("The mail has low chance of being spam [ probability : {0}% ]".format(round(solution, 1)))
        lbl1.configure(text="The mail has low chance of being spam [ probability : {0}% ]".format(round(solution, 1)))
    else:
        print("The mail is a Ham :) [ probability : {0}% ]".format(round(solution, 1)))
        lbl1.configure(text="The mail is a Ham :) [ probability : {0}% ]".format(round(solution, 1)))
btn = Button(window, text="Check for Spam ", command=clicked)
btn.grid(column=0, row=4)
lbl2 = Label(window, text="", font=("Arial Bold",12))
lbl2.grid(column=0, row=5)
window.mainloop()