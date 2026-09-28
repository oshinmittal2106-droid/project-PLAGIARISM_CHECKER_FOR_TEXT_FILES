from file_handler import check_file, read_file
from text_processing import clean_words
from text_processing import count_word_frequency
from text_processing import count_unique_words
from text_processing import find_word_length
from text_processing import search_word
from text_processing import find_common_words
from text_processing import find_unique_words
from plagiarism_checker import compare_files
from plagiarism_checker import display_result
from plagiarism_checker import find_common_words_all
from visualization import display_graph
from report_generator import save_report
from report_generator import save_word_analysis


# PLAGIARISM CHECKER FOR TEXT FILES
print("**********************")
print("  PLAGIARISM CHECKER")
print("**********************")
print("Welcome to PLAGIARISM CHECKER!")


files = []
documents = []
word_lists = []
clean_word_lists = []
word_freq = []
pair_results = []
common_all = []
all_phrases = []
highest_result = None

while True:
    print("\n******************")
    print("     MAIN MENU")
    print("******************")
    print("1. Check plagiarism")
    print("2. View saved report")
    print("3. Display plagiarism result")
    print("4. Display similarity graph")
    print("5. Display highest similarity")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        
        try:
            no_of_files = int(input("Enter number of text files: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if no_of_files < 2:
            print("Please enter at least two files.")
            continue

        if no_of_files > 50:
            print("Please enter a maximum of 50 files.")
            continue

        files = []
        documents = []
        word_lists = []
        clean_word_lists = []
        word_freq = []
        pair_results = []
        common_all = []
        all_phrases = []
        highest_result = None

        print("\nEnter the names of the text files.")

        for i in range(no_of_files):
            file_name = input(
                "Enter the name of file " + str(i + 1) + ": "
            )
            files.append(file_name)

        print("\nFiles Selected:")

        for file_name in files:
            print(file_name)

        duplicate_found = False

        for i in range(len(files)):
            for j in range(i + 1, len(files)):
                if files[i] == files[j]:
                    duplicate_found = True

        if duplicate_found:
            print("Warning: Same file name entered more than once.")

        valid_files = True

        for file_name in files:
            if check_file(file_name):
                content = read_file(file_name)
                documents.append(content)
            else:
                print("Please enter a valid file")
                valid_files = False
                break

        if not valid_files:
            print("File checking stopped.")
            continue

        print("\nAll files are valid.")

        for document in documents:
            words = document.lower().split()
            word_lists.append(words)

        print("Text processing completed.")

        for words in word_lists:
            new_words = clean_words(words)
            clean_word_lists.append(new_words)

        print("Punctuation removed successfully.")

        for words in clean_word_lists:
            frequency = count_word_frequency(words)
            word_freq.append(frequency)

        print("Word frequency calculated successfully.")

        common_all = find_common_words_all(clean_word_lists)

        print("\nCOMMON WORDS IN ALL FILES")
        print(common_all)
        print(
            "Number of common words in all files:",
            len(common_all)
        )

        # Creating a new report for every plagiarism check
        with open("plagiarism_report.txt", "w") as file:
            file.write("PLAGIARISM CHECKER REPORT\n")
            file.write("=========================\n")

        for i in range(no_of_files):
            for j in range(i + 1, no_of_files):
                common_words, similarity, phrases = compare_files(
                    clean_word_lists[i],
                    clean_word_lists[j]
                )

                pair_results.append(
                    (files[i], files[j], similarity)
                )

                current_result = (
                    files[i],
                    files[j],
                    len(clean_word_lists[i]),
                    len(clean_word_lists[j]),
                    common_words,
                    similarity
                )

                # Storing the pair with the highest similarity
                if highest_result is None:
                    highest_result = current_result
                elif similarity > highest_result[5]:
                    highest_result = current_result

                print("\n------------------------------")
                print(
                    "Comparing",
                    files[i],
                    "and",
                    files[j]
                )
                print("------------------------------")

                print(
                    "Total words in",
                    files[i],
                    ":",
                    len(clean_word_lists[i])
                )

                print(
                    "Total words in",
                    files[j],
                    ":",
                    len(clean_word_lists[j])
                )

                print(
                    "Common words:",
                    len(common_words)
                )

                common_list = find_common_words(
                    clean_word_lists[i],
                    clean_word_lists[j]
                )

                unique_file1 = find_unique_words(
                    clean_word_lists[i],
                    clean_word_lists[j]
                )

                unique_file2 = find_unique_words(
                    clean_word_lists[j],
                    clean_word_lists[i]
                )

                print("Common words list:", common_list)

                print(
                    "Words only in",
                    files[i],
                    ":",
                    unique_file1
                )

                print(
                    "Words only in",
                    files[j],
                    ":",
                    unique_file2
                )

                print("Similarity:", similarity, "%")
                print("Repeated phrases:", phrases)
                print(
                    "Number of repeated phrases:",
                    len(phrases)
                )

                all_phrases.append(
                    (files[i], files[j], phrases)
                )

                # Giving a result based on similarity
                if similarity >= 80:
                    print("Result: Very high similarity")
                elif similarity >= 50:
                    print("Result: Moderate similarity")
                else:
                    print("Result: Low similarity")

                save_report(
                    files[i],
                    files[j],
                    len(clean_word_lists[i]),
                    len(clean_word_lists[j]),
                    common_words,
                    similarity,
                    phrases
                )

                save_word_analysis(
                    files[i],
                    files[j],
                    common_list,
                    unique_file1,
                    unique_file2
                )

        print("\nWORD FREQUENCY")

        for i in range(no_of_files):
            print("\nWord frequency in", files[i])

            for word in word_freq[i]:
                print(
                    word,
                    ":",
                    word_freq[i][word]
                )

        print("\nFILE STATISTICS")

        for i in range(no_of_files):
            unique_words = count_unique_words(
                clean_word_lists[i]
            )

            longest_word, shortest_word = find_word_length(
                clean_word_lists[i]
            )

            print("\nFile:", files[i])

            print(
                "Total words:",
                len(clean_word_lists[i])
            )

            print(
                "Unique words:",
                unique_words
            )

            print(
                "Longest word:",
                longest_word
            )

            print(
                "Shortest word:",
                shortest_word
            )

        print("\nWORD SEARCH")

        search = input("Enter a word to search: ")
        search = search.lower()

        for i in range(no_of_files):
            count = search_word(
                clean_word_lists[i],
                search
            )

            print(
                search,
                "in",
                files[i],
                ":",
                count,
                "times"
            )

        print("\nPLAGIARISM CHECKING COMPLETED")
        print(
            "Total number of files checked:",
            no_of_files
        )

        total_comparisons = (
            no_of_files * (no_of_files - 1)
        ) // 2

        print(
            "Total comparisons made:",
            total_comparisons
        )

        if highest_result is not None:
            print(
                "\nHighest similarity:",
                highest_result[5],
                "%"
            )

            print(
                "Between",
                highest_result[0],
                "and",
                highest_result[1]
            )

        print("\nReport saved as plagiarism_report.txt")

    elif choice == "2":

        try:
            with open("plagiarism_report.txt", "r") as file:
                report = file.read()

                if report.strip() == "":
                    print("The report is empty.")

                else:
                    print("\n" + report)

        except FileNotFoundError:
            print(
                "No report found. Please check plagiarism first."
            )

    elif choice == "3":

        if highest_result is None:
            print("Please check plagiarism first.")

        else:
            file1 = highest_result[0]
            file2 = highest_result[1]
            total_words1 = highest_result[2]
            total_words2 = highest_result[3]
            common_words = highest_result[4]
            similarity = highest_result[5]

            display_result(
                file1,
                file2,
                total_words1,
                total_words2,
                common_words,
                similarity
            )

    elif choice == "4":

        if highest_result is None:
            print("Please check plagiarism first.")
        else:
            display_graph(
                files,
                clean_word_lists,
                pair_results,
                common_all
            )

    elif choice == "5":

        if highest_result is None:
            print("Please check plagiarism first.")

        else:
            file1 = highest_result[0]
            file2 = highest_result[1]
            total_words1 = highest_result[2]
            total_words2 = highest_result[3]
            common_words = highest_result[4]
            similarity = highest_result[5]

            print("\n==============================")
            print("     HIGHEST SIMILARITY")
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

    elif choice == "6":

        print("\nExiting program.....")
        print(
            "Thank you for using PLAGIARISM CHECKER!"
        )
        break

    else:

        print("\nInvalid choice.")
        print(
            "Please enter a number from 1 to 6."
        )