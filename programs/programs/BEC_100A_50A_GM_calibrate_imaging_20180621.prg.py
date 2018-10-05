prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(252100000, "Synchronize.sub", enable=False)
    prg.add(257000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(260000000, "B comp x", 665.0)
    prg.add(275000000, "Evaporation Ramp.sub")
    prg.add(712003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(712010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(841220000, "empty.sub")
    prg.add(851220000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=4500.0000)
    prg.add(851230000, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=665, stop_t=4500)
    prg.add(910230000, "empty.sub")
    prg.add(910230000, "Config Levit 2017.sub", enable=False)
    prg.add(910232100, "Delta 1 Current", 10.000, enable=False)
    prg.add(910332100, "IGBT B comp x OFF", enable=False)
    prg.add(910337100, "Config Field OFF.sub", enable=False)
    prg.add(910347100, "Pulse uw ON", enable=False)
    prg.add(910347120, "Pulse uw OFF", enable=False)
    prg.add(910347154, "Picture NaK 20ms delay.sub")
    prg.add(910347154, "Picture NaK no Rep 20ms delay.sub", enable=False)
    prg.add(910377154, "Config Field OFF.sub")
    prg.add(926117579, "Set MOT NaK.sub")
    prg.add(926617579, "Dark Spot MOT load.sub")
    prg.add(926717579, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(5, 100, 10)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tau1 = iters[j]
        cmd.set_var('tau', tau1)
        print('\n')
        print('Run #%d/%d, with variables:\ntau = %g\n'%(j+1, len(iters), tau1))
        cmd.run(wait_end=True, add_time=23000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
