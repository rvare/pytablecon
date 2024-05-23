import csv
import sys

def mdtable_to_csv(file_name):
    """
    Converts a Markdown to CSV.
    md_lines contains the lines of the Markdown table from file.
    processed_lines contains the fields of the Markdown table.
    """
    # Get Markdown table
    md_lines = list()
    with open(file_name) as md_file:
        for i in md_file:
            md_lines.append(i)

    # Process Markdown table and convert
    processed_lines = [i.strip('\n').split('|') for i in md_lines]
    del processed_lines[1]

    str_lines = list()
    for i in processed_lines:
        if i[0] == '' and i[-1] == '':
            del i[0]
            del i[-1]
        # Remove white spaces in string
        for j, s in enumerate(i):
            i[j] = s.strip()
        str_lines.append(i)
    
    # Output to file
    with open("../tests/test_output.csv", mode="w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(str_lines)

def csv_to_mdtable(file_name):
    """
    Converts a CSV to a formatted Markdown table.
    TODO: Find way to make this function better
    """
    csv_lines = list()
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        second_line = False
        temp_str = "|"

        for line in csv_reader:
            csv_lines.append(line)
            if second_line == False:
                for i in csv_lines[0]:
                    temp_str += "-|"
                temp_str += '\n'
                second_line = True
        str_lines = list()
        second_line = False
        
        for i in csv_lines:
            str_lines.append("| " + " | ".join(i) + " |\n")
            if second_line == False:
                str_lines.append(temp_str)
                second_line = True

    with open("../tests/test_output.md", mode="w") as output_file:
        output_file.writelines(str_lines)
        

if __name__ == '__main__':
    file_name = sys.argv[1]
    lines_temp = list()

    file_extension = file_name.split('.')[-1]
    # Prints for testing
    # print(file_extension)
    # print(file_name.split('.'))

    if file_extension == "md":
        mdtable_to_csv(file_name)
    else:
        csv_to_mdtable(file_name)