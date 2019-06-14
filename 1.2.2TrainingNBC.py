#Hakan Turgut
#NLP HW 2

#1.2.2 Training The Naive Bayes Classifier

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


#Prints probability Results

print ("\n" + "Naive Bayes Classifier: " +"\n")

print "Comedy Class Probabilities: \n" #Prints all of the probabilities for the comedy class

print ("P(Comedy) = " + str(comedyC) + "/" + str(comedyC+actionC))

for x in range(len(listComedyU)):

    print("P(" + listComedyU[x] + "|Comedy) = " + str(listComedyC[x]) + "/" + str(comedyC))

print("P(furious|Comedy) = " + str(0) + "/" + str(comedyC) + "\n" + "P(shoot|Comedy) = " + str(0) + "/" + str(comedyC))

print "\n"

print "Action Class Probabilities: \n" #Prints all of the probabilities for the action class

print ("P(Action) = " + str(actionC) + "/" + str(comedyC+actionC))

for x in range(len(listActionU)):

    print("P(" + listActionU[x] + "|Action) = " + str(listActionC[x]) + "/" + str(actionC))

print("P(couple|Action) = " + str(0) + "/" + str(actionC) + "\n")