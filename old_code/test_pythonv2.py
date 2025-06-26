import csv

def read_and_sum_column(filename, column_index):
    total = 0
    try:
        f = open(filename, 'rU')
        reader = csv.reader(f)
        for row in reader:
            try:
                total += float(row[column_index])
            except (ValueError, IndexError):
                continue
        f.close()
        print "Total sum in column %d: %f" % (column_index, total)
    except IOError:
        print "Error: File not found or unreadable."

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print "Usage: python script.py <filename.csv> <column_index>"
    else:
        filename = sys.argv[1]
        index = int(sys.argv[2])
        read_and_sum_column(filename, index)
