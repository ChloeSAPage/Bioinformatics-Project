# Load Nucleotide sequence into a list
def LoadRecords(FileName): 
	RecordList = []
	file = open(FileName, "r")
	for Line in file:	
		Tokens = Line.split()
		RecordList.append(Tokens)
	file.close()
	return RecordList


def LoadSingleSequence(FileName):
	RecordData = LoadRecords(FileName)
	return RecordData[0][2]

Records = LoadRecords("Human-Covid19.txt")
BatSeq = LoadSingleSequence("Bat-Covid19.txt")


#creating the function SequenceDistance and giving it two paramaters, batsequence and the sequence to be compared.
def SequenceDistance(BatSeq, closestrecordseq): 
    Seq1 = BatSeq #seq1 is the bat sequence or the sequence that you want to compare to
    Seq2 = closestrecordseq 
    counter = 0
    matches = 0
    while counter <=len(Seq1): #this goes through the sequence character by character and compares them
        NT1 =Seq1[counter:counter+1]
        NT2 =Seq2 [counter:counter+1]
        counter+=1
        if NT1 == NT2: #if the nucleotide is the same it will add 1 to the matches counter
            if NT1 !="": #this ensures that even if there is nothing in the two sequences it wont give a value
                    matches+=1
    Distance = 1 -(matches/len(Seq1)) #distance equation
    return Distance


def FindClosestRecord(BatSeq, Records): #function is given two parameters the BatSequence and the Records list of list given in supplied code
    Seq1 = BatSeq
    smallestdistance=1 #variable that is here so the distance can be compared to something
    listnosmall=0 #list that has the smallest distance
    positioninlist=0 #our position in the list so that we know which sequence has which ID and comes from which country
    for x in Records: #goes through list of list and sets the list=x
        Seq2 = x[2]
        counter = 0
        matches = 0
        while counter <=len(Seq1): #compares sequence nucleotide by nucleotide and sees if there are matches
                NT1 =Seq1[counter:counter+1]
                NT2 =Seq2[counter:counter+1]
                counter+=1
                if NT1 == NT2:
                    if NT1 !="":
                        matches+=1 
        Distance = 1 -(matches/len(Seq1)) 
        if Distance<smallestdistance: #if the distance is smaller than 1 then the variable smallestdistance is changed.
            smallestdistance=Distance #as we go through the loop the smallest distance is compared to the next and only if it is smaller will the variable smallest distance be replaced.
            listnosmall=positioninlist
        positioninlist+=1 #this adds one to show where we are in the list of lists
    return Records[listnosmall]


def FilterbyCountry(Records, country):
    countrylist=[] #creates a list that shows the sequences from the same countries
    for x in Records: #goes through list of list and sets the list=x
        country2 = x[0]
        counter = 0
        if country2==country:
                        countrylist.append(x)
    return countrylist


#function that takes 3 parameters, Records (given list of lists), country which is the country we want, country 2 which is the country we are comparing to to see if it is the same as country
def PrintTransmitter(Records,country,country2):
    origincountry = FilterbyCountry(Records, country )
    targetcountry = FilterbyCountry(Records, country2)
    tempclosestvariable2=1
    closestoriginal=[] 
    closesttarget=[]
    for x in origincountry:
        tempclosestrecord= FindClosestRecord(x[2],targetcountry) #finds the smallest distance in the desired country
        tempclosestoriginal=x
        tempclosestdistance=SequenceDistance(tempclosestrecord[2], tempclosestoriginal[2]) #finds the distance between 
        if tempclosestdistance<tempclosestvariable2: #if the distance is lower than 1
            tempclosestvariable2=tempclosestdistance #then we make it equal to tempcclosestvariable2 which will then be compared again in the above statement
            closestoriginal=tempclosestoriginal 
            closesttarget=tempclosestrecord 
    print("ID of target sequence: ", closesttarget[1])
    print("ID of original sequence: ", closestoriginal[1])
    print("Distance: ", tempclosestvariable2)

# Results
closestrecord = FindClosestRecord(BatSeq, Records) 
print("Part 1")
print ("Country: ", closestrecord[0]) #DZA
print ("ID: ", closestrecord[1]) #022-NABAXH
print ("Distance: ", SequenceDistance(BatSeq, closestrecord[2])) #0.04601206434316352
print("Part 2") #this part takes a long time
PrintTransmitter(Records, "EST","UZB") #ID of target sequence:  009-ZMWJCM
#ID of original sequence:  001-DIZIJO
#Distance:  0.04557640750670244