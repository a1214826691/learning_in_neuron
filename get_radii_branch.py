import morphology
from neuron import h
import matplotlib.pyplot as plt
import sys
import csv

csv_file = 'output.csv'

# swc_file = sys.argv[1]
swc_file = "swcs/32-human-hcca1-idab1-porta4-sec1-cel2-soma-corr1-7z.CNG.swc"
cell = morphology.load(swc_file)
print(dir(cell))

# 存储树突和轴突的半径
radii = []

# 存储分支顺序
branch_orders, radii= morphology.all_branch_orders(h)
print(len(branch_orders))
print("Branch Orders:", branch_orders)
print(len(radii))
print(radii)

# 将数据写入CSV文件
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['branch_orders', 'radii'])  # 写入表头
    writer.writerows(zip(branch_orders, radii))  # 写入数据行


