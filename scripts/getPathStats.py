import csv
import json

presets = ['01', '02', '04', '05', '06', '07', '08', '09', '10']
for id in presets:
    puf_groups = { f'puf_loop[{i}]' : {'rt_d0': 0, 'rt_d1': 0, 'diff': 0, 'out': None} for i in range(16)}
    delay_total = 0
    diff_total = 0
    with open(f'Nx_paths{id}.csv', mode='r', newline='') as dfile:
        reader = csv.reader(dfile)
        header= next(reader)
        for row in reader:
            net_start = row[0].split('.')
            # net_end

            if net_start[0] not in puf_groups:
                continue
            # net_end = row[1].split('.')
            if 'dl1' in net_start[1] :
                puf_groups[net_start[0]]['rt_d0'] = float(row[2])
            elif 'dl0' in net_start[1] : 
                puf_groups[net_start[0]]['rt_d1'] = float(row[2])
            else:
                continue

        dfile.close()

    for group in puf_groups:
        puf_groups[group]['diff'] = puf_groups[group]['rt_d0'] - puf_groups[group]['rt_d1']
        delay_total = delay_total + puf_groups[group]['rt_d0'] + puf_groups[group]['rt_d1']
        diff_total = diff_total + abs(puf_groups[group]['diff'])
        if puf_groups[group]['rt_d0'] < puf_groups[group]['rt_d1']:
            puf_groups[group]['out'] = 1
        else:
            puf_groups[group]['out'] = 0

    puf_groups["Average Static D-latch Cycle"] = delay_total / 16.0
    puf_groups["Average D-Diff"] = diff_total / 16.0
    with open(f'PathDelays{id}.json', 'w') as path_file:
        json.dump(puf_groups, path_file, indent=4)

# print(f"Average Static D-latch Cycle: {delay_total / len(puf_groups)}")