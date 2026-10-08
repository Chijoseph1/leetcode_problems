def longest_substring1(word):
    remove_duplicate =set(word)
    return len(remove_duplicate)

def longest_substring2(word):
    result = []
    for n in word:
        if n in result:
            continue
        else:
            result.append(n)
    return len(result)

word = "abbbb"
print(longest_substring1(word))
print(longest_substring2(word))

