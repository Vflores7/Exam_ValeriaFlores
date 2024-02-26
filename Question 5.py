def find_pattern_occurrences(text):

    count = 0


    for i in range(len(text) - 4):

        if text[i:i + 2] == 'un' and text[i + 2:i + 4] == 'an':
            count += 1

    return count