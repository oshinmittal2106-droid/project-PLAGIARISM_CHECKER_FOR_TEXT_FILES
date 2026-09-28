# Project Statement

## Problem Statement

Plagiarism Checker for Text Files is a Python-based educational project designed to identify basic similarity between multiple text files. The project compares the words present in selected text files and provides information such as common words, words unique to each file, word frequency, repeated phrases, and similarity percentage.

The program can compare between 2 and 50 text files at a time. It also identifies the pair of files with the highest similarity and finds words that are common in all selected files.

The project uses word-level comparison and does not perform advanced semantic analysis or use online sources and databases.

## Objectives

The main objectives of the project are:

* To compare two or more text files.
* To support comparison of up to 50 files.
* To read and process text files.
* To convert text into lowercase.
* To remove selected punctuation marks.
* To find common words between files.
* To find words unique to each file.
* To find words common in all selected files.
* To calculate basic word-based similarity.
* To detect repeated two-word phrases.
* To calculate word frequency.
* To count unique words.
* To find the longest and shortest words.
* To provide a word search feature.
* To identify the pair of files with the highest similarity.
* To display a similarity progress bar.
* To display word count and pairwise similarity graphs.
* To save plagiarism results and word analysis in a text report.
* To provide input validation and error handling.
* To use modular programming with separate Python files.

## Proposed Solution

The proposed solution is a Python program divided into separate modules for different tasks.

The `file_handler.py` module validates and reads the selected text files. The `text_processing.py` module performs operations such as cleaning punctuation, calculating word frequency, counting unique words, finding word length, searching words, and finding common and unique words.

The `plagiarism_checker.py` module compares the processed files, calculates word-based similarity, detects repeated two-word phrases, and displays plagiarism results. It also finds the words common in all selected files.

The `visualization.py` module creates graphs showing word count comparison and pairwise similarity between files.

The `report_generator.py` module saves comparison results and word analysis in a text report.

The `main.py` module controls the complete workflow and provides the main menu. The program accepts 2 to 50 text files, processes them, performs pairwise comparisons, identifies the highest similarity pair, displays results, generates visualizations, and saves the report.

## Expected Outcome

The expected outcome of the project is a working Python application that can:

* Compare multiple text files.
* Calculate basic word-based similarity.
* Display common and unique words.
* Find words common in all selected files.
* Calculate word frequency.
* Find unique, longest, and shortest words.
* Search for a specific word.
* Detect repeated two-word phrases.
* Identify the highest similarity pair.
* Display similarity using a progress bar.
* Generate word count and pairwise similarity graphs.
* Save comparison results in a text report.
* Handle invalid inputs and file-related errors.

## Concepts Used

The project applies the following Python and programming concepts:

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

## Scope

The project is designed for basic comparison of local `.txt` files. It supports multiple file comparison, word-level similarity, common and unique word analysis, word frequency, word searching, repeated phrase detection, highest similarity identification, graphical visualization, and report generation.

The project does not include online plagiarism databases, internet-based source checking, advanced semantic analysis, or meaning-based comparison.

## Target Users

The project can be useful for:

* Students learning Python programming.
* Educators demonstrating basic text processing.
* Users who want to perform simple word-level comparison between text files.

## Project Modules

The project is divided into the following Python modules:

* `main.py` – Controls the main program and menu.
* `file_handler.py` – Handles file validation and reading.
* `text_processing.py` – Performs text processing and word analysis.
* `plagiarism_checker.py` – Performs similarity checking, repeated phrase detection, and plagiarism result display.
* `report_generator.py` – Generates and saves the text report.
* `visualization.py` – Generates word count and similarity graphs.