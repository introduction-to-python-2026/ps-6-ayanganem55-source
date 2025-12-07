def create_codon_dict(file_path):
 
    codon_dict = {}     

   
    with open(file_path, 'r') as file:                 
        for line in file:             
        
      g/trailing whitespace (especiall   
            parts = line.strip().split('\t')             
            
            
            if len(parts) >= 3:                
                codon = parts[0]         
                codon_dict[codon] = amino_acid     
                
    return codon_dict


