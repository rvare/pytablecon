import sys
from pytable_csv import *
from pytable_tsv import *
from pytable_md import *
from pytable_html import *

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        file_name = sys.argv[1]
        output_name = sys.argv[2]
        lines_temp = []
    else:
        print("Not enough arguments. Be sure to specify input file and output file format")
        print("Ex: file_name.ex out")
        exit()

    file_extension = file_name.split('.')[-1]

    if file_extension == "md": # From Markdown
        if output_name == "csv":
            mdtable_to_csv(file_name)
        elif output_name == "tsv":
            mdtable_to_tsv(file_name)
        elif output_name == "html":
            mdtable_to_html(file_name)
    elif file_extension == "csv": # From CSV
        if output_name == "md":
            csv_to_mdtable(file_name)
        elif output_name == "html":
            csv_to_html(file_name)
        elif output_name == "tsv":
            csv_to_tsv(file_name)
    elif file_extension == "tsv": # From TSV
        if output_name == "md":
            tsv_to_mdtable(file_name)
        elif output_name == "csv":
            tsv_to_csv(file_name)
        elif output_name == "html":
            tsv_to_html(file_name)
    else:
        print("Output format not valid")
        exit()
