import collections

class Processor(object):
    def __init__(self, inputfile, outputfile):
        self.drug_map = collections.defaultdict(list)
        self.input_file = inputfile
        self.output_file = outputfile
    def process(self):
        input_file_name = self.input_file.split('/')[-1]
        print("Start processing",input_file_name, '...')
        # read the dataset
        with open(self.input_file) as file:
            next(file)
            for i,line in enumerate(file):
                # if i < 12000000:
                #     continue
                # if i == 5157:
                #     print ("error line",line)

                #preprocessing. some drug name or customer's names may contain ',' , so do preprocess to solve this problem.
                if '"' in line:
                    pre_content = line.split(',')
                    for j, item in enumerate(pre_content):
                        if item[0] == '"':
                            t = 1
                            while pre_content[j+t][-1] != '"':
                                item = item +","+ pre_content[j+t]
                                t += 1
                            item = item +","+ pre_content[j+t]
                            pre_content[j] = item
                            del pre_content[j+1:j+t+1]
                    content = pre_content
                    # print(content)
                #processing
                elif '"' not in line:
                    content = line.split(",")
                # store data into a map. {drug_name:[drug_num,{set of name of prescriber}, cost_of_drug]}
                if content[3] not in self.drug_map:
                    self.drug_map[content[3]].append(content[3])
                    self.drug_map[content[3]].append({content[1]+content[2]})
                    self.drug_map[content[3]].append(float(content[4]))
                else:
                    self.drug_map[content[3]][1].add(content[1]+content[2])
                    self.drug_map[content[3]][2] += float(content[4])
                # randomly test the dataset
                if i>12000000:
                    break
        #sort the map's values by
        # sorted_drug_map = sorted(sorted(self.drug_map.values(), key = lambda kv:kv[2], reverse = True), key = lambda kv:kv[1])
        sorted_drug_map = sorted(sorted(self.drug_map.values(), key = lambda kv:kv[2], reverse = True),key = lambda kv:kv[1])

        # create the processed file.
        output = open(self.output_file,'w')
        output.write('drug_name,num_prescriber,total_cost\n')
        for i in sorted_drug_map:
            #After testing, find decimals is not important, so I choose round the number of drug cost.
            # This is a way to display the precise numer of drug cost. i[2] = [str(i[2]),int(i[2])][int(i[2])==i[2]]
            i[2]=round(i[2])
            line = i[0]+","+str(len(i[1]))+","+str(i[2])
            output.writelines(line+'\n')
        output.close()
