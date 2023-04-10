#get key, values of rna_protein
#assign values of rna_protein as a key in to  new dictionary:
#each keys of new dictionary should countain every represented codons

rna_protein = {"UUU": "F",     "CUU": "L",      "AUU": "I",    "GUU": "V",
                "UUC": "F",      "CUC": "L",      "AUC": "I",     "GUC": "V",
                "UUA": "L",     "CUA": "L",      "AUA": "I",      "GUA":"V",
                "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
                "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
                "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
                "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
                "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
                "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
                "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
                "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
                "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
                "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
                "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
                "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
                "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"}


proteins_dict = [x for x in rna_protein.values()]

proteins = []

for i in proteins_dict:
    if i not in proteins:
        proteins.append(i)

# for x,y in rna_protein.items():
#     new_dict = {}
#     for p in proteins:
#         if y == p:
#             new_dict[p] = rna_protein[x]
#     print(new_dict)

for x,y in rna_protein.items():
    for i in y:
        print(i)






        #new_dict[p]=[x for x in rna_protein()]
    #print(new_dict)

































