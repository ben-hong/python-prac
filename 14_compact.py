def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """


    result = []

    for element in lst:
        if element:
            result.append(element)

    return result
    
    