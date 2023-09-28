import morphology
from neuron import h
import matplotlib.pyplot as plt
from neuron.units import ms, mV, µm
import numpy as np
import random
import sys

# Get the SWC file path from command line argument
swc_file = sys.argv[1]
# number_synapses = sys.argv[2]

cell = morphology.load(swc_file)
# cell = morphology.load("test2.swc")

# Plot loaded neuron with shapeplot
fig = plt.figure(figsize=(7,7))
shapeax = plt.subplot(111, projection='3d')
shapeax.view_init(75,66)
shapelines = morphology.shapeplot(h,shapeax)
#shapelines = morphology.shapeplot(h,shapeax,cvals=v[200])
plt.title('Synapses at red dots',fontweight='bold')
# plt.show()

syn_ids=random.sample(range(len(cell.all)),20)

syns=[]

# Now mark the location of our stimulation
for i in syn_ids:
    print(i)
    morphology.mark_locations(h,cell.all[i],0.0)
    # path = morphology.get_section_path(h, cell.all[i])
    # middle_index = round(np.shape(path)[0] / 2)
    # a = path[middle_index, :]#middle_position = path[middle_index, :]
    # # a = morphology.get_section_path(h, cell.all[syns[synapse]])[
    # #     round(np.shape(morphology.get_section_path(h, cell.all[syns[synapse]]))[0] / 2),]
    # print("distance to soma")
    # print(np.sqrt((a*a).sum(axis=0)))


plt.show()




for sec in cell.all:
    sec.Ra = 100  # Axial resistance in Ohm * cm
    sec.cm = 1  # Membrane capacitance in micro Farads / cm^2

for i in range((len(cell.soma))):
    cell.soma[i].insert("hh")
    for seg in cell.soma[i]:
        seg.hh.gnabar = 0.12  # Sodium conductance in S/cm2
        seg.hh.gkbar = 0.036  # Potassium conductance in S/cm2
        seg.hh.gl = 0.0003  # Leak conductance in S/cm2
        seg.hh.el = -54.3  # Reversal potential in mV
for i in range((len(cell.dend))):
    # Insert passive current in the dendrite
    cell.dend[i].insert("pas")
    for seg in cell.dend[i]:
        seg.pas.g = 0.001  # Passive conductance in S/cm2
        seg.pas.e = -65  # Leak reversal potential mV

def ampa(cell):
    exp2syn = []
    ns = []
    nc = []

    # Iterate over the selected synapse IDs
    for i in syn_ids:
        # Create an Exp2Syn synaptic object
        exp2syn.append(h.Exp2Syn(cell.all[i](0.0)))

        # Create a NetStim object for each synapse
        ns.append(h.NetStim())
        ns[-1].start = 0
        ns[-1].number = 1  # Set the number of presynaptic events to 1

        # Create a NetCon object to connect the NetStim to the Exp2Syn target
        nc.append(h.NetCon(ns[-1], exp2syn[-1]))
        nc[-1].weight[0] = 1  # Set the synaptic weight

    # Run the simulation


    # soma_v = h.Vector().record(cell.soma[0](0.5)._ref_v)
    dend_v1 = h.Vector().record(cell.all[syn_ids[0]](0.5)._ref_v)
    t = h.Vector().record(h._ref_t)

    h.load_file("stdrun.hoc")
    h.finitialize(-65 * mV)
    h.continuerun(400 * ms)

    # plt.plot(t, soma_v, label="soma[0](0.5)")
    plt.plot(t, dend_v1, label="ampa_dend[0](0.5)")
    plt.legend()


def nmda(cell):
    exp2syn = []
    ns = []
    nc = []

    # Iterate over the selected synapse IDs
    for i in syn_ids:
        # Create an Exp2Syn synaptic object
        exp2syn.append(h.Exp2NMDAR(cell.all[i](0.0)))

        # Create a NetStim object for each synapse
        ns.append(h.NetStim())
        ns[-1].start = 0
        ns[-1].number = 1  # Set the number of presynaptic events to 1

        # Create a NetCon object to connect the NetStim to the Exp2Syn target
        nc.append(h.NetCon(ns[-1], exp2syn[-1]))
        nc[-1].weight[0] = 1  # Set the synaptic weight

    # Run the simulation

    # soma_v = h.Vector().record(cell.soma[0](0.5)._ref_v)
    dend_v2 = h.Vector().record(cell.all[syn_ids[0]](0.5)._ref_v)
    t = h.Vector().record(h._ref_t)

    h.load_file("stdrun.hoc")
    h.finitialize(-65 * mV)
    h.continuerun(400 * ms)

    # plt.plot(t, soma_v, label="soma[0](0.5)")
    plt.plot(t, dend_v2, label="nmda_dend[0](0.5)")
    plt.legend()

ampa(cell)
nmda(cell)
plt.show()