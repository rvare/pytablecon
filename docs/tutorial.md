# Getting Help

Use `-h` flag or `--help` to get help in the commandline.

# How to run

To run the script, do the following

```python
python main.py --what_to_convert_to file.extension
```

The file output will appear in the same directory as the converted file.

# Examples

## From Markdown to CSV

```python
python main.py -c test.md
```

Will convert a markdown table to a CSV file.

## From CSV to HTML

```python
python main.py -w test.csv
```

Will convert a CSV file into an HTML table

