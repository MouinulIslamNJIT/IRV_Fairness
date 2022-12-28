


import os
import timeit
from ProcessInput import readInput,createDummyInput
from Utils import IRV
from BlomMargin import BlomMargin
from OurMargin import OurMargin
from LRM import LRM
from OurUB import upperBound
from OurHeuristicV1 import heuristic


def runRealData(path):
    result = "Dataset," \
             "Number_Of_Candidates," \
             "Number_of_voters," \
             "Max_Ballot_length," \
             "Preferred_winner," \
             "Upper_Bound," \
             "heuristic_margin," \
             "Our_margin," \
             "Blom_margin," \
             "Margin_correct," \
             "Upper_bound_correct," \
             "Heuristic_equl_margin," \
             "Our_runtime," \
             "Blom_runtime," \
             "Our_number_LPS," \
             "Blom_number_LPS," \
             "Our_number_node_explored," \
             "Blom_number_node_explored," \
             "Our_bl_calls," \
             "Blom_Leaf_node_explored\n"


    f = open("result/testlb10.csv", "w")
    f.write(result)

    dir_list = os.listdir(path)
    print(dir_list)

    #dir_list = ['Data_NA_Auburn.txt_ballots.txt', 'Data_NA_Ballina.txt_ballots.txt', 'Data_NA_Balmain.txt_ballots.txt', 'Data_NA_Bankstown.txt_ballots.txt', 'Data_NA_Barwon.txt_ballots.txt']#['Data_NA_Murray.txt_ballots.txt']

    for inputfile in dir_list:

        if inputfile.__contains__(".txt") == False:
            continue
        datasetName = inputfile.split(".")[0]
        fileName = path +"/"+ inputfile
        B,C,n,maxBLen = readInput(fileName)

        for cw in C:

            numVoters = sum(B.values())
            ub = upperBound(B,C,cw)
            heuristic_margin = heuristic(B,C,cw)

            result = ""
            result =  result + datasetName + ","
            result =  result + str(n) + ","
            result =  result + str(numVoters) + ","
            result =  result + str(maxBLen) + ","
            result = result + str(cw) + ","
            result = result + str(ub) + ","
            result = result + str(heuristic_margin) + ","


            print("################# Election ########################")
            print("Dataset Name = ",datasetName)
            print("Number of candidates = ",n)
            print("Number of voters = ",numVoters)
            print("Max ballot length = ",maxBLen)
            print("Preferred winner = ", cw)
            print("Upper bound = ",ub)
            print("heuristic margin = ",heuristic_margin)

            ################################################# ours #########################################################

            ourMargin = OurMargin()
            start = timeit.default_timer()
            marginOurs = ourMargin.marginOurs(C,B,cw)
            end = timeit.default_timer()
            runtimeOurs = end - start
            print("################# Our Result ########################")
            print("margin  = ", marginOurs)
            print("run time = ", runtimeOurs)
            print("number of nodes explored = ",ourMargin.nodeExplored)
            print("number of ILPs = ",ourMargin.numLP)



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
            print("number of ILPs = ",blomMargin.numLP)

            ##########################################################################################################
            marginCorrect = 1
            if marginOurs != marginBlom:
                print("error in margin calculation")
                marginCorrect = 0

            upperBoundCorrect = 1
            if marginBlom > ub:
                print("error in ub calculation")
                upperBoundCorrect = 0

            equal = 0
            if marginBlom == heuristic_margin:
                equal = 1


            result =  result + str(marginOurs) + ","
            result =  result + str(marginBlom) + ","
            result =  result + str(marginCorrect) + ","
            result = result + str(upperBoundCorrect) + ","
            result = result + str(equal) + ","
            result =  result + str(runtimeOurs) + ","
            result =  result + str(runtimeBlom) + ","
            result =  result + str(ourMargin.numLP) + ","
            result =  result + str(blomMargin.numLP) + ","
            result =  result + str(ourMargin.nodeExplored) + ","
            result = result + str(blomMargin.nodeExplored) + ","
            result = result + str(ourMargin.blomLBCall) + ","
            result =  result + str(blomMargin.branchExplored) + "\n"
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

    f = open("result_dummy.csv", "w")
    f.write(result)

    for it in range(0,numIt):

        bsize = it%10 + 1
        #numCand = 3 + it

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



 # To test dummy dataset specify following parameters.
# numIt,numCand,numSig,bsize,fixed,bPerSig
# runDummyData(100,10,500,10,1,10)