prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(202100000, "Synchronize.sub", enable=False)
    prg.add(207000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(210000000, "B comp x", 775.0)
    prg.add(225000000, "Evaporation Ramp.sub")
    prg.add(662003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(662010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(802010000, "empty.sub", enable=False)
    prg.add(804010000, "Config Field OFF.sub", enable=False)
    prg.add(804010000, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(804020000, "Picture NaK for Levit 2017.sub", enable=False)
    prg.add(804020010, "IGBT 4 Close")
    prg.add(804020030, "Delta 1 Voltage", 8.0000)
    prg.add(804020110, "Pulse TTL2-12", polarity=1, pulse_t=0.06530)
    prg.add(804020530, "Delta 1 Current", 50.000)
    prg.add(804022030, "Config Levitation zero current.sub")
    prg.add(804022290, "B comp x", 3000.0, enable=False)
    prg.add(804023290, "B comp y", 0.0000, enable=False)
    prg.add(804023290, "IGBT B comp x OFF", enable=False)
    prg.add(804082030, "DDS27 ch1 freq ramp", start_t=0.0000, stop_x=130.000, n_points=40, start_x=120.000, stop_t=2.0000, enable=False)
    prg.add(804082030, "DDS27 ch2 freq ramp", start_t=0.0000, stop_x=128.000, n_points=400, start_x=127.000, stop_t=2.0000)
    prg.add(804082030, "empty.sub")
    prg.add(804082048, "Pulse uw ON")
    prg.add(804102048, "Pulse uw OFF")
    prg.add(804102048, "empty.sub")
    prg.add(804103048, "Config Field OFF.sub")
    prg.add(804113048, "Picture NaK for Levit 2017.sub", enable=False)
    prg.add(804113048, "Picture NaK for Levit no Rep 2017.sub")
    prg.add(819853473, "Set MOT NaK.sub")
    prg.add(820353473, "Dark Spot MOT load.sub")
    prg.add(820453473, "Config MOT.sub")
    return prg
def commands(cmd):
    import os
    import numpy as np
    #amp_arr, freq_arr = np.mgrid[6:7:1, 1626.3:1629:0.1, ]
    #iters = list(zip(amp_arr.ravel(), freq_arr.ravel()))
    iters = [14]
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        amp1, freq1 = iters[j]
        print('\n')
        cmd.set_var('freq', freq1)
        comm = "python3 /home/stronzio/remote_device_marconi/MarconiComm.py"
        args = "--freq %g --amp %g"%(freq1, amp1)
        os.system(comm + " " + args)
        print('Run #%d/%d, with variables:\namp = %g\nfreq = %g\n'%(j+1, len(iters), amp1, freq1))
        cmd.run(wait_end=True, add_time=3000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd