import csv
import os

parts = ['Nx00', 'Nx53', 'Nx56', 'Nx59','Nx120'] # 'Nx63', 

preset = 'iladata10s'
ila_path = 'H:/PUF/PUF_manualPR/'
puf_len = 16

ila_files = [file for file in os.listdir(ila_path) if preset in file ]

with open('ila_comps10s.csv', mode='w', newline='') as ofile:
    header = ['Device'] + [f'Po[{i}]' for i in range(16)]
    writer = csv.writer(ofile)
    writer.writerow(header)

    for part in parts:
        for ila in ila_files:
            if part in ila:
                with open(ila, mode='r', newline='') as pfile:
                    csv_data = list(csv.reader(pfile))
                    for r in range(4):
                        row = csv_data[250 * (r + 1)]
                        entry = [part] + row[3:19]
                        writer.writerow(entry)
                    
                    pfile.close()

    ofile.close()
        
                






