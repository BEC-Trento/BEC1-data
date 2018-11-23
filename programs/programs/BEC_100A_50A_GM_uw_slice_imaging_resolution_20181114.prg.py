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
    prg.add(30000000, "B comp x", 675.0)
    prg.add(45000000, "Evaporation Ramp.sub")
    prg.add(482003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(482010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(622010000, "empty.sub", enable=False)
    prg.add(627010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=6000.0000)
    prg.add(627020000, "B comp x ramp", start_t=0, stop_x=6000, n_points=200, start_x=675, stop_t=6000)
    prg.add(697020000, "empty.sub", enable=False)
    prg.add(697021660, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(697021660, "Picture Levit 2017 - 120ms", enable=False)
    prg.add(697021660, "IGBT 1 pinch", 10.0000)
    prg.add(697021670, "IGBT 4 Close")
    prg.add(697021690, "Delta 1 Voltage", 5.0000)
    prg.add(697023690, "Config Levitation zero current.sub")
    prg.add(697024190, "IGBT B comp x OFF")
    prg.add(697024690, "B comp x", 3600.0, enable=False)
    prg.add(697025790, "Delta 1 Current", 14.130)
    prg.add(697026830, "Pulse TTL2-12", polarity=1, pulse_t=0.06530)
    prg.add(697026840, "empty.sub")
    prg.add(697046840, "Pulse uw", polarity=1, pulse_t=1.00000)
    prg.add(697096840, "empty.sub")
    prg.add(697097840, "Config Field OFF.sub")
    prg.add(697107840, "Picture NaK for Levit 2017.sub")
    prg.add(697107840, "Picture NaK for Levit no Rep 2017.sub", enable=False)
    prg.add(712848265, "Set MOT NaK.sub")
    prg.add(713348265, "Dark Spot MOT load.sub")
    prg.add(713448265, "Config MOT.sub")
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
