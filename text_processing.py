def count_word_frequency(words):

    freq = {}

    for word in words:

        if word in freq:
            freq[word] = freq[word] + 1

        else:
            freq[word] = 1

    return freq


def clean_words(words):

    new_words = []

    for word in words:

        word = word.strip(".,!?;:'\"()[]{}")

        if word != "":
            new_words.append(word)

    return new_words


def count_unique_words(words):

    unique_words = set(words)

    return len(unique_words)


def find_word_length(words):

    if len(words) == 0:

        return "", ""

    longest_word = words[0]
    shortest_word = words[0]

    for word in words:

        if len(word) > len(longest_word):

            longest_word = word

        if len(word) < len(shortest_word):

            shortest_word = word

    return longest_word, shortest_word


def search_word(words, search):

    count = 0

    for word in words:

        if word == search:

            count = count + 1

    return count


def find_common_words(words1, words2):

    common_words = []

    for word in words1:

        if word in words2 and word not in common_words:

            common_words.append(word)

    return common_words


def find_unique_words(words1, words2):

    unique_words = []

    for word in words1:

        if word not in words2 and word not in unique_words:

            unique_words.append(word)

    return unique_words