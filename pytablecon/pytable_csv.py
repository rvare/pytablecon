import csv

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
    output_path = file_name.replace("md", "csv")
    with open(output_path, mode="w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(str_lines)