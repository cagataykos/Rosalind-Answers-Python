
#steps 1) get dna Strings convert the dna strings in to 2 elements of list and compare them
dna1_lst = []
dna2_lst = []
count_point_mutations= []
def mutations(infile):
    with open(infile, "r") as in_f:
        dna_strings = in_f.readlines()
        dna_strings = [i.strip() for i in dna_strings]
        dna_1 = dna_strings[0]
        dna_2 = dna_strings[1]
        for i in dna_1:
            dna1_lst.append(i)
        for i in dna_2:
            dna2_lst.append(i)
        if len(dna1_lst) != len(dna2_lst):
            print("two DNA is not equal")
        else:
            for x,y in zip(dna1_lst,dna2_lst):
                if x != y :
                    count_point_mutations.append(x)
            print(f" Total Number of Point Mutations  {len(count_point_mutations)}")

mutations("test-point-mutations.txt")