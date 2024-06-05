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