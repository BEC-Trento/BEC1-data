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
    prg.add(837010000, "empty.sub")
    prg.add(837010000, "Pulse uw", polarity=1, pulse_t=0.00000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(837060000, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(837060030, "Picture FastStingray", enable=False)
    prg.add(837060030, "Picture NaK - new Stingray")
    prg.add(838060030, "Config Field OFF.sub")
    prg.add(838062410, "Picture Levit 2017 - setup", enable=False)
    prg.add(838064510, "Delta 1 Current", 13.200, enable=False)
    prg.add(838554510, "Config Field OFF.sub", enable=False)
    prg.add(838564510, "Pulse TTL2-12", polarity=1, pulse_t=0.95600, enable=False)
    prg.add(838564540, "Picture FastStingray", enable=False)
    prg.add(854304965, "Set MOT NaK.sub")
    prg.add(854804965, "Dark Spot MOT load.sub")
    prg.add(854904965, "Config MOT.sub")
    return prg
def commands(cmd):
    import os
    import numpy as np
    iters = np.arange(450, 550, 10)
    #iters = [400]
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uw_freq1 = iters[j]
        cmd.set_var('uw_freq', uw_freq1)
        fr = 1e-3*uw_freq1 + 1769
        comm = "python3 devices/marconi/MarconiComm.py"
        args = " --freq %.9f"%(fr)
        os.system(comm+args)
        print('\n')
        print('Run #%d/%d, with variables:\nuw_freq = %g\n'%(j+1, len(iters), uw_freq1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
