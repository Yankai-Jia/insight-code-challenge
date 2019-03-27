import time
import sys
from data_process import Processor

def pharmacy_counting():
    start_time = time.time()
    processor = Processor(input_file,output_file)
    processor.process()
    print("program executed: %s" %(time.time() - start_time))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("Usage: python3 ./src/pharmacy_counting.py\n\
        ./input/itcont.txt\n\
        ./output/top_cost_drug.txt")
        input_file = input("input_file：")
        output_file = input("oput_file：")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    pharmacy_counting()
