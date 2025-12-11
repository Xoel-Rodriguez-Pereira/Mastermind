
def reproduction (parents, values):

    DAD = 0
    MUM = 1
    return [values[couple[DAD]][:2] + values[couple[MUM]][2:] for couple in parents] + \
           [values[couple[DAD]][2:] + values[couple[MUM]][:2] for couple in parents]
 
