prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(11000, "TTL3-11 ON")
    prg.add(41000, "Optical Levit (-) Amp", 1000)
    prg.add(91000, "B comp y", 0.0000)
    prg.add(101000, "IGBT B comp y ON")
    prg.add(491000, "Bcomp y Sign Plus", enable=False)
    prg.add(1491000, "Set MOT NaK.sub")
    prg.add(1991000, "Dark Spot MOT load.sub")
    prg.add(2091000, "Config MOT.sub")
    prg.add(9000000, "Optical Levit ON")
    prg.add(10000000, "Synchronize.sub", enable=False)
    prg.add(19999000, "TTL2-12 ON")
    prg.add(20000000, "Melassa Na.sub")
    prg.add(20001000, "Melassa Na amp.sub")
    prg.add(20001500, "Config Field OFF.sub")
    prg.add(20002000, "TTL2-12 OFF")
    prg.add(20049500, "MOT lights Off.sub")
    prg.add(20050000, "Picture close SetImaging", enable=False)
    prg.add(20050000, "Picture close NaK.sub")
    prg.add(35044500, "Bx Grad OFF")
    prg.add(40045459, "Set MOT NaK.sub")
    prg.add(40545459, "Dark Spot MOT load.sub")
    prg.add(40645459, "Config MOT.sub")
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
