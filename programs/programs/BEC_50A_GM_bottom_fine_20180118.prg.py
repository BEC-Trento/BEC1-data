prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(2200000, "Bottom Evaporation OFF")
    prg.add(115100000, "Synchronize.sub", enable=False)
    prg.add(120100000, "All Shutter Close 2017.sub")
    prg.add(120101490, "TTL2-12 ON")
    prg.add(120101500, "Config Field OFF.sub")
    prg.add(120104500, "MOT lights Off close.sub")
    prg.add(120105000, "Mirrors Imaging")
    prg.add(120106735, "Gray Molasses 2017")
    prg.add(120166735, "empty.sub")
    prg.add(120166735, "Loading_GM_Q50_MTC200A")
    prg.add(122291645, "B comp x", 945.0)
    prg.add(140100000, "Evaporation Ramp.sub")
    prg.add(577103000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(577110000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(684400000, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(686400000, "empty.sub", enable=False)
    prg.add(686400000, "RFO FM amp", 2.0000)
    prg.add(686400100, "Bottom Evaporation ON")
    prg.add(686400200, "RFO Trig Sweep burst", start_t=0.0000, stop_x=0.000, n_points=6, start_x=1.000, stop_t=15.0000)
    prg.add(686600200, "Bottom Evaporation OFF")
    prg.add(686600300, "RFO FM amp", 0.0000)
    prg.add(686602300, "Pulse uw ON", enable=False)
    prg.add(686602320, "Pulse uw OFF", enable=False)
    prg.add(686603320, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(686603320, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(686603320, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(686603320, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(686603320, "Picture Levit 2017 - 80ms", enable=False)
    prg.add(686603320, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(686603320, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(686603320, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(686603320, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(686613320, "Picture NaK.sub")
    prg.add(686613320, "Picture NaK no Rep.sub", enable=False)
    prg.add(686613320, "empty.sub", enable=False)
    prg.add(694613320, "Set MOT NaK.sub")
    prg.add(695113320, "Dark Spot MOT load.sub")
    prg.add(695213320, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(202, 302, 2)
    j = 0
    while(cmd.running):
        t1 = iters[j]
        cmd.set_var('t', t1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nt = %g\n'%(j+1, len(iters), t1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
