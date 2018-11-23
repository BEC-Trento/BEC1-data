prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(22000000, "Fluo Lock", 200.0000)
    prg.add(22100000, "Synchronize.sub")
    prg.add(27000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(30000000, "B comp x", 775.0)
    prg.add(45000000, "Evaporation Ramp.sub")
    prg.add(482003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(482010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(622010000, "empty.sub", enable=False)
    prg.add(627010000, "Config Field OFF.sub", enable=False)
    prg.add(627020000, "Picture NaK for Levit 2017.sub", enable=False)
    prg.add(627020010, "IGBT 4 Close")
    prg.add(627020030, "Delta 1 Voltage", 8.0000)
    prg.add(627020110, "Pulse TTL2-12", polarity=1, pulse_t=0.06530)
    prg.add(627022030, "Config Levitation zero current.sub")
    prg.add(627022290, "B comp x", 3000.0, enable=False)
    prg.add(627023290, "B comp y", 0.0000, enable=False)
    prg.add(627052030, "Optical Levit (+) freq ramp", start_t=0.0000, stop_x=125.000, n_points=100, start_x=100.000, stop_t=5.0000, enable=False)
    prg.add(627092039, "Pulse uw", polarity=1, pulse_t=0.01000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(627092039, "Pulse uw ON", enable=False)
    prg.add(627102039, "Pulse uw OFF", enable=False)
    prg.add(627102039, "empty.sub", enable=False)
    prg.add(627113039, "Config Field OFF.sub")
    prg.add(627123039, "Picture NaK for Levit 2017.sub")
    prg.add(627123039, "Picture NaK for Levit no Rep 2017.sub", enable=False)
    prg.add(642863464, "Set MOT NaK.sub")
    prg.add(643363464, "Dark Spot MOT load.sub")
    prg.add(643463464, "Config MOT.sub")
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
