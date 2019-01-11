prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(0, "Set Marconi uw", frequency=1769.000000, amplitude=0.00, functions=dict(frequency=lambda x: x + 1e-3*cmd.get_var('uw_freq'), amplitude=lambda x: cmd.get_var('uw_amp')))
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(252100000, "Synchronize.sub", enable=False)
    prg.add(257000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(257000490, "Pulse TTL2-12", polarity=1, pulse_t=0.56900, enable=False)
    prg.add(260000000, "B comp x", 775.0)
    prg.add(275000000, "Evaporation Ramp.sub")
    prg.add(712003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(712010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(882010000, "empty.sub", enable=False)
    prg.add(886010000, "empty.sub")
    prg.add(886010000, "Picture SetRepumper")
    prg.add(886020000, "Picture SetImaging")
    prg.add(887020000, "Pulse uw", polarity=1, pulse_t=0.00000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(887090000, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(887090030, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(887090530, "Na Probe/Push (+) ON")
    prg.add(887090530, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau')))
    prg.add(887592910, "Picture Levit 2017 - setup")
    prg.add(887595010, "Delta 1 Current", 13.200)
    prg.add(888085010, "Config Field OFF.sub")
    prg.add(888095010, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(888095040, "Picture NaK - new Stingray", enable=False)
    prg.add(888095040, "Picture NaK Ready - new Stingray")
    prg.add(888095040, "Picture FastStingray", enable=False)
    prg.add(903835465, "Set MOT NaK.sub")
    prg.add(904335465, "Dark Spot MOT load.sub")
    prg.add(904435465, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(550, 650, 10)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uw_freq1 = iters[j]
        cmd.set_var('uw_freq', uw_freq1)
        print('\n')
        print('Run #%d/%d, with variables:\nuw_freq = %g\n'%(j+1, len(iters), uw_freq1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
