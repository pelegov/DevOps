import csv

jamf = open("/Users/nave-peleg/Downloads/1730 Computers in All Managed Devices.csv", "r")
csv_reader = csv.reader(jamf, delimiter=',')
csv_list = list(csv_reader)
jamf.close()

jamf = open('sorted_computer.csv', 'w')
jamf.write('rank,')

rank = 0

for i in csv_list[0]:
    if i == csv_list[0][-1]:
        jamf.write(i)
    else:
        jamf.write(i + ',')
jamf.write('\n')

for i in csv_list:
    if rank == 0:
        prev_i = csv_list[csv_list.index(i)]
        rank +=1
    else:
        prev_i = csv_list[csv_list.index(i) - 1]

    if i[-1] == prev_i[-1]:
        jamf.write(f'{rank},')
    else:
        rank += 1
        jamf.write(f'{rank},')
    for j in i:
        jamf.write(j)
    else:
        jamf.write(j + ',')
    jamf.write('\n')

jamf.close()
