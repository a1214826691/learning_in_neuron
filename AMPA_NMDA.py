from neuron import h
from neuron.units import ms, mV, µm
import matplotlib.pyplot as plt


class BallAndStick:
    def __init__(self, gid):
        self._gid = gid
        self._setup_morphology()
        self._setup_biophysics()

    def _setup_morphology(self):
        self.soma = h.Section(name="soma", cell=self)
        self.dend = h.Section(name="dend", cell=self)
        self.dend.connect(self.soma)
        self.all = self.soma.wholetree()
        self.soma.L = self.soma.diam = 12.6157 * µm
        self.dend.L = 200 * µm
        self.dend.diam = 1 * µm

    def _setup_biophysics(self):
        for sec in self.all:
            sec.Ra = 100  # Axial resistance in Ohm * cm
            sec.cm = 1  # Membrane capacitance in micro Farads / cm^2
        self.soma.insert("hh")
        for seg in self.soma:
            seg.hh.gnabar = 0.12  # Sodium conductance in S/cm2
            seg.hh.gkbar = 0.036  # Potassium conductance in S/cm2
            seg.hh.gl = 0.0003  # Leak conductance in S/cm2
            seg.hh.el = -54.3  # Reversal potential in mV
        # Insert passive current in the dendrite
        self.dend.insert("pas")
        for seg in self.dend:
            seg.pas.g = 0.001  # Passive conductance in S/cm2
            seg.pas.e = -65  # Leak reversal potential mV

    def __repr__(self):
        return "BallAndStick[{}]".format(self._gid)

def create_n_BallAndStick(n):
    cells = []
    for i in range(n):
        cells.append(BallAndStick(i))
    return cells



def ampa(my_cells):
    stim_ampa = h.ExpAMPAR(my_cells[0].dend(0.5))
    # stim_nmda = h.Exp2NMDAR(soma2(0.5))
    stim_ampa.tau1 = 2 * ms

    ns = h.NetStim()
    ns.number = 1
    ns.start = 9

    ncstim = h.NetCon(ns, stim_ampa)
    ncstim.delay = 1 * ms
    ncstim.weight[0] = 0.04

    v1 = h.Vector().record(my_cells[0].soma(0.5)._ref_v)  # Membrane potential vector
    # v2 = h.Vector().record(soma2(0.5)._ref_v)
    t = h.Vector().record(h._ref_t)  # Time stamp vector

    syns = []
    netcons = []
    for source, target in zip(my_cells, my_cells[1:] + [my_cells[0]]):  # 将第一个元素连接到list末尾
        syn = h.ExpAMPAR(target.dend(0.5))
        nc = h.NetCon(source.soma(0.5)._ref_v, syn, sec=source.soma)
        nc.weight[0] = 0.05
        nc.delay = 5
        netcons.append(nc)
        syns.append(syn)

    h.load_file("stdrun.hoc")
    h.finitialize(-65 * mV)
    h.continuerun(100 * ms)

    plt.plot(t, v1, label="ampa_soma(0.5)")
    # plt.plot(t, v2, label="dend(0.5)")
    plt.legend()
    # plt.show()

    return v1


def nmda(my_cells):
    stim_nmda = h.Exp2NMDAR(my_cells[0].dend(0.5))
    stim_nmda.tau1 = 2 * ms

    ns = h.NetStim()
    ns.number = 1
    ns.start = 9

    ncstim = h.NetCon(ns, stim_nmda)
    ncstim.delay = 1 * ms
    ncstim.weight[0] = 0.04

    v2 = h.Vector().record(my_cells[0].soma(0.5)._ref_v)  # Membrane potential vector
    t = h.Vector().record(h._ref_t)  # Time stamp vector

    syns = []
    netcons = []
    for source, target in zip(my_cells, my_cells[1:] + [my_cells[0]]):  # 将第一个元素连接到list末尾
        syn = h.Exp2NMDAR(target.dend(0.5))
        nc = h.NetCon(source.soma(0.5)._ref_v, syn, sec=source.soma)
        nc.weight[0] = 0.05
        nc.delay = 5
        netcons.append(nc)
        syns.append(syn)

    h.load_file("stdrun.hoc")
    h.finitialize(-65 * mV)
    h.continuerun(100 * ms)

    plt.plot(t, v2, label="nmda_soma(0.5)")
    plt.legend()


    return v2

cells1 = create_n_BallAndStick(7)
cells2 = create_n_BallAndStick(7)

t = h.Vector().record(h._ref_t)
ampa_v=ampa(cells1)
nmda_v=nmda(cells2)
plt.show()









# my_cells = create_n_BallAndStick(7)
# stim_ampa = h.ExpAMPAR(my_cells[0].dend(0.5))
# # stim_nmda = h.Exp2NMDAR(soma2(0.5))
# stim_ampa.tau1 = 2 * ms

# ns = h.NetStim()
# ns.number = 1
# ns.start = 9

# ncstim=h.NetCon(ns,stim_ampa)
# ncstim.delay = 1 * ms
# ncstim.weight[0] = 0.04


# v1 = h.Vector().record(my_cells[0].soma(0.5)._ref_v)  # Membrane potential vector
# # v2 = h.Vector().record(soma2(0.5)._ref_v)
# t = h.Vector().record(h._ref_t)  # Time stamp vector

# syns = []
# netcons = []
# for source, target in zip(my_cells, my_cells[1:] + [my_cells[0]]):#将第一个元素连接到list末尾
#     syn = h.ExpAMPAR(target.dend(0.5))
#     nc = h.NetCon(source.soma(0.5)._ref_v, syn, sec=source.soma)
#     nc.weight[0] = 0.05
#     nc.delay = 5
#     netcons.append(nc)
#     syns.append(syn)

# h.load_file("stdrun.hoc")
# h.finitialize(-65 * mV)
# h.continuerun(100 * ms)

# # plt.plot(t, v1, label="ampa_soma(0.5)")
# # plt.plot(t, v2, label="dend(0.5)")
# # plt.legend()
# # plt.show()

# spike_times = [h.Vector() for nc in netcons]
# for nc, spike_times_vec in zip(netcons, spike_times):
#     nc.record(spike_times_vec)


# h.finitialize(-65 * mV)
# h.continuerun(100 * ms)


# for i, spike_times_vec in enumerate(spike_times):
#     print("cell {}: {}".format(i, list(spike_times_vec)))

# plt.figure()

# for i, spike_times_vec in enumerate(spike_times):
#     print(i, list(spike_times_vec))
#     plt.vlines(list(spike_times_vec), i + 0.5, i + 1.5)
# plt.show()