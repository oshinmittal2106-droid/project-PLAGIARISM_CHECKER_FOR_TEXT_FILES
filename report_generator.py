def save_report(
    file1,
    file2,
    total_words1,
    total_words2,
    common_words,
    similarity,
    phrases
):

    with open("plagiarism_report.txt", "a") as file:

        file.write("\n")
        file.write("Comparing " + file1 + " and " + file2 + "\n")
        file.write(
            "Total words in "
            + file1
            + ": "
            + str(total_words1)
            + "\n"
        )
        file.write(
            "Total words in "
            + file2
            + ": "
            + str(total_words2)
            + "\n"
        )

        file.write(
            "Common words: "
            + str(common_words)
            + "\n"
        )

        file.write(
            "Number of common words: "
            + str(len(common_words))
            + "\n"
        )

        file.write(
            "Similarity: "
            + str(similarity)
            + "%\n"
        )

        file.write(
            "Repeated phrases: "
            + str(phrases)
            + "\n"
        )

        file.write(
            "Number of repeated phrases: "
            + str(len(phrases))
            + "\n"
        )


        if similarity >= 80:

            file.write(
                "Result: Very high similarity\n"
            )

        elif similarity >= 50:

            file.write(
                "Result: Moderate similarity\n"
            )

        else:

            file.write(
                "Result: Low similarity\n"
            )


def save_word_analysis(
    file1,
    file2,
    common_list,
    unique_file1,
    unique_file2
):

    with open("plagiarism_report.txt", "a") as file:

        file.write("\n")
        file.write("WORD ANALYSIS\n")
        file.write("-------------------------\n")

        file.write(
            "Comparing "
            + file1
            + " and "
            + file2
            + "\n"
        )

        file.write("Common words:\n")
        file.write(str(common_list) + "\n")

        file.write(
            "Words only in "
            + file1
            + ":\n"
        )

        file.write(str(unique_file1) + "\n")

        file.write(
            "Words only in "
            + file2
            + ":\n"
        )

        file.write(str(unique_file2) + "\n")