import zipfile
import glob
from pathlib import Path

# output_dir = 'F:/python/PythonProject/neuron/human/allen/models'
output_dir = 'F:/python/PythonProject/neuron/mouse/allen/models'

from allensdk.api.queries.biophysical_api import BiophysicalApi
#from allensdk.api.queries.glif_api import GlifApi

bp = BiophysicalApi()
#bp = GlifApi()
bp.cache_stimulus = True # change to False to not download the large stimulus NWB file

modtype = 'perisomatic_clean'
#modtype = 'GLIF'

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

# # human cells
# cells = ctc.get_cells(require_reconstruction = True,
#                       species=[CellTypesApi.HUMAN])

# mouse cells
cells = ctc.get_cells(require_reconstruction = True,
                      species=[CellTypesApi.MOUSE])

#ctc.get_ephys_data(cells[0]['id'])

for cell in cells:
    print(cell['id'])
    models = bp.get_neuronal_models([cell['id']])
    if len(models)>0:
        for model in models:
            if 'perisomatic' in model['name']:
                cell['model_id'] = model['id']
        try:
            print(cell['model_id'])
            #if(cell['model_id'] is not None):
            neuronal_model_id = cell['model_id']    # get this from the web site as above
            #os.mkdir('E:\Human\code\Allen_models\\' + modtype + '\\' + str(cell['id']))
            bp.cache_data(int(cell['model_id']), working_directory='F:/python/PythonProject/neuron/mouse/allen/models_' + modtype + '/' + str(cell['id']))
            #nm = bp.get_neuronal_models_by_id([neuronal_model_id])[0]

        except:
            print('no data found')





#
# #
# import zipfile
# import glob
# from pathlib import Path
#
# # output_dir = 'F:/python/PythonProject/neuron/human/allen/models'
# output_dir = 'F:/python/PythonProject/neuron/mouse/allen/models'
#
# from allensdk.api.queries.biophysical_api import BiophysicalApi
# #from allensdk.api.queries.glif_api import GlifApi
#
# bp = BiophysicalApi()
# #bp = GlifApi()
# bp.cache_stimulus = True # change to False to not download the large stimulus NWB file
#
# modtype = 'perisomatic_clean'
# #modtype = 'GLIF'
#
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
# # human cells
# cells = ctc.get_cells(require_reconstruction = True,
#                       species=[CellTypesApi.HUMAN])
#
#
# #ctc.get_ephys_data(cells[0]['id'])
# num=0
# lst2=[]
# for cell in cells:
#
#     lst=[cell['id']]
#     models = bp.get_neuronal_models([cell['id']])
#     if len(models)>0:
#         for model in models:
#             if 'perisomatic' in model['name']:
#                 cell['model_id'] = model['id']
#         try:
#
#             #if(cell['model_id'] is not None):
#             neuronal_model_id = cell['model_id']    # get this from the web site as above
#             lst.append(neuronal_model_id)
#             lst2.append(lst)
#             # print(lst)
#             lst.clear()
#             num+=1
#             #os.mkdir('E:\Human\code\Allen_models\\' + modtype + '\\' + str(cell['id']))
#             # bp.cache_data(int(cell['model_id']), working_directory='F:/python/PythonProject/neuron/mouse/allen/models_' + modtype + '/' + str(cell['id']))
#             #nm = bp.get_neuronal_models_by_id([neuronal_model_id])[0]
#
#         except:
#             print('no data found')
# print(num)
# print(lst2.sort())
#
