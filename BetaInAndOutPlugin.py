import PyPluMA

class BetaInAndOutPlugin:
    def input(self, inputfile):
       self.parameters = dict()
       paramfile = open(inputfile, 'r')
       for line in paramfile:
           contents = line.strip().split('\t')
           self.parameters[contents[0]] = contents[1]

    def run(self):
        csvfile = open(PyPluMA.prefix()+"/"+self.parameters['csvfile'], 'r')
        metafile = open(PyPluMA.prefix()+"/"+self.parameters['metadata'], 'r')
        header = metafile.readline()
        headercontents = header.strip().split(',')
        sample_idx = headercontents.index("\"Sample\"")
        group_idx = headercontents.index("\"Group\"")

        groups = dict()
        group_list = []
        for line in metafile:
           contents = line.strip().split(',')
           sample = contents[sample_idx]
           group = contents[group_idx]
           if (group in groups):
               groups[group].append(sample)
           else:
               group_list.append(group)
               groups[group] = [sample]

        csvfile.readline()
        self.values = dict()
        # Assume: Sample1, Sample2, Value
        for i in range(len(group_list)):
            self.values[group_list[i]] = []
        self.values["\"out\""] = []

        for line in csvfile:
            contents = line.strip().split(',')
            sample1 = contents[0]
            sample2 = contents[1]
            value = contents[2]
            group_idx1 = -1
            group_idx2 = -1
            for i in range(len(group_list)):
                if (sample1 in groups[group_list[i]]):
                   group_idx1 = i
                if (sample2 in groups[group_list[i]]):
                   group_idx2 = i
            if (group_idx1 == group_idx2):
               self.values[group_list[group_idx1]].append(value)
            else:
               self.values["\"out\""].append(value)

    def output(self, filename):
       outfile = open(filename, 'w')
       for group1 in self.values:
          outfile.write(group1+',')
          for i in range(len(self.values[group1])):
              outfile.write(self.values[group1][i])
              if (i == len(self.values[group1])-1):
                  outfile.write('\n')
              else:
                  outfile.write(',')



