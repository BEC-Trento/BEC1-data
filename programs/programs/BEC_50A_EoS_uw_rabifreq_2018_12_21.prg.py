prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(0, "Set Marconi uw", frequency=1769.000000, amplitude=0.00, functions=dict(frequency=lambda x: x + 1e-3*cmd.get_var('uw_freq'), amplitude=lambda x: cmd.get_var('uw_amp')))
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
    prg.add(750010000, "empty.sub", enable=False)
    prg.add(754010000, "empty.sub")
    prg.add(754010000, "Picture SetRepumper")
    prg.add(754020000, "Picture SetImaging")
    prg.add(754420030, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(755020520, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(755020530, "Pulse uw", polarity=1, pulse_t=0.00000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(755090550, "Na Probe/Push (+) ON", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('uw_tau')))
    prg.add(755090550, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau') + 1e-3*cmd.get_var('uw_tau')))
    prg.add(755592930, "Picture Levit 2017 - setup")
    prg.add(755595030, "Delta 1 Current", 13.200)
    prg.add(756085030, "Config Field OFF.sub")
    prg.add(756095030, "Pulse TTL2-12", polarity=1, pulse_t=0.95600, enable=False)
    prg.add(756095060, "Picture NaK - new Stingray", enable=False)
    prg.add(756095060, "Picture NaK Ready - new Stingray", enable=False)
    prg.add(756095060, "Picture FastStingray Ready")
    prg.add(771835485, "Set MOT NaK.sub")
    prg.add(772335485, "Dark Spot MOT load.sub")
    prg.add(772435485, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 50, 4)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uw_tau1 = iters[j]
        cmd.set_var('uw_tau', uw_tau1)
        print('\n')
        print('Run #%d/%d, with variables:\nuw_tau = %g\n'%(j+1, len(iters), uw_tau1))
        cmd.run(wait_end=True, add_time=500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
