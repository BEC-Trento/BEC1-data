prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1489000, "Trigger LZ OFF")
    prg.add(1490000, "Trigger LZ ON")
    prg.add(1491000, "Trigger LZ OFF")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(32095990, "TTL2-12 OFF")
    prg.add(32096000, "Config Field OFF.sub")
    prg.add(32100000, "MOT lights Off TTL short.sub")
    prg.add(32101700, "TTL2-12 ON")
    prg.add(32101750, "TTL2-12 OFF")
    prg.add(32101800, "GrayMolassesPulse", enable=False)
    prg.add(32101800, "GM pulse", enable=False)
    prg.add(32101900, "Gray Molasses 2017")
    prg.add(32176900, "mot imaging subroutine atoms probe bg", functions=dict(time=lambda x: 2212.5000+cmd.get_var('tof'), funct_enable=False))
    prg.add(39136600, "Set MOT NaK.sub")
    prg.add(39636600, "Dark Spot MOT load.sub")
    prg.add(39736600, "Config MOT.sub")
    prg.add(41031600, "Shutter Probe Na Open", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 1, 0.05)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        B_comp_z1 = iters[j]
        cmd.set_var('B_comp_z', B_comp_z1)
        print('\n')
        print('Run #%d/%d, with variables:\nB_comp_z = %g\n'%(j+1, len(iters), B_comp_z1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
