**Contents**

- [Introduction](#introduction)
- [Program Flow](#program-flow)
	- [Main Flow](#main-flow)
- [Testing](#testing)

- - -

# Introduction

This file is to document the development process of the project. It's also used for anyone who wants to contribute or just learn from it.

# Program Flow

## Main Flow

The following is the main flow of execution. It is made to be as abstract and general as possible to allow for some flexibility in the development.

```mermaid
flowchart TD;
start[Start]
ed[End]
wrtf[Write to file]

to{Convert To/What Dash Flag?}
csv[Convert to CSV]
tsv[Convert to TSV]
html[Convert to HTML]
md[Convert to Markdown Table]
json[Convert to JSON]
md_style{Which Style?}
delimiter{Delimiter Type}
dfe1[Determine Input File Extension]
dfe2[Determine Input File Extension]
dfe3[Determine Input File Extension]
dfe4[Determine Input File Extension]
dfe5[Determine Input File Extension]

start ----> to
to --CSV--> dfe1
dfe1 ----> delimiter
to --TSV--> dfe2 
dfe2 ----> tsv
to --HTML--> dfe3
dfe3 ----> html
to --Markdown--> dfe4
dfe4 ----> md_style
to --JSON--> dfe5
dfe5 ----> json

delimiter --Comma--> csv
delimiter --Colon--> csv
delimiter --Semicolon--> csv
delimiter --Pipe--> csv

md_style --Traditional--> md
md_style --Grid--> md
md_style --Dashed--> md

csv ----> wrtf
tsv ----> wrtf
html ----> wrtf
md ----> wrtf
json ----> wrtf

wrtf --> ed
```

# Testing

To test the code, run the program and use the test files in `tests` folder.

*Note:* In the future, we will try to use actual testing automation.


