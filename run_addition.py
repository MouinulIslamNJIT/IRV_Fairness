


import os
import timeit
from ProcessInput import readInput,createDummyInput
from Utils import IRV
from BlomMargin_addition import BlomMargin
from OurMargin_addition import OurMargin
from LRM_addition import LRM



def runRealData(path):
    result = "Dataset," \
             "Number_Of_Candidates," \
             "Number_of_voters," \
             "Max_Ballot_length," \
             "Upper_Bound," \
             "Our_margin," \
             "Blom_margin," \
             "Correct," \
             "Our_runtime," \
             "Blom_runtime," \
             "Our_number_LPS," \
             "Blom_number_LPS," \
             "Our_number_node_explored," \
             "Blom_number_node_explored," \
             "Our_lb_worng\n"


    f = open("result.csv", "w")
    f.write(result)







    dir_list = os.listdir(path)
    print(dir_list)
    #dir_list = ['Berkeley_2010_D1CityCouncil.txt']
    #dir_list = ['Berkeley_2010_D1CityCouncil.txt']

    for inputfile in dir_list:

        if inputfile.__contains__(".txt") == False:
            continue
        datasetName = inputfile.split(".")[0]
        fileName = path +"/"+ inputfile
        B,C,n,maxBLen = readInput(fileName)

        pi = IRV(B,C)
        cw = pi[n-1]
        numVoters = sum(B.values())
        ub = LRM(B,C)


        result = ""
        result =  result + datasetName + ","
        result =  result + str(n) + ","
        result =  result + str(numVoters) + ","
        result =  result + str(maxBLen) + ","
        result = result + str(ub) + ","


        print("################# Election ########################")
        print("Dataset Name = ",datasetName)
        print("Number of candidates = ",n)
        print("Number of voters = ",numVoters)
        print("Max ballot length = ",maxBLen)
        print("Upper bound = ",ub)

        ################################################# BLOM #########################################################

        ourMargin = OurMargin()
        start = timeit.default_timer()
        marginOurs = ourMargin.marginOurs(C,B,cw)
        end = timeit.default_timer()
        runtimeOurs = end - start
        print("################# Our Result ########################")
        print("margin  = ", marginOurs)
        print("run time = ", runtimeOurs)
        print("number of nodes explored = ",ourMargin.nodeExplored)
        print("number of nodes explored = ",ourMargin.numLP)



        ###################################################### OURS ####################################################

        blomMargin = BlomMargin()
        start = timeit.default_timer()
        marginBlom = blomMargin.marginBlom(C,B,cw)
        end = timeit.default_timer()
        runtimeBlom = end - start
        print("################# Blom Result ########################")
        print("margin  = ", marginBlom)
        print("run time = ", runtimeBlom)
        print("number of nodes explored = ",blomMargin.nodeExplored)
        print("number of nodes explored = ",blomMargin.numLP)

        ##########################################################################################################
        correct = 1
        if marginOurs != marginBlom:
            print("error in calculation")
            correct = 0



        result =  result + str(marginOurs) + ","
        result =  result + str(marginBlom) + ","
        result =  result + str(correct) + ","
        result =  result + str(runtimeOurs) + ","
        result =  result + str(runtimeBlom) + ","
        result =  result + str(ourMargin.numLP) + ","
        result =  result + str(blomMargin.numLP) + ","
        result =  result + str(ourMargin.nodeExplored) + ","
        result =  result + str(blomMargin.nodeExplored) + ","
        result = result + str(ourMargin.lbNotEq) + "\n"

        f.write(result)



    f.close()


def runDummyData(numIt,numCand,numSig,bsize,fixed,bPerSig):
    result = "Dataset," \
             "Number_Of_Candidates," \
             "Number_of_voters," \
             "Max_Ballot_length," \
             "Upper_Bound," \
             "Our_margin," \
             "Blom_margin," \
             "Correct," \
             "Our_runtime," \
             "Blom_runtime," \
             "Our_number_LPS," \
             "Blom_number_LPS," \
             "Our_number_node_explored," \
             "Blom_number_node_explored\n"

    f = open("result_random_bs=3_vary_n.csv", "w")
    f.write(result)

    for it in range(0,numIt):
        numCand = bsize + it % 10

        B,C = createDummyInput(numCand,numSig,bsize,fixed,bPerSig,it)

        datasetName = "Dummy_"+str(it)
        pi = IRV(B, C)
        n = len(C)
        maxBLen = bsize
        cw = pi[n - 1]
        numVoters = sum(B.values())
        ub = LRM(B, C)

        result = ""
        result = result + datasetName + ","
        result = result + str(n) + ","
        result = result + str(numVoters) + ","
        result = result + str(maxBLen) + ","
        result = result + str(ub) + ","

        print("################# Election ########################")
        print("Dataset Name = ", datasetName)
        print("Number of candidates = ", n)
        print("Number of voters = ", numVoters)
        print("Max ballot length = ", maxBLen)
        print("Upper bound = ", ub)


        ################################################# Ours #########################################################

        ourMargin = OurMargin()
        start = timeit.default_timer()
        marginOurs = ourMargin.marginOurs(C, B, cw)
        end = timeit.default_timer()
        runtimeOurs = end - start
        print("################# Our Result ########################")
        print("margin  = ", marginOurs)
        print("run time = ", runtimeOurs)
        print("number of nodes explored = ", ourMargin.nodeExplored)
        print("number of nodes explored = ", ourMargin.numLP)

        ###################################################### Bloms ####################################################

        blomMargin = BlomMargin()
        start = timeit.default_timer()
        marginBlom = blomMargin.marginBlom(C, B, cw)
        end = timeit.default_timer()
        runtimeBlom = end - start
        print("################# Blom Result ########################")
        print("margin  = ", marginBlom)
        print("run time = ", runtimeBlom)
        print("number of nodes explored = ", blomMargin.nodeExplored)
        print("number of nodes explored = ", blomMargin.numLP)

        ##########################################################################################################
        correct = 1
        if marginOurs != marginBlom:
            print("error in calculation")
            correct = 0

        result = result + str(marginOurs) + ","
        result = result + str(marginBlom) + ","
        result = result + str(correct) + ","
        result = result + str(runtimeOurs) + ","
        result = result + str(runtimeBlom) + ","
        result = result + str(ourMargin.numLP) + ","
        result = result + str(blomMargin.numLP) + ","
        result = result + str(ourMargin.nodeExplored) + ","
        result = result + str(blomMargin.nodeExplored) + "\n"

        f.write(result)

    f.close()

#path = "USIRV"
path = "NSW"

runRealData(path)


#numIt,numCand,numSig,bsize,fixed,bPerSig
#runDummyData(100,10,500,3,1,10)