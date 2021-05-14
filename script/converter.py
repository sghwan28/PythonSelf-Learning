import csv
import pandas as pd

with open("zr333.stru","r") as raw:
    with open('cell.csv', 'w', encoding='ascii', errors='ignore') as f:
        fw = csv.writer(f, delimiter =',')
        for line in raw:
            if line.startswith('atoms'):
                line = line.replace(' ','')
                line = line.strip('\n')
                line = line[:5] + ',' + line[5:]
                fw.writerow(line.split(','))

            if len(line) > 105:
                for i in range(10):
                    if not line[i].isalpha():
                        line = line[:i+1] + "," + line[i+1:]
                        break
                line = line.replace(" ",'')
                line = line.strip('\n')
                fw.writerow(line.split(','))

cell = pd.read_csv('cell.csv')
cell = cell.iloc[:,:5]


print(cell)
print(cell.describe())