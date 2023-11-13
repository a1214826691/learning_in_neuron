from pathlib import Path

output_dir = 'F:/python/PythonProject/neuron/human/allen/swcs'

from allensdk.core.cell_types_cache import CellTypesCache
import os

# Instantiate the CellTypesCache instance.  The manifest_file argument
# tells it where to store the manifest, which is a JSON file that tracks
# file paths.  If you supply a relative path it will go into your
# current working directory
try:
    ctc = CellTypesCache(manifest_file=Path(output_dir) / 'manifest.json')
except:
    os.remove(Path(output_dir) / 'manifest.json')
    ctc = CellTypesCache(manifest_file=Path(output_dir) / 'manifest.json')


from allensdk.core.cell_types_cache import CellTypesCache
from allensdk.api.queries.cell_types_api import CellTypesApi
from allensdk.core.cell_types_cache import ReporterStatus as RS

# human cells
cells = ctc.get_cells(require_reconstruction = True,
                      species=[CellTypesApi.HUMAN])
print("Human cells: %d" % len(cells))
print(cells[0])

##get swcs
# for cell in cells:
#     ctc.get_reconstruction(cell['id'], file_name=output_dir + '/' + str(cell['id']) + '.swc')
##get all features
# all_features = ctc.get_all_features(require_reconstruction=True)

import pandas as pd
## convert to a pandas DataFrame
# all_features = pd.DataFrame(all_features)
# print("All features available for %d cells" % len(all_features))

# all_features.to_csv("F:/python/PythonProject/neuron/human/allen/all_features.csv")


import os


# 遍历swcs文件夹中的每个csv，添加brain_region列
# for file_name in os.listdir("F:/python/PythonProject/neuron/human/allen/swcs2"):
#     if file_name.endswith(".csv"):
#
#         file_path = os.path.join("F:/python/PythonProject/neuron/human/allen/swcs2", file_name)
#         swc = pd.read_csv(file_path, names=["branch_order", "radii"], skiprows=1)
#
#         neuron_name = int(file_name[:-15])  # 去掉后缀
#         print(neuron_name)
#         flag=0
#         for cell in cells:
#             if cell['id'] == neuron_name:
#                 neuron_region = cell['structure_area_abbrev']
#                 flag=1
#                 swc["neuron_region"] = neuron_region
#                 out_path = os.path.join("F:/python/PythonProject/neuron/human/allen/swcs2", file_name)
#                 swc.to_csv(out_path, index=False)
#                 break
#         if(flag==0):
#             print("id match fails")


df_all = pd.DataFrame(columns=['speciman_name','speciman_id', 'brain_region'])
for file_name in os.listdir("F:/python/PythonProject/neuron/human/allen/swcs2"):
    if file_name.endswith(".csv"):
        file_path = os.path.join("F:/python/PythonProject/neuron/human/allen/swcs2", file_name)
        neuron_name = int(file_name[:-15])  # 去掉后缀
        print(neuron_name)
        flag = 0
        for cell in cells:
            if cell['id'] == neuron_name:
                neuron_region = cell['structure_area_abbrev']
                flag = 1
                df_row = pd.DataFrame([[cell['name'],cell['id'], neuron_region]], columns=['speciman_name','speciman_id', 'brain_region'])
                df_all = df_all.append(df_row, ignore_index=True)
                print(neuron_region)
                print(df_row)
                break
        if flag == 0:
            print("id match fails")

df_all.to_csv('F:/python/PythonProject/neuron/human/allen/BrainRegion.csv', index=False)


# df_all.to_csv('F:/python/PythonProject/neuron/human/allen/swcs2/output.csv', index=False)


