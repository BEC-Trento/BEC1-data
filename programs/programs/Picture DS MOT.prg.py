prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(97000000, "Shutter Probe Na Open")
    prg.add(100001674, "Config Field OFF.sub")
    prg.add(100001737, "MOT lights Off close.sub")
    prg.add(100005268, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(108830252, "Set MOT NaK.sub")
    prg.add(109330252, "Dark Spot MOT load.sub")
    prg.add(109430252, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    dt_arr, count_arr = np.mgrid[2:12:1, 0:3:1, ]
    iters = list(zip(dt_arr.ravel(), count_arr.ravel()))
    j = 0
    while(cmd.running):
        dt1, count1 = iters[j]
        cmd.set_var('dt', dt1)
        cmd.set_var('count', count1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\ncount = %g\n'%(j+1, len(iters), dt1, count1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
