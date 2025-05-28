import sys
import argparse
from pytable_csv import *
from pytable_tsv import *
from pytable_md import *
from pytable_html import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A converter for tabular data.")
    parser.add_argument("-w", "--html", help="Convert to HTML.")
    parser.add_argument("-c", "--csv", help="Convert to CSV.")
    parser.add_argument("-t", "--tsv", help="Convert to TSV.")
    parser.add_argument("-m", "--markdown", help="Convert to Markdown.")

    args = parser.parse_args()

    assert '.' in sys.argv[2], "Must have file extension" # The assumption is that all files have a '.' extension.
    file_name = sys.argv[2]
    file_extension = sys.argv[2].split('.')[-1] # Grabs the file extension

    if file_extension not in ("csv", "tsv", "md"):
        print("Error: your file must have the following extensions: csv, tsv, or md")
        exit()

    if args.csv:
        if file_extension == "tsv":
            tsv_to_csv(file_name)
        elif file_extension == "md":
            md_to_csv(file_name)
    elif args.tsv:
        if file_extension == "csv":
            csv_to_tsv(file_name)
        elif file_extension == "md":
            md_to_tsv(file_name)
    elif args.html:
        if file_extension == "csv":
            csv_to_html(file_name)
        elif file_extension == "tsv":
            tsv_to_html(file_name)
        elif file_extension == "md":
            md_to_html(file_name)
    elif args.markdown:
        if file_extension == "csv":
            csv_to_mdtable(file_name)
        elif file_extension == "tsv":
            tsv_to_mdtable(file_name)

