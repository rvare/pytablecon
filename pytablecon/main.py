import csv
import sys

def mdtable_to_csv(lines_temp):
    strip_lines = [i.strip('\n') for i in lines_temp]
    del strip_lines[1]
    split_lines = [i.split('|') for i in strip_lines]
    lines = list()
    for i in split_lines:
        if i[0] == '' and i[-1] == '':
            del i[0]
            del i[-1]

        for j, s in enumerate(i):
            i[j] = s.strip()

        lines.append(i)
    
    return lines

def csv_to_mdtable(file_name):
    csv_lines = list()
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        second_line = False
        temp_str = "|"
        for line in csv_reader:
            #print(line)
            csv_lines.append(line)
            if second_line == False:
                for i in csv_lines[0]:
                    temp_str += "-|"
                # csv_lines.append(temp_str)
                temp_str += '\n'
                second_line = True
        str_lines = list()
        second_line = False
        for i in csv_lines:
            str_lines.append("| " + " | ".join(i) + " |\n")
            if second_line == False:
                str_lines.append(temp_str)
                second_line = True

    print(csv_lines)

    with open("../tests/test_output.md", mode="w") as output_file:
        output_file.writelines(str_lines)
        

if __name__ == '__main__':
    file_name = sys.argv[1]
    lines_temp = list()
    # with open("../tests/test1.md") as md_file:
    with open(file_name) as md_file:
        for i in md_file:
            lines_temp.append(i)

    file_extension = file_name.split('.')[3]
    print(file_extension)

    if file_extension == "md":
        lines = mdtable_to_csv(lines_temp)
        with open("../tests/test_output.csv", mode="w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerows(lines)
    else:
        print("here")
        csv_to_mdtable(file_name)
        # with open("../tests/test_out.md", mode="w", newline="") as output_file:
        #     output_file.write(lines)