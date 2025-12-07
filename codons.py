def create_codon_dict(file_path):
    def create_codon_dict(file_path):           codon_dict = {}     
with open(file_path, 'r') as file:                 for line in file:             
parts = line.strip().split('\t')             
if len(parts) >= 3:                
codon = parts[0]                 amino_acid = parts[2]                 codon_dict[codon] = amino_acid     return codon_dict


