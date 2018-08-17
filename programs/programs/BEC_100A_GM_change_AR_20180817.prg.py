prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(207100000, "Synchronize.sub", enable=False)
    prg.add(212000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(215000000, "B comp x", 665.0)
    prg.add(230000000, "Evaporation Ramp.sub")
    prg.add(667003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(667010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(796220000, "empty.sub", enable=False)
    prg.add(801220000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=5500.0000)
    prg.add(801230000, "B comp x ramp", start_t=0, stop_x=750, n_points=400, start_x=665, stop_t=5500)
    prg.add(866230000, "empty.sub", enable=False)
    prg.add(866230000, "Bx Grad ON")
    prg.add(866330000, "Bx Grad OFF")
    prg.add(866331560, "Pulse TTL2-12", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(866331560, "Picture Levit 2017 - 30ms", functions=dict(time=lambda x: x + cmd.get_var('delay')))
    prg.add(866360000, "B comp x", 750.0, functions=dict(time=lambda x: x + cmd.get_var('delay')))
    prg.add(866361560, "Config Field OFF.sub", enable=False)
    prg.add(866366560, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('delay'), funct_enable=False), enable=False)
    prg.add(866396560, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('delay'), funct_enable=False), enable=False)
    prg.add(882136985, "Set MOT NaK.sub")
    prg.add(882636985, "Dark Spot MOT load.sub")
    prg.add(882736985, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    r_arr, delay_arr = np.mgrid[0:1:1, 10:140:20, ]
    iters = list(zip(r_arr.ravel(), delay_arr.ravel()))
    j = 0
    while(cmd.running):
        r1, delay1 = iters[j]
        cmd.set_var('r', r1)
        cmd.set_var('delay', delay1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nr = %g\ndelay = %g\n'%(j+1, len(iters), r1, delay1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
