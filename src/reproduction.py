
def reproduction (parents, values):
    return [values[parents[couple][0]][:2] + values[parents[couple][1]][2:] for couple in parents]
 
