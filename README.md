# Pharmacy counting
This project is to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which would be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order. It is developed in Python.
# Table of Contents
1. [Problem](README.md#problem)
    1. [Input]( README.md#input )
    2. [Output]( README.md#output )
    3. [Challenge]( README.md#challenge )
2. [Approach]( README.md#approach )
    1. [Program Structure]( README.md#Program Structure )
    2. [Time Complexity](README.md#Time Complexity )
3. [Run instructions]( README.md#Run instructions)

# Problem
## Input
Input dataset provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name. It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication.

## Output
The program creates one output file:
 * `top_cost_drug.txt`: a list contains drug, number of prescriber and total cost. And it is listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order.

## Challenges
1. The dataset cannot be split just by comma. It may have cases like `1508809740,ABRAMOVICI,BERNARD,"PANCRELIPASE 5,000 , ACN",1344.95`.
2. It is a large dataset. Need do unit test to check the data first to know the possible types of the data.
3. Sort the list by two rules.

# Approach
## Program Structure
The program contains three source files:
* `unit_test.py`: to check the possible types of the dataset.
* `data_process.py`: to do data processing. It contains two parts. First part to do preprocessing. Based on the result we get from `unit_test.py`, preprocess the raw data with different cases to one uniform format.
Second, store the data into a map. Set the drug name as the key, a list of other information as the value. The structure of the map is {drug_name:[drug_num,{set of name of prescriber}, cost_of_drug]}.
* `pharmacy_counting.py`: The entrance of the program. Compute processing time.

## Time Complexity
In preprocessor, the most time consuming part is to split a line with comma. Total time is O(n), n denotes the number of letters in the input file. Other operations are based on hash table with O(1) time.

In data processing part, the time to loop all events is O(m), here m denotes the number of line.

And sorting time is O(klogk), k is the number of drug.

# Run instructions
Make sure `./output` directory and `./input/incont.txt` in current directory.

Run by `sh run.sh`
