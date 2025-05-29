# Contains functions that go from one format to HTML
import csv

def csv_to_html(file_name):
    """
    Converts a CSV file to an HTML document with no CSS styleing.

    Keyword arguements:
    file_name: Contains the path of the file that is to be converted.
    """
    table_lines = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)

        csv_iter = iter(csv_reader)
        csv_col_headers = next(csv_iter)
        table_lines.append(' '*4 + "<table>\n")
        table_lines.append(' '*8 + "<tr>\n")
        for col_header in csv_col_headers:
            table_lines.append(' '*12 + f"<th>{col_header}</th>\n")
        table_lines.append(' '*8 + "</tr>\n")

        while (line := next(csv_iter, None)) is not None:
            table_lines.append(' '*8 + "<tr>\n")
            for i in line: # Could replace by line.join(' '*12 + "<td>" + line.join("</td>\n<td>" + "</td>"))
                table_lines.append(' '*12 + f"<td>{i}</td>\n")
            table_lines.append(' '*8 + "</tr>\n")
        
        table_lines.append(' '*4 + "</table>\n")

    output_to_file(file_name, "csv", "html", table_lines)    

def tsv_to_html(file_name):
    """
    Converts a TSV file to an HTML document with no CSS styling.

    Keyword arguements:
    file_name: Contains the path of the file that is to be converted.
    """
    table_lines = []
    tsv_lines = []
    with open(file_name) as tsv_file:
        for line in tsv_file:
            tsv_lines.append(line.strip('\n').split('\t'))
    
    tsv_iter = iter(tsv_lines)
    table_lines.append(' '*4 + "<table>\n")
    table_lines.append(' '*8 + "<tr>\n")
    tsv_col_headers = next(tsv_iter)
    for i in tsv_col_headers:
        table_lines.append(' '*12 + f"<th>{i}</th>\n")
    table_lines.append(' '*8 + "</tr>\n")

    while (line := next(tsv_iter, None)) is not None:
        table_lines.append(' '*8 + "<tr>\n")
        for i in line:
            table_lines.append(' '*12 + f"<td>{i}</td>\n")
        table_lines.append(' '*8 + "</tr>\n")
    
    table_lines.append(' '*4 + "</table>\n")
    output_to_file(file_name, "tsv", "html", table_lines)    

def mdtable_to_html(file_name):
    """
    Converts a Markdown table to HTML with no CSS styling.
    Can only do the pipe style table for now.

    Keyword arguements:
    file_name: Contains the path of the file that is to be converted.
    """
    table_lines = []
    md_table_lines = []

    with open(file_name) as md_file:
        for line in md_file:
            md_table_lines.append(line.strip('\n'))
    
    md_iter = iter(md_table_lines)
    table_lines.append(' '*4 + "<table>\n")
    table_lines.append(' '*8 + "<tr>\n")
    table_headers = next(md_iter).split('|')
    del table_headers[0]
    del table_headers[-1]
    for i in range(len(table_headers)):
        table_headers[i] = table_headers[i].strip()
    table_headers_str = "</th>\n            <th>".join(table_headers)
    table_headers_str = ' '*12 + f"<th>{table_headers_str}</th>\n"
    table_lines.append(table_headers_str)
    table_lines.append(' '*8 + "</tr>\n")

    next(md_iter) # Remove column alignment syntax. Will find a way to use this in the future

    while (line := next(md_iter, None)) is not None:
        table_lines.append(' '*8 + "<tr>\n")
        table_cols = line.split('|')
        del table_cols[0]
        del table_cols[-1]
        for i in range(len(table_cols)):
            table_cols[i] = table_cols[i].strip()
        table_cols_str = "</td>\n            <td>".join(table_cols)
        table_cols_str = ' '*12 + f"<td>{table_cols_str}</td>\n"
        table_lines.append(table_cols_str)
        table_lines.append(' '*8 + "</tr>\n")
    
    table_lines.append(' '*4 + "</table>\n")
    output_to_file(file_name, "md", "html", table_lines)

def output_to_file(file_name, orig_format, output_format, table_lines):
    name_temp = file_name.split('.')[-2].split('/')[-1]
    html_head = ' '*4 + "<head>\n" + ' '*8 + f"<title>{name_temp}</title>\n" + ' '*4 + "</head>\n"
    output_path = file_name.replace(orig_format, output_format)
    with open(output_path, "w") as output_file:
        output_file.write("<!DOCTYPE HTML>\n<html>\n")
        output_file.write(html_head)
        output_file.write(' '*4 + "<body>\n")
        output_file.writelines(table_lines)
        output_file.write(' '*4 + "</body>\n</html>")
