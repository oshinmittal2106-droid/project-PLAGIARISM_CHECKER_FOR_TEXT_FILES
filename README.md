# Plagiarism Checker for Text Files

## About

Plagiarism Checker for Text Files is a Python-based project that checks the basic similarity between multiple text files by comparing their words. The project reads and processes text files, converts text to lowercase, removes selected punctuation marks, calculates word frequency, finds common and unique words, calculates similarity percentage, detects repeated two-word phrases, and provides visual results.

The project can compare up to 50 text files at a time. It also identifies the pair of files with the highest similarity and finds words that are common in all selected files.

This project is developed as an educational tool for understanding Python programming concepts such as file handling, functions, lists, dictionaries, loops, conditional statements, exception handling, text processing, modular programming, and data visualization.

The project does not use an online database or advanced semantic analysis.

## Features

* Compares two or more text files
* Supports up to 50 text files at a time
* Validates file format, missing files, and empty files
* Reads and processes text files
* Converts text to lowercase
* Removes selected punctuation marks
* Calculates word frequency
* Counts unique words
* Finds common words between two files
* Finds words unique to each file
* Finds words common in all selected files
* Finds the longest and shortest words
* Searches for a specific word in each file
* Calculates basic word-based similarity percentage
* Detects repeated two-word phrases
* Displays similarity using a progress bar
* Identifies the pair of files with the highest similarity
* Displays word count comparison graph
* Displays pairwise similarity graph
* Saves plagiarism results to a text report
* Saves word analysis to the report
* Allows the saved report to be viewed from the main menu
* Uses separate Python modules for different tasks
* Includes input validation and error handling

## Project Structure

```text
Plagiarism Checker for Text Files/

│
├── main.py
├── file_handler.py
├── text_processing.py
├── plagiarism_checker.py
├── report_generator.py
├── visualization.py
├── README.md
├── statement.md
├── essay1.txt
├── essay2.txt
├── essay3.txt
└── plagiarism_report.txt
```

## Modules

### main.py

Controls the main program and menu. It takes user input, manages the workflow, calls the required functions, performs file comparisons, displays results, and connects all the modules.

### file_handler.py

Handles text file validation and reading. It checks whether the file is a `.txt` file, whether it exists, and whether it is empty.

### text_processing.py

Performs text processing operations such as cleaning punctuation, calculating word frequency, counting unique words, finding the longest and shortest words, searching for words, and finding common and unique words.

### plagiarism_checker.py

Compares selected files, calculates similarity, detects repeated two-word phrases, identifies common words, finds words common in all files, and displays plagiarism results.

### report_generator.py

Creates and updates the plagiarism report. It stores comparison results, similarity percentage, repeated phrases, common words, and word analysis.

### visualization.py

Creates graphs for word count comparison and pairwise similarity between files.

## How to Run

1. Make sure Python is installed on the computer.

2. Install Matplotlib using:

```text
pip install matplotlib
```

3. Open the project folder in VS Code.

4. Place the `.txt` files that need to be checked in the project folder.

5. Open `main.py`.

6. Run the program.

7. Select option `1` from the main menu.

8. Enter the number of text files to compare.

9. Enter the names of the text files.

10. The program processes and compares the files.

11. The results are displayed on the screen.

12. Other menu options can be used to view the saved report, plagiarism result, similarity graph, and highest similarity.

## Testing

The project was tested using different types of inputs and situations, including:

* Valid text files
* Multiple text files
* Missing files
* Invalid file extensions
* Empty files
* Invalid number of files
* More than 50 files
* Similar text files
* Different text files
* Word searching
* Word frequency
* Common and unique words
* Repeated phrases
* Similarity percentage
* Similarity progress bar
* Highest similarity pair
* Common words in all selected files
* Word count graph
* Pairwise similarity graph
* Saved report generation
* Viewing the saved report

Detailed testing results are included in the project report.

## Input

The program takes the following inputs from the user:

* Number of text files to compare
* Names of the text files
* A word to search for

The files must be valid, non-empty `.txt` files.

## Output

The program provides:

* Total number of words
* Number of common words
* Common words list
* Unique words in each file
* Word frequency
* Number of unique words
* Longest word
* Shortest word
* Search result
* Repeated two-word phrases
* Similarity percentage
* Similarity result category
* Similarity progress bar
* Highest similarity pair
* Words common in all selected files
* Word count comparison graph
* Pairwise similarity graph
* Saved plagiarism report

## Error Handling

The program handles different invalid inputs and file-related errors, including:

* Entering fewer than two files
* Entering more than 50 files
* Entering an invalid number
* Entering a non-text file
* Entering a file that does not exist
* Entering an empty file
* Trying to view a report before generating one
* Trying to display results before checking plagiarism
* Entering an invalid menu option

## Technologies Used

* Python
* VS Code
* Matplotlib
* Git
* GitHub

## Purpose of the Project

This project demonstrates the use of:

* Variables and data types
* Input and output
* Conditional statements
* Loops
* Functions
* Lists
* Dictionaries
* Sets
* Strings
* File handling
* Exception handling
* Input validation
* Modular programming
* Text processing
* Data visualization

## Limitations

* The project uses basic word-level comparison.
* It does not perform advanced semantic analysis.
* It does not understand the meaning or context of sentences.
* Similar words with different forms may not always be identified as related.
* The similarity calculation is based on word overlap.
* The project does not use online sources or an external database.

## Future Enhancements

Possible future improvements include:

* Improved similarity scoring methods
* Semantic text comparison
* Support for PDF and DOCX files
* More efficient processing for large files
* Improved repeated phrase detection
* Online source or database integration
* Automated testing
* More advanced visualization
* Improved report generation

## Project Screenshots

The project report contains screenshots of:

* Main menu
* Plagiarism result
* Similarity progress bar
* Similarity graph
* Saved report
* Highest similarity result

## Educational Purpose

This project was developed as part of the VITyarthi Build Your Own Project activity for learning and applying Python programming concepts in a practical project.