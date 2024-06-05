import sys
from pytable_csv import *
from pytable_tsv import *
from pytable_md import *

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
