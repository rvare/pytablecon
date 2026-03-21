import csv
import pytable_constants as ptc

def csv_to_mdtable(file_name: str) -> None:
    """
    Converts a CSV to a formatted Markdown table.

    Keyword arguements:
    file_name: Contains the path of the file that is to be converted.
    """
    md_lines: list[str] = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)

        csv_iter = iter(csv_reader)
        col_headers = next(csv_iter)
        md_lines.append("| " + " | ".join(col_headers) + " |\n")
        alignment_columns = md_alignment_columns(",".join(col_headers), ',')
        md_lines.append(alignment_columns + '\n')

        while (line := next(csv_iter, None)) is not None:
            md_lines.append("| " + " | ".join(line) + " |\n")

    output_path: str = file_name.replace(ptc.CSV_FILE_EXTENSION, ptc.MARKDOWN_FILE_EXTENSION)
    with open(output_path, mode="w") as output_file:
        output_file.writelines(md_lines)

def tsv_to_mdtable(file_name: str) -> None:
    """
    Converts TSV file to Markdown table.

    Keyword arguements:
    file_name: Contains the path of the file that is to be converted.
    """
    tsv_lines: list[str] = []
    with open(file_name) as tsv_file:
        for line in tsv_file:
            tsv_lines.append(line)
   
    alignment_cols = md_alignment_columns(tsv_lines[0], '\t')

    processed_lines: list[str] = []
    for i in tsv_lines:
        processed_lines.append( "| " + i.strip('\n').replace('\t', " | ") + " |\n" )

    processed_lines.insert(1, alignment_cols + '\n')

    output_path = file_name.replace(ptc.TSV_FILE_EXTENSION, ptc.MARKDOWN_FILE_EXTENSION)
    with open(output_path, mode="w") as output_file:
        output_file.writelines(processed_lines)

def md_alignment_columns(cols: str, delimiter: str) -> str:
    """
    Determines the number of columns for a Markdown table.

    Keyword arguements:
    cols: The column headers of the file.
    delimter: The character used to deliminate the columns.

    TODO: Modify function so that it can do alignment.
    TODO: Modify function so that it can do different Markdown tables styles.
    """
    num_columns: int = len(cols.split(delimiter))
    alignment_columns: str = "|" # This is the first pipe for the alignment syntax
    for i in range(num_columns):
        alignment_columns += "-|"
    
    return alignment_columns
