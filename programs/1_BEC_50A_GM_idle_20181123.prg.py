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
    prg.add(807010000, "Config Field OFF.sub")
    prg.add(807050000, "Picture NaK.sub")
    prg.add(807051685, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(807054045, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(807054045, "Picture Levit 2017 - 80ms", enable=False)
    prg.add(807054045, "Picture Levit 2017 - 120ms", enable=False)
    prg.add(822794470, "Set MOT NaK.sub")
    prg.add(823294470, "Dark Spot MOT load.sub")
    prg.add(823394470, "Config MOT.sub")
    return prg
def commands(cmd):
    import os
    import numpy as np
    # amp_arr = np.arange(6, 10, 100)
    # uw_tau_arr = np.arange(10, 100, 1000)
    freq1 = 1698.100
    amp_arr = [6]
    uw_tau_arr = [10]
    iters = list(zip(amp_arr, uw_tau_arr))
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        amp1, uw_tau1 = iters[j]
        cmd.set_var('amp', amp1)
        cmd.set_var('uw_tau', uw_tau1)
        print('\n')
        comm = "python3 /home/stronzio/remote_device_marconi/MarconiComm.py"
        args = "--freq %g --amp %g"%(freq1, amp1)
        os.system(comm + " " + args)
        print('Run #%d/%d, with variables:\namp = %g\nuw_tau = %g\n'%(j+1, len(iters), amp1, uw_tau1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
