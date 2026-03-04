import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    from collections import Counter
    cnt = Counter(tokens)
    bow = np.zeros(len(vocab), dtype=np.int_)
    for i in range(len(vocab)):
        bow[i] = cnt[vocab[i]]
    return bow