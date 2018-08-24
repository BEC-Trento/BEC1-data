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
    prg.add(192600000, "Synchronize.sub", enable=False)
    prg.add(197500000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(200500000, "B comp x", 665.0)
    prg.add(215500000, "Evaporation Ramp.sub")
    prg.add(652503000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(652510000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(781720000, "empty.sub")
    prg.add(786720000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=2500.0000)
    prg.add(786730000, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=665, stop_t=2500)
    prg.add(821730000, "empty.sub")
    prg.add(826230000, "Picture SetImaging")
    prg.add(826330000, "Picture SetRepumper", enable=False)
    prg.add(826330000, "TTL2-12 ON", enable=False)
    prg.add(826430000, "Bx Grad ON")
    prg.add(826530000, "Bx Grad OFF")
    prg.add(827030000, "empty.sub")
    prg.add(827030000, "Pulse uw Ramp", start_t=0.0000, stop_x=0.0200, n_points=20, start_x=0.0080, stop_t=380.0000, functions=dict(time=lambda x: x + cmd.get_var('delay')))
    prg.add(827071000, "Picture Ramp Trig1", start_t=0.0000, stop_x=0.000, n_points=20, start_x=1.000, stop_t=380.0000, functions=dict(time=lambda x: x + cmd.get_var('delay')))
    prg.add(831571000, "Picture Quantum - 1 shot Trig1", functions=dict(time=lambda x: x + cmd.get_var('delay')))
    prg.add(832571000, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('delay')))
    prg.add(833571000, "Bx Grad OFF")
    prg.add(841589640, "TTL2-12 OFF")
    prg.add(841689640, "Pulse uw OFF")
    prg.add(841690900, "Set MOT NaK.sub")
    prg.add(842189640, "Dark Spot MOT load.sub")
    prg.add(842289640, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 20, 2)
    j = 0
    while(cmd.running):
        delay1 = iters[j]
        cmd.set_var('delay', delay1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndelay = %g\n'%(j+1, len(iters), delay1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
