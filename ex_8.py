def sort_string(st: str) -> str:
    """
    Sorts the characters in a string in alphabetical/Unicode order.

    The function converts the string to a list of characters, sorts them
    in ascending order , and then joins them back into a string.

    Args:
        st (str): The input string to be sorted

    Returns:
        str: A new string with characters sorted in ascending order
    """
    chars = list(st)
    chars.sort()
    return ''.join(chars)


text = input("Enter a text: ")
print(sort_string(text))
