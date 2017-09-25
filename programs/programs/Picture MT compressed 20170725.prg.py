prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(197550000, "Shutter Probe Na Open")
    prg.add(200000500, "Melassa Na.sub")
    prg.add(200001500, "Melassa Na amp.sub")
    prg.add(200002000, "Config Field OFF.sub")
    prg.add(200003350, "MOT lights Off.sub")
    prg.add(200007350, "Delta 1 Current", 200.000)
    prg.add(200007360, "Delta 2 Voltage", 30.0000)
    prg.add(200007370, "Config MT compr.sub", enable=False)
    prg.add(200007370, "Config MOT.sub")
    prg.add(200009370, "Mirrors Imaging")
    prg.add(201009370, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=300.0000)
    prg.add(201012370, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=300.0000)
    prg.add(204512370, "Config Field OFF.sub")
    prg.add(204527370, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(213344870, "Set MOT NaK.sub")
    prg.add(213844870, "Dark Spot MOT load.sub")
    prg.add(213944870, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    dt_arr, count_arr = np.mgrid[3:10:2, 0:2:1, ]
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
