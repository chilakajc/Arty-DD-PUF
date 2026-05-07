import csv
import json

presets = ['01', '02', '04', '05', '06', '07', '08', '09', '10']
for id in presets:
    diff_total = 0
    delay_total = 0
    puf_groups = { f'puf_loop[{i}]' : {'d0': 0, 'd1': 0, 'diff': 0, 'out': None} for i in range(16)}
    with open(f'Nx_PR{id}.csv', mode='r', newline='') as dfile:
        reader = csv.reader(dfile)
        header= next(reader)
        for row in reader:
            net_start = row[0].split('.')
            # print(f"row: {row[3:]}")
            # net_end

            if net_start[0] not in puf_groups:
                continue
            # net_end = row[1].split('.')
            if net_start[0] in row[1] and net_start[1].endswith('dl0/reset') and row[1].endswith('dl0/Q_reg/CLR'): # or net_start[1].endswith('dl1/P0'): # or (net_start[0] in row[1] and net_start[1].endswith('dl0/reset') and row[1].endswith('dl0/Q_reg/CLR')) :
                # print(f"row: {row}")
                puf_groups[net_start[0]]['d0'] += int(row[3])
            elif net_start[0] in row[1] and net_start[1].endswith('dl0/reset') and row[1].endswith('dl1/Q_reg/CLR'): # or row[1].endswith('i_1/I2'): # or : row[1].endswith('dl0/Q_reg/D') (net_start[0] in row[1] and net_start[1].endswith('dl0/reset') and row[1].endswith('dl1/Q_reg/CLR')) :  #
                # print(f"row: {row}")
                puf_groups[net_start[0]]['d1'] += int(row[3])
            else:
                continue

        dfile.close()

    for group in puf_groups:
        puf_groups[group]['diff'] = abs(puf_groups[group]['d0'] - puf_groups[group]['d1'])
        delay_total = delay_total + puf_groups[group]['d0'] + puf_groups[group]['d1']
        diff_total = diff_total + abs(puf_groups[group]['diff'])
        
        if puf_groups[group]['d0'] < puf_groups[group]['d1']:
            puf_groups[group]['out'] = 1
        else:
            puf_groups[group]['out'] = 0

    puf_groups["Average D-Diff"] = diff_total / 16.0
    puf_groups["Average Delay"] = 0.5 * delay_total / 16.0
    with open(f'PUFRoutes{id}.json', 'w') as route_file:
        json.dump(puf_groups, route_file, indent=4)


            
