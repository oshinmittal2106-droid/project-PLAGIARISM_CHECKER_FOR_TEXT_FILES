
import matplotlib.pyplot as plt


def display_graph(files, clean_word_lists, pair_results, common_all):
    file_labels = []

    for file_name in files:
        file_labels.append(file_name)

    file_labels.append("Common in All")

    word_values = []

    for words in clean_word_lists:
        word_values.append(len(words))

    word_values.append(len(common_all))

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)

    plt.bar(file_labels, word_values)

    plt.xlabel("Files")
    plt.ylabel("Number of Words")
    plt.title("Word Count Comparison")

    for i in range(len(word_values)):
        plt.text(
            i,
            word_values[i],
            str(word_values[i]),
            ha="center",
            va="bottom"
        )

    similarity_labels = []
    similarity_values = []

    for result in pair_results:
        similarity_labels.append(result[0] + " vs " + result[1])
        similarity_values.append(result[2])

    plt.subplot(2, 1, 2)

    plt.bar(similarity_labels, similarity_values)

    plt.xlabel("File Comparisons")
    plt.ylabel("Similarity (%)")
    plt.title("Pairwise Similarity")

    for i in range(len(similarity_values)):
        plt.text(
            i,
            similarity_values[i],
            str(similarity_values[i]) + "%",
            ha="center",
            va="bottom"
        )

    plt.xticks(rotation=30)

    plt.figtext(
        0.5,
        0.01,
        "Files compared: " + str(len(files)) +
        "    Total comparisons: " + str(len(pair_results)),
        ha="center"
    )

    plt.tight_layout(rect=[0, 0.04, 1, 1])

    plt.show()