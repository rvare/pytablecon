import csv

if __name__ == '__main__':
    lines_temp = list()
    with open("tests/test1.md") as md_file:
        for i in md_file:
            lines_temp.append(i)
    
    strip_lines = [i.strip('\n') for i in lines_temp]
    split_lines = [i.split('|') for i in strip_lines]
    lines = list()
    for i in split_lines:
        if i[0] == '' and i[-1] == '':
            del i[0]
            del i[-1]

        for j, s in enumerate(i):
            i[j] = s.strip()

        lines.append(i)

    del lines[1]

    for i in lines:
        print(i)

    with open("tests/test.csv", mode="w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(lines)