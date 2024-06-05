import csv

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

    output_path = file_name.replace("csv", "md")
    with open(output_path, mode="w") as output_file:
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

    output_path = file_name.replace("tsv", "md")
    with open(output_path, mode="w") as output_file:
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