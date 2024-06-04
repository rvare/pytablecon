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
    processed_lines = [x.strip('\n').split('|') for x in md_lines]
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
    TODO: Find way to make this function better DONE
    """
    csv_lines = list()
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)

        csv_iter = iter(csv_reader)
        col_headers = next(csv_iter)
        csv_lines.append("| " + " | ".join(col_headers) + " |\n")
        alignment_columns = md_alignment_columns(",".join(col_headers), ',')
        csv_lines.append(alignment_columns + '\n')

        while (line := next(csv_iter, None)) is not None:
            csv_lines.append("| " + " | ".join(line) + " |\n")

    with open("../tests/test_output.md", mode="w") as output_file:
        output_file.writelines(csv_lines)
        
def tsv_to_mdtable(file_name):
    """
    Converts TSV file to Markdown table.
    """
    tsv_lines = list()
    with open(file_name) as tsv_file:
        for line in tsv_file:
            tsv_lines.append(line)
   
    alignment_cols = md_alignment_columns(tsv_lines[0], '\t')

    processed_lines = list()
    for i in tsv_lines:
        processed_lines.append( "| " + i.strip('\n').replace('\t', " | ") + " |\n" )

    processed_lines.insert(1, alignment_cols + '\n')

    with open("../tests/test_output.md", mode="w") as output_file:
        output_file.writelines(processed_lines)

def md_alignment_columns(cols, delimiter):
    """
    Determines the number of columns for a Markdown table.
    TODO: Modify function so that it can do alignment.
    TODO: Modify function so that it can do different Markdown tables styles.
    """
    num_columns = len(cols.split(delimiter))
    alignment_columns = "|" # This is the first pipe for the alignment syntax
    for i in range(num_columns):
        alignment_columns += "-|"
    
    return alignment_columns

def mdtable_to_tsv(file_name):
    """
    Convert Markdown table to TSV.
    TODO: Handle different kinds of Markdown tables.
    """
    # Get Markdown table
    md_lines = list()
    with open(file_name) as md_file:
        for i in md_file:
            md_lines.append(i)

    # Get Markdown table
    md_lines = list()
    with open(file_name) as md_file:
        for i in md_file:
            md_lines.append(i)

    # Process Markdown table and convert
    processed_lines = [x.strip('\n').split('|') for x in md_lines]
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

    joined_str = list()
    for i in str_lines:
        joined_str.append("\t".join(i) + '\n')
    
    with open("../tests/test_output.tsv", "w") as output_file:
        output_file.writelines(joined_str)

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        file_name = sys.argv[1]
        output_name = sys.argv[2]
        lines_temp = list()
    else:
        print("Not enough arguments. Be sure to specify input file and output file format")
        print("Ex: file_name.ex out")
        exit()

    file_extension = file_name.split('.')[-1]
    # Prints for testing
    # print(file_extension)
    # print(file_name.split('.'))

    if file_extension == "md":
        if output_name == "csv":
            mdtable_to_csv(file_name)
        elif output_name == "tsv":
            mdtable_to_tsv(file_name)
    elif file_extension == "csv":
        if output_name == "md":
            csv_to_mdtable(file_name)
        elif output_name == "html":
            print("CSV to HTML")
    elif file_extension == "tsv":
        if output_name == "md":
            tsv_to_mdtable(file_name)
        elif output_name == "HTML":
            print("TSV to HTML")
    else:
        print("Output format not valid")
        exit()
