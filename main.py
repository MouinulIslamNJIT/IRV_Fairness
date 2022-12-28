
from run import runRealData, runDummyData

def main():
    # To test on real dataset specify input file directory
    path = "Data/USIRV"
    #path = "Data/NSW"
    runRealData(path)



if __name__ == '__main__':
    main()
