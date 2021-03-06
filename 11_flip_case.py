def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    swap = to_swap.lower()

    result = ""

    for letter in phrase:
        if letter.isupper() and letter.lower() == swap:
            result += letter.lower() 
        elif letter.islower() and letter == swap:
            result += letter.upper()
        else: 
            result += letter

    return result

        






