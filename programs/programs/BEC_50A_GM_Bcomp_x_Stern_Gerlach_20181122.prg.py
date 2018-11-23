prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(22100000, "Synchronize.sub")
    prg.add(27000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(30000000, "B comp x", 775.0)
    prg.add(45000000, "Evaporation Ramp.sub")
    prg.add(482003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(482010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(622010000, "empty.sub", enable=False)
    prg.add(627010000, "Config Field OFF.sub", enable=False)
    prg.add(627010300, "Pulse TTL2-12", polarity=1, pulse_t=0.06530, enable=False)
    prg.add(627011250, "B comp x SG", enable=False)
    prg.add(627170250, "Picture NaK for Levit 2017.sub", enable=False)
    prg.add(627170250, "Picture Levit 2017 - setup")
    prg.add(627171250, "Delta 1 Current", 13.000)
    prg.add(627672250, "Config Field OFF.sub")
    prg.add(627682250, "B comp x SG")
    prg.add(627812250, "Picture NaK for Levit 2017.sub")
    prg.add(627812250, "Picture NaK for Levit no Rep 2017.sub", enable=False)
    prg.add(643552675, "Set MOT NaK.sub")
    prg.add(644052675, "Dark Spot MOT load.sub")
    prg.add(644152675, "Config MOT.sub")
    return prg
def commands(cmd):
    import os
    import numpy as np
    iters = np.arange(1697.0, 1698, 0.1)
    iters = [1670.06]
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        freq1 = iters[j]
        cmd.set_var('freq', freq1)
        comm = "python3 /home/stronzio/remote_device_marconi/MarconiComm.py %g"%freq1
        os.system(comm)
        print('\n')
        print('Run #%d/%d, with variables:\nfreq = %g\n'%(j+1, len(iters), freq1))
        cmd.run(wait_end=True, add_time=20000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
