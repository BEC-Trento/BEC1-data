prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(12096000, "Config Field OFF.sub")
    prg.add(12100000, "MOT lights Off TTL short.sub")
    prg.add(12105000, "mot imaging subroutine atoms probe bg")
    prg.add(17105000, "Set MOT NaK.sub")
    prg.add(17605000, "Dark Spot MOT load.sub")
    prg.add(17705000, "Config MOT.sub")
    prg.add(19000000, "Shutter Probe Na Open", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(260, 310, 5)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        zs_det1 = iters[j]
        cmd.set_var('zs_det', zs_det1)
        print('\n')
        print('Run #%d/%d, with variables:\nzs_det = %g\n'%(j+1, len(iters), zs_det1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
