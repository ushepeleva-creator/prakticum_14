def count_holes(word: str) -> int:
    """
    Counts the number of letters in a word that contain enclosed spaces (holes).

    The function checks each character in the word against a predefined set
    of letters that have holes: {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}.

    Args:
        word (str): The input word to analyze for holes

    Returns:
        int: The number of characters in the word that contain holes
    """
    letter = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    return sum(1 for ch in word if ch in letter)

text = input()
words = text.split()
count_with_holes = 0
count_without_holes = 0
words_with_two_or_more_holes = []
for word in words:
    holes = count_holes(word)
    count_with_holes += holes
    count_without_holes += (len(word) - holes)
    if holes >= 2:
        words_with_two_or_more_holes.append(word)
print(count_with_holes)
print(count_without_holes)
print(words_with_two_or_more_holes)
