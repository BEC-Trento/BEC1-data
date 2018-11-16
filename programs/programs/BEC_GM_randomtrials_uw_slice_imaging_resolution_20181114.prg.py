prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(52100000, "Synchronize.sub")
    prg.add(57000000, "[MAIN] Loading MOT - GM - MTC200A", enable=False)
    prg.add(57000000, "Loading MOT - GM - MTC50A")
    prg.add(60000000, "B comp x", 675.0)
    prg.add(70000000, "empty.sub", enable=False)
    prg.add(70010000, "B comp x ramp", start_t=0, stop_x=6000, n_points=200, start_x=675, stop_t=2000)
    prg.add(95010000, "empty.sub", enable=False)
    prg.add(95011660, "IGBT 1 pinch", 10.0000)
    prg.add(95011670, "IGBT 4 Close")
    prg.add(95011690, "Delta 1 Voltage", 5.0000)
    prg.add(95013690, "Config Levitation zero current.sub")
    prg.add(95014690, "B comp x", 3600.0)
    prg.add(95015790, "Delta 1 Current", 14.130)
    prg.add(95015790, "Pulse TTL2-12", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(95215790, "IGBT B comp x OFF")
    prg.add(95216790, "Pulse uw ON")
    prg.add(95216840, "Pulse uw OFF")
    prg.add(95216874, "Config Field OFF.sub")
    prg.add(95226874, "Picture NaK for Levit 2017.sub", enable=False)
    prg.add(95226874, "Picture NaK for Levit no Rep 2017.sub")
    prg.add(95226875, "empty.sub", enable=False)
    prg.add(95256988, "Config Field OFF.sub")
    prg.add(110997413, "Set MOT NaK.sub")
    prg.add(111497413, "Dark Spot MOT load.sub")
    prg.add(111597413, "Config MOT.sub")
    return prg
def commands(cmd):
    import os
    import numpy as np
    iters = np.arange(12.5, 50, 0.7)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        freq1 = iters[j]
        cmd.set_var('freq', freq1)
        comm = "python3 /home/stronzio/remote_device_marconi/MarconiComm.py %g"%(1e3*freq1)
        os.system(comm)
        print('\n')
        print('Run #%d/%d, with variables:\nfreq = %g\n'%(j+1, len(iters), freq1))
        cmd.run(wait_end=True, add_time=22000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
