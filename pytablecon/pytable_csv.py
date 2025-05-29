import csv

def mdtable_to_csv(file_name):
    """
    Converts a Markdown to CSV.

    Keyword arguements:
    file_name: contains the path of the file that is to be converted.
    """
    # Get Markdown table
    md_lines = []
    with open(file_name) as md_file:
        for i in md_file:
            md_lines.append(i)

    # Process Markdown table and convert
    processed_lines = [x.strip('\n').split('|') for x in md_lines]
    del processed_lines[1]

    str_lines = []
    for i in processed_lines:
        if i[0] == '' and i[-1] == '':
            del i[0]
            del i[-1]
        # Remove white spaces in string
        for j, s in enumerate(i):
            i[j] = s.strip()
        str_lines.append(i)
    
    # Output to file
    output_path = file_name.replace("md", "csv")
    with open(output_path, mode="w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(str_lines)

def tsv_to_csv(file_name):
    """
    Converts a TSV file to a CSV file.

    Keyword arguements:
    file_name: contains the path of the file that is to be converted.
    """
    tsv_lines = []
    with open(file_name) as tsv_file:
        for i in tsv_file:
            tsv_lines.append(i)
    
    processed_lines = [x.split('\t') for x in tsv_lines]
    csv_lines = [','.join(x) for x in processed_lines]

    output_path = file_name.replace("tsv", "csv")
    with open(output_path, "w") as output_file:
        output_file.writelines(csv_lines)
