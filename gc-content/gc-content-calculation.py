#GC-content calculation from fasta file within multiple labelled DNA seq

seq = {}
def get_id(input):
    with open(input,"r") as id_dna:
        for line in id_dna:
            line=line.strip()
            if line.startswith(">"):
                id_seq = line
                seq[id_seq]=""
            else:
                seq[id_seq]+=line
        for i,k in seq.items():
            total_nuc = int(len(k))
            total_g = int(k.count("G"))
            total_c = int(k.count("C"))
            total_gc=total_g+total_c
            gc_calculation = total_gc / total_nuc
            gc_calculation= gc_calculation*100

            print(f"{i}\n{round(gc_calculation,3)}")


get_id("test.fasta")

