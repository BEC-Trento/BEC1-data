prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(2200000, "Bx Grad OFF")
    prg.add(2300000, "Bottom Evaporation OFF")
    prg.add(2310000, "RFO FM amp", 0.0000)
    prg.add(192710000, "Synchronize.sub", enable=False)
    prg.add(197610000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(200610000, "B comp x", 665.0)
    prg.add(215610000, "Evaporation Ramp.sub")
    prg.add(652613000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(652620000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(781830000, "empty.sub")
    prg.add(786830000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=2500.0000)
    prg.add(786840000, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=665, stop_t=2500)
    prg.add(821840000, "empty.sub")
    prg.add(826340000, "Picture SetImaging", enable=False)
    prg.add(826440000, "Picture SetRepumper", enable=False)
    prg.add(826440000, "TTL2-12 ON", enable=False)
    prg.add(826640000, "empty.sub")
    prg.add(826740000, "RFO FM amp", 0.5000, enable=False)
    prg.add(826940000, "Pulse RFO Sweep Trig", polarity=1, pulse_t=0.16500, enable=False)
    prg.add(826941000, "Pulse RFO Bottom Evap", polarity=1, pulse_t=4.00000, enable=False)
    prg.add(826941000, "Pulse uw", polarity=1, pulse_t=0.02000)
    prg.add(826991000, "Picture NaK Ready no Rep.sub", enable=False)
    prg.add(826991000, "Picture NaK Ready.sub", enable=False)
    prg.add(826991000, "Picture NaK.sub")
    prg.add(827191000, "Config Field OFF.sub")
    prg.add(827291000, "RFO FM amp", 0.0000)
    prg.add(833791000, "Bx Grad OFF")
    prg.add(841809640, "TTL2-12 OFF")
    prg.add(841909640, "Pulse uw OFF")
    prg.add(841910900, "Set MOT NaK.sub")
    prg.add(842409640, "Dark Spot MOT load.sub")
    prg.add(842509640, "Config MOT.sub")
    return prg
def commands(cmd):
    import os
    import numpy as np
    iters = np.arange(1780, 1880, 20)
    j = 0
    cmd.set_var('series', 3)
    while(cmd.running):
        freq1 = iters[j]
        cmd.set_var('freq', freq1)
        comm = "python3 /home/stronzio/marconi_remote/MarconiComm.py %g"%freq1
        os.system(comm)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nfreq = %g\n'%(j+1, len(iters), freq1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
