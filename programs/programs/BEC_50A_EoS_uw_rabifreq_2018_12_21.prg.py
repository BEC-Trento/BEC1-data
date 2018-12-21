prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(232100000, "Synchronize.sub", enable=False)
    prg.add(237000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(237000490, "Pulse TTL2-12", polarity=1, pulse_t=0.56900, enable=False)
    prg.add(240000000, "B comp x", 775.0)
    prg.add(255000000, "Evaporation Ramp.sub")
    prg.add(692003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(692010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(832010000, "empty.sub", enable=False)
    prg.add(836010000, "empty.sub")
    prg.add(836010000, "Picture SetRepumper")
    prg.add(836020000, "Picture SetImaging")
    prg.add(837020000, "Pulse uw", polarity=1, pulse_t=0.00000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(837090000, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(837090030, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(837090530, "Na Probe/Push (+) ON")
    prg.add(837090530, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau')))
    prg.add(837592910, "Picture Levit 2017 - setup")
    prg.add(837595010, "Delta 1 Current", 13.200)
    prg.add(838085010, "Config Field OFF.sub")
    prg.add(838095010, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(838095040, "Picture NaK - new Stingray", enable=False)
    prg.add(838095040, "Picture NaK Ready - new Stingray")
    prg.add(838095040, "Picture FastStingray", enable=False)
    prg.add(853835465, "Set MOT NaK.sub")
    prg.add(854335465, "Dark Spot MOT load.sub")
    prg.add(854435465, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(25, 50, 2)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uw_tau1 = iters[j]
        cmd.set_var('uw_tau', uw_tau1)
        print('\n')
        print('Run #%d/%d, with variables:\nuw_tau = %g\n'%(j+1, len(iters), uw_tau1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
