import csv

reader = csv.reader(open("India Related Data_555.csv"))
reader1 = csv.reader(open("India Related Data_444 - India Related Data_444.csv"))
f = open("combined.csv", "w")
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)
f.close()
