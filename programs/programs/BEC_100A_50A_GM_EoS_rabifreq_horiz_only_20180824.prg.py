prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(192600000, "Synchronize.sub", enable=False)
    prg.add(197500000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(200500000, "B comp x", 665.0)
    prg.add(215500000, "Evaporation Ramp.sub")
    prg.add(652503000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(652510000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(781720000, "empty.sub")
    prg.add(786720000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=300, start_x=100.000, stop_t=2500.0000)
    prg.add(786730000, "B comp x ramp", start_t=0, stop_x=750, n_points=300, start_x=665, stop_t=2500)
    prg.add(821730000, "Picture SetImaging")
    prg.add(821740109, "Picture SetRepumper")
    prg.add(822740109, "TTL2-12 ON", enable=False)
    prg.add(822748609, "TTL Repumper MOT ON", enable=False)
    prg.add(822750109, "Pulse uw", polarity=1, pulse_t=0.01100, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('t_uw')), enable=False)
    prg.add(822750109, "TTL Repumper MOT OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('tau'), funct_enable=False), enable=False)
    prg.add(822820109, "Picture Quantum - 1 shot Trig1")
    prg.add(823320109, "Picture Levit 2017 - setup")
    prg.add(823321109, "Delta 1 Current", 13.000)
    prg.add(823611109, "IGBT 4 Open")
    prg.add(823618309, "TTL Repumper MOT ON", enable=False)
    prg.add(823619809, "TTL Repumper MOT OFF", enable=False)
    prg.add(823619909, "Picture NaK Ready.sub")
    prg.add(823649909, "Config Field OFF.sub")
    prg.add(831572049, "TTL2-12 OFF", enable=False)
    prg.add(831672049, "Pulse uw OFF")
    prg.add(831673309, "Set MOT NaK.sub")
    prg.add(832172049, "Dark Spot MOT load.sub")
    prg.add(832272049, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    Label_arr, t_uw_arr = np.mgrid[1:2:1, 1:100:4, ]
    iters = list(zip(Label_arr.ravel(), t_uw_arr.ravel()))
    j = 0
    while(cmd.running):
        Label1, t_uw1 = iters[j]
        cmd.set_var('Label', Label1)
        cmd.set_var('t_uw', t_uw1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nLabel = %g\nt_uw = %g\n'%(j+1, len(iters), Label1, t_uw1))
        cmd.run(wait_end=True, add_time=2000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
