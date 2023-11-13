import morphology
from neuron import h
import sys
import csv




swc_file = sys.argv[1]
csv_file = sys.argv[1]+'-output.csv'
#swc_file = "swcs/32-human-hcca1-idab1-porta4-sec1-cel2-soma-corr1-7z.CNG.swc"
cell = morphology.load(swc_file)

# Save the radii
radii = []

# Save the branch orders
branch_orders, radii= morphology.all_branch_orders(h)
# print(len(branch_orders))
# print("Branch Orders:", branch_orders)
# print(len(radii))
# print(radii)
print("success")


# Write the data into csv file
with open(csv_file, 'a+', newline='') as file:
    writer = csv.writer(file)
    # writer.writerow(['branch_orders', 'radii'])  # 写入表头
    writer.writerows(zip(branch_orders, radii))  # 写入数据行

