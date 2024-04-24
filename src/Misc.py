def read_from_a_file(file_name):
    content_formatted = []

    with open(file_name, 'r') as f:
        all_lines = f.readlines()
        # Now every line in all_lines list contains "\n", this needs to be handled
        for line in all_lines:
            formated_line = line.rstrip()
            # use split if required to break a string based on a delimiter like " ", "." etc
            line_splitted = formated_line.split(" ")
            content_formatted.append(line_splitted)
    return content_formatted


if __name__ == "__main__":
    file_path = "../data/sample_file.txt" # This can be anything, so never hardcode, read from arguments in a function

    print(read_from_a_file(file_path))
