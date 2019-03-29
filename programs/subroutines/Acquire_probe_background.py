prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(12580, "B comp x", 0.0, enable=False)
    prg.add(50000, "Optical Levit (-) Amp", 1000, enable=False)
    prg.add(100000, "B comp y", 0.0000, enable=False)
    prg.add(121000, "IGBT B comp y ON", enable=False)
    prg.add(12000000, "Mirrors Imaging")
    prg.add(12000000, "All Shutter Close.sub")
    prg.add(12049500, "MOT lights Off.sub")
    prg.add(22055520, "IGBT B comp x ON")
    prg.add(27555520, "RFO SetImaging+Ref", enable=False)
    prg.add(27555520, "Picture SetImaging")
    prg.add(28055520, "All AOM On.sub")
    prg.add(29155510, "RFO ImagingQuatum Ramp", start_t=0.0000, stop_x=0.000, n_points=150, start_x=1.000, stop_t=14900.0000)
    prg.add(180155510, "startup.prg")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 500, 15)
    j = 0
    while(cmd.running):
        dt1 = iters[j]
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\n'%(j+1, len(iters), dt1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
