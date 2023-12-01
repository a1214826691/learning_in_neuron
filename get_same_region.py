from pathlib import Path

# # output_dir = 'F:/python/PythonProject/neuron/human/allen/swcs'
# output_dir = 'F:/python/mouse/allen/swcs'
# from allensdk.core.cell_types_cache import CellTypesCache
# import os
#
# # Instantiate the CellTypesCache instance.  The manifest_file argument
# # tells it where to store the manifest, which is a JSON file that tracks
# # file paths.  If you supply a relative path it will go into your
# # current working directory
# try:
#     ctc = CellTypesCache(manifest_file=Path(output_dir) / 'manifest.json')
# except:
#     os.remove(Path(output_dir) / 'manifest.json')
#     ctc = CellTypesCache(manifest_file=Path(output_dir) / 'manifest.json')
#
#
# from allensdk.core.cell_types_cache import CellTypesCache
# from allensdk.api.queries.cell_types_api import CellTypesApi
# from allensdk.core.cell_types_cache import ReporterStatus as RS
#
#
# cells = ctc.get_cells(require_reconstruction = True,
#                       species=[CellTypesApi.MOUSE])
#
#
# import pandas as pd
#
#
# df_all = pd.DataFrame(columns=['speciman_name','speciman_id', 'brain_region'])
# for file_name in os.listdir("F:/python/mouse/allen/swcs"):
#     if file_name.endswith(".swc"):
#         file_path = os.path.join("F:/python/mouse/allen/swcs", file_name)
#         neuron_name = int(file_name[:-4])  # 去掉后缀
#         print(neuron_name)
#         flag = 0
#         for cell in cells:
#             if cell['id'] == neuron_name:
#                 neuron_region = cell['structure_area_abbrev']
#                 flag = 1
#                 df_row = pd.DataFrame([[cell['name'],cell['id'], neuron_region]], columns=['speciman_name','speciman_id', 'brain_region'])
#                 df_all = df_all.append(df_row, ignore_index=True)
#                 print(neuron_region)
#                 print(df_row)
#                 break
#         if flag == 0:
#             print("id match fails")
#
# df_all.to_csv('F:/python/mouse/allen/BrainRegion.csv', index=False)

import pandas as pd
import numpy as np

allen_df = pd.read_csv('F:/python/mouse/allen/BrainRegion.csv')
ours_df = pd.read_csv('F:/python/mouse/our_features.csv',encoding='gb18030')

#获取两个文件中共同的region列表
common_regions = np.intersect1d(allen_df['brain_region'], ours_df['Manually_corrected_soma_region'])

# region_counts_df = pd.DataFrame(columns=['Region', 'Count', 'Allen', 'Ours'])
region_counts_df = pd.DataFrame(columns=['Region', 'Allen', 'Ours'])

#统计每种region的个数
for region in common_regions:
    a = len(allen_df[allen_df['brain_region'] == region])
    b = len(ours_df[ours_df['Manually_corrected_soma_region'] == region])
    count = a + b
    # df = pd.DataFrame({'Region': [region], 'Count': [count], 'Allen': [a], 'Ours': [b]})
    df = pd.DataFrame({'Region': [region], 'Allen': [a], 'Ours': [b]})
    region_counts_df = pd.concat([region_counts_df, df], ignore_index=True)

print(region_counts_df)
region_counts_df.to_csv('F:/python/mouse/SameRegion.csv', index=False)
