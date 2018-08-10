prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(122100000, "Synchronize.sub", enable=False)
    prg.add(127000000, "All Shutter Close 2017.sub")
    prg.add(127001490, "Pulse TTL2-12", polarity=1, pulse_t=0.54000)
    prg.add(127001500, "Config Field OFF.sub")
    prg.add(127004500, "MOT lights Off close.sub")
    prg.add(127005000, "Mirrors Imaging")
    prg.add(127006735, "Gray Molasses 2017")
    prg.add(127066735, "empty.sub")
    prg.add(127066735, "Loading_GM_Q50_MTC200A")
    prg.add(127070000, "TTL0-13 broken ON")
    prg.add(129191645, "B comp x", 665.0)
    prg.add(132000000, "All AOM On.sub")
    prg.add(147000000, "Evaporation Ramp.sub")
    prg.add(584003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(584010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(713220000, "empty.sub", enable=False)
    prg.add(718220000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(718230000, "B comp x ramp", start_t=0, stop_x=750, n_points=200, start_x=665, stop_t=1200)
    prg.add(738230000, "empty.sub", enable=False)
    prg.add(738231560, "Pulse TTL2-12", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(738231560, "TTL0-13 broken OFF", enable=False)
    prg.add(738231617, "Picture Levit 2017 - 10ms", enable=False)
    prg.add(738231617, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(738231617, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(738231617, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(738231617, "Pulse uw", polarity=1, pulse_t=0.00100, enable=False)
    prg.add(738231717, "Picture NaK no Rep short delay.sub", enable=False)
    prg.add(738231717, "Picture NaK short delay.sub")
    prg.add(738261717, "Config Field OFF.sub")
    prg.add(738266717, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(738296717, "Config Field OFF.sub", enable=False)
    prg.add(754037142, "Set MOT NaK.sub")
    prg.add(754537142, "Dark Spot MOT load.sub")
    prg.add(754637142, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.2, 3, 0.2)
    j = 0
    while(cmd.running):
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
