def compare_files(words1, words2):

    common_words = []

    for word in words1:
        if word in words2 and word not in common_words:
            common_words.append(word)

    if len(words1) == 0 or len(words2) == 0:
        similarity = 0

    else:
        percentage1 = (
            len(common_words) / len(words1)
        ) * 100

        percentage2 = (
            len(common_words) / len(words2)
        ) * 100

        similarity = (
            percentage1 + percentage2
        ) / 2

    phrases = []

    for i in range(len(words1) - 1):

        phrase = (
            words1[i]
            + " "
            + words1[i + 1]
        )

        for j in range(len(words2) - 1):

            phrase2 = (
                words2[j]
                + " "
                + words2[j + 1]
            )

            if phrase == phrase2 and phrase not in phrases:
                phrases.append(phrase)

    return common_words, round(similarity, 2), phrases


def display_result(
    file1,
    file2,
    total_words1,
    total_words2,
    common_words,
    similarity
):

    print("\n==============================")
    print("     PLAGIARISM RESULT")
    print("==============================")

    print("File 1:", file1)
    print("File 2:", file2)

    print(
        "Total words in",
        file1,
        ":",
        total_words1
    )

    print(
        "Total words in",
        file2,
        ":",
        total_words2
    )

    print(
        "Common words:",
        len(common_words)
    )

    print(
        "Similarity:",
        similarity,
        "%"
    )

    if similarity >= 80:
        print("Result: Very high similarity")

    elif similarity >= 50:
        print("Result: Moderate similarity")

    else:
        print("Result: Low similarity")

    bar_length = 20

    filled = int(
        (similarity / 100) * bar_length
    )

    bar = (
        "█" * filled
        + "-" * (bar_length - filled)
    )

    print("Similarity Percentage:")
    print(
        "[" + bar + "]",
        similarity,
        "%"
    )

    print("==============================")


def find_common_words_all(clean_word_lists):

    if len(clean_word_lists) == 0:
        return []

    common_words = []

    for word in clean_word_lists[0]:

        if word not in common_words:

            found_in_all = True

            for words in clean_word_lists[1:]:

                if word not in words:
                    found_in_all = False
                    break

            if found_in_all:
                common_words.append(word)

    return common_words