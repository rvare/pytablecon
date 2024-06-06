# Contains functions that go from one format to HTML
import csv

def csv_to_html(file_name):
    """
    Converts a CSV file to an HTML document.
    There is no styling for the HTML output.
    """
    name_temp = file_name.split('.')[-2].split('/')[-1]
    html_head = ' '*4 + "<head>\n" + ' '*8 + f"<title>{name_temp}</title>\n" + ' '*4 + "</head>\n"

    table_lines = list()
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
            for i in line:
                table_lines.append(' '*12 + f"<td>{i}</td>\n")
            table_lines.append(' '*8 + "</tr>\n")
        
        table_lines.append(' '*4 + "</table>\n")
    
    output_path = file_name.replace("csv", "html")
    with open(output_path, mode="w") as output_file:
        output_file.write("<!DOCTYPE HTML>\n<html>\n")
        output_file.write(html_head)
        output_file.write(' '*4 + "<body>\n")
        output_file.writelines(table_lines)
        output_file.write(' '*4 + "</body>\n</html>")

def tsv_to_html(file_name):
    """
    Converts a TSV file to an HTML document.
    There is no styling for the HTML output.
    """
    name_temp = file_name.split('.')[-2].split('/')[-1]
    html_head = ' '*4 + "<head>\n" + ' '*8 + f"<title>{name_temp}</title>\n" + ' '*4 + "</head>\n"
    table_lines = list()
    tsv_lines = list()
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
    
    output_path = file_name.replace("tsv", "html")
    with open(output_path, "w") as output_file:
        output_file.write("<!DOCTYPE HTML>\n<html>\n")
        output_file.write(html_head)
        output_file.write(' '*4 + "<body>\n")
        output_file.writelines(table_lines)
        output_file.write(' '*4 + "</body>\n</html>")

def md_to_html(file_name):
    pass