def read_file(file_name):

    try:

        with open(file_name, "r") as file:

            content = file.read()

            return content

    except FileNotFoundError:

        print("File not found:", file_name)

        return ""


def check_file(file_name):

    if not file_name.endswith(".txt"):

        print("Please enter a text file.")

        return False

    try:

        with open(file_name, "r") as file:

            text = file.read()

        if text.strip() == "":

            print("File is empty.")

            return False

        return True

    except FileNotFoundError:

        print("File not found.")

        return False