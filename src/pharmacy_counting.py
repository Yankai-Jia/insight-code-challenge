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
        input_file = input("Please enter input file path：")
        output_file = input("Please enter output file path：")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    pharmacy_counting()
