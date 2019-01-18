prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(122100000, "Synchronize.sub")
    prg.add(127000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(127000490, "Pulse TTL2-12", polarity=1, pulse_t=0.56900, enable=False)
    prg.add(130000000, "B comp x", 775.0)
    prg.add(145000000, "Evaporation Ramp.sub")
    prg.add(582003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(582010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(744010000, "empty.sub", enable=False)
    prg.add(748710000, "Picture SetRepumper")
    prg.add(748720000, "Picture SetImaging")
    prg.add(749010050, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(749229400, "Pulse Probe Na", polarity=1, pulse_t=0.00500)
    prg.add(749230146, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(749230490, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(749230500, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(749230520, "Pulse Probe Na", polarity=1, pulse_t=0.00500, functions=dict(time=lambda x: x + 1e-3*cmd.get_var('uw_tau')))
    prg.add(749450620, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(749670169, "Pulse Probe Na", polarity=1, pulse_t=0.00500)
    prg.add(749670865, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(749671219, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau2')))
    prg.add(749671239, "Pulse Probe Na", polarity=1, pulse_t=0.00500, functions=dict(time=lambda x: x + 1e-3*cmd.get_var('uw_tau2')))
    prg.add(749891239, "Picture Levit 2017 - setup")
    prg.add(749893339, "Delta 1 Current", 13.200)
    prg.add(749911239, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(750383339, "Config Field OFF.sub")
    prg.add(750393368, "Picture FastStingray TOF Ready Trig2")
    prg.add(766133793, "Set MOT NaK.sub")
    prg.add(766633793, "Dark Spot MOT load.sub")
    prg.add(766733793, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    from random import choice
    nreps = 100
    uw1 = [1, 1.3]
    uw2 = [2, 2.5]

    iters = [(choice(uw1), choice(uw2)) for q in range(nreps)]
    np.random.shuffle(iters)
    j = 0

    while(cmd.running):
        print('\n-------o-------')
        u1, u2 = iters[j]
        cmd.set_var('uw_tau', u1)
        cmd.set_var('uw_tau2', u2)
        print('\n')
        print('Run #%d/%d, with variables:\nrep = %g\nuw_tau = %g\n'%(j+1, len(iters), rep1, uw_tau1))
        cmd.run(wait_end=True, add_time=500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
