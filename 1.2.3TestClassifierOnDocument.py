#Hakan Turgut
#NLP HW 2

#1.1.2-1 Training The Naive Bayes Classifier With AddOneSmoothing

file = open("movie-review.NB", "r")

comedyC = 0 #Counter for occurence of comedy
actionC = 0 #Counter for occurence of action

list = [] #List of each every line in corpus
listComedy =[] #list of words in comedy class
listAction =[] #list of words in action class

listComedyU = [] #unique list for comedy
listActionU = [] #unique list for action

for line in file: #Adds each sentence of training corpus in to a main list
    list.append(line)


for x in range(len(list)): #Adds each sentence from list in to a comedy and action list

    if list[x].count("comedy") > 0:
        listComedy.append(list[x]) #Creates comedy list

    else: listAction.append(list[x]) #Creates action list


for x in range(0, len(list)): #Counts the occurence of comedy and action classes

    if list[x].count("comedy")>0:
        comedyC = comedyC + 1 #Counts number of occurences of comedy class

    else: actionC = actionC + 1 #counts number of occurences of action class


for x in range(len(listComedy)): #Makes unique list out of words in comedy class

    tempList = listComedy[x].split(",")

    for y in range (len(tempList)):

         if ((listComedyU.count(tempList[y]) == 0) and (tempList[y]!= "comedy") and (tempList[y]!= "comedy\n")) :

            listComedyU.append(tempList[y])


for x in range(len(listAction)): #makes unique list of words in action class

    tempList = listAction[x].split(",")

    for y in range (len(tempList)):

         if ((listActionU.count(tempList[y]) == 0) and (tempList[y]!= "action")and (tempList[y]!= "action\n")) :

            listActionU.append(tempList[y])


listComedyC = [0,0,0,0,0] #counter for each word in comedy list


listActionC = [0,0,0,0,0,0] #counter for each word in action list


for x in range(0, len(listComedyU)): #iterates through each unique word in comedy class

    for y in range (0, len(list)): #iterates through each line in training corpus

        if list[y].count("comedy")>0:

            if list[y].count(listComedyU[x])>0:
                 # print("comedy")
                listComedyC[x] = listComedyC[x] + 1 #Stores count for each unique word in comedy class



for x in range(0, len(listActionU)): #iterates through each unique word in action class

    for y in range (0, len(list)): #iterates through each line in training corpus

        if list[y].count("action")>0:

            if list[y].count(listActionU[x])>0:
                # print("action")
                listActionC[x] = listActionC[x] + 1 #stores count for each unique word in action class


#Prints Probability Results

#Add 1 to each numertor of the probabilities due to add one smoothing. In addition to this, we add number of unique vocab words in corpus to each denominator

print ("\n" + "Naive Bayes Classifier With Add One Smoothing:" +"\n")

print "Comedy Class Probabilities: \n" #Prints all of the probabilities for the comedy class

print ("P(Comedy) = " + str(comedyC) + "/" + str(comedyC+actionC))

for x in range(len(listComedyU)):

    print("P(" + listComedyU[x] + "|Comedy) = " + str(listComedyC[x]+1) + "/" + str(comedyC+7)) #Add 1 to each numerator in the Comedy class

print("P(furious|Comedy) = " + str(0+1) + "/" + str(comedyC+7) + "\n" + "P(shoot | Comedy) = " + str(0+1) + "/" + str(comedyC+7))

print("\n\n" + "Probability of {fast, couple, shoot, fly} under Comedy Class: " + "\n")
print("P = P(Comedy) * P(fast|Comedy) * P(couple|Comedy) * P(shoot|Comedy) * P(fly|Comedy) \n")
print("  = 2/5 * 2/9 * 3/9 * 1/9 * 2/9 \n ")
print("  = " + str(float(2/float(5)) * (2/float(9)) * (3/float(9)) * (1/float(9)) * (2/float(9))))

print "\n"

print "Action Class Probabilities: \n" #Prints all of the probabilities for the action class

print ("P(Action) = " + str(actionC) + "/" + str(comedyC+actionC))

for x in range(len(listActionU)):

    print("P(" + listActionU[x] + " | Action) = " + str(listActionC[x]+1) + "/" + str(actionC+7)) #Add 1 to each numerator in the Action class

print("P(couple | Action) = " + str(0+1) + "/" + str(actionC+7) + "\n")

print("\n\n" + "Probability of {fast, couple, shoot, fly} under Action Class: " + "\n")
print("P = P(Action) * P(fast|Action) * P(couple|Action) * P(shoot|Action) * P(fly|Action) ")
print("  = 3/5 * 1/10 * 4/10 * 2/10")
print("  = " + str( (3/float(5)) * (1/float(10)) * (4/float(10)) * (2/float(10))))

print("\n Final Result: The probability of {fast, couple, shoot, fly} is greater under the Action Class than it is under the Comedy Class as a result of the computations above")