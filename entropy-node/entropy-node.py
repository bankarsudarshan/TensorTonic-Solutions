import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if not y:
        return 0.0
    from collections import Counter
    cnt = Counter(y)
    probabilities = np.array([freq/len(y) for freq in cnt.values()])
    log_probabilities = np.log2(probabilities)
    return -sum(probabilities * log_probabilities)