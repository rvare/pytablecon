import csv

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
    
    output_path = file_name.replace("md", "tsv")
    with open(output_path, "w") as output_file:
        output_file.writelines(joined_str)

def csv_to_tsv(file_name):
    """
    Converts a CSV file to a TSV file.
    tsv_lines = contains data seperated by tabs
                to be written to file.
    """
    tsv_lines = list()

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            tsv_lines.append('\t'.join(row) + '\n')
        
        file_name_parts = file_name.split('.')
        file_name_parts[-1] = "tsv"
        output_file = '.'.join(file_name_parts)
        print(output_file)
        with open(output_file, mode="w") as output_file:
            output_file.writelines(tsv_lines)