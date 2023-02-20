def parse_log_file(filename):
    """
    Parses a log file with different number of columns in each row and groups them based on the number of columns.

    Parameters:
    filename (str): The name of the log file to parse.

    Returns:
    A dictionary where the keys are the number of columns in each row and the values are lists of rows for each number of columns.
    """

    # Initialize an empty dictionary to store the rows for each number of columns
    row_dict = {}

    # Open the log file and read each row
    with open(filename, 'r') as file:
        for line in file:
            # Split the row into columns based on tab
            columns = line.strip().split('\t')

            # Get the number of columns in the row
            num_columns = len(columns)

            # Add the row to the corresponding list based on the number of columns
            if num_columns in row_dict:
                row_dict[num_columns].append(columns)
            else:
                row_dict[num_columns] = [columns]

    return row_dict

if __name__ == '__main__':
	filename = 'example.log'
	row_dict = parse_log_file(filename)
	print(row_dict)


