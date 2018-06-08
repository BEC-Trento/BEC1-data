prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(197550000, "Shutter Probe Na Open")
    prg.add(199950560, "Compress MOT Na", enable=False)
    prg.add(200151560, "Melassa Na.sub")
    prg.add(200152560, "Melassa Na amp.sub")
    prg.add(200153060, "Config Field OFF.sub")
    prg.add(200203060, "MOT lights Off close.sub")
    prg.add(200283060, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(209100560, "Set MOT NaK.sub")
    prg.add(209600560, "Dark Spot MOT load.sub")
    prg.add(209700560, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(3000, 5001, 500)
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