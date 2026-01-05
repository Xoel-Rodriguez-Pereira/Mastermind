from src.constants import CODE_LENGHT

def reproduction (parents, values):

    DAD = 0
    MUM = 1
    gene_midle = CODE_LENGHT // 2
    return [values[couple[DAD]][:gene_midle] + values[couple[MUM]][gene_midle:] for couple in parents] + \
           [values[couple[DAD]][gene_midle:] + values[couple[MUM]][:gene_midle] for couple in parents]
 
