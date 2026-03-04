def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    from collections import Counter
    cnt = Counter()
    for sentence in sentences:
        cnt.update(sentence)
    return dict(cnt)