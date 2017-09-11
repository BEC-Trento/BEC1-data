prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(12100000, "Shutter Probe Na Open", enable=False)
    prg.add(14550500, "Melassa Na.sub")
    prg.add(14551500, "Melassa Na amp.sub")
    prg.add(14552000, "Config Field OFF.sub")
    prg.add(14600000, "MOT lights Off.sub")
    prg.add(14611000, "B comp x", 1000.0)
    prg.add(14615000, "Delta 1 Current", 50.000)
    prg.add(14615010, "Delta 2 Voltage", 30.0000, enable=False)
    prg.add(14615020, "Config MT compr.sub")
    prg.add(14617020, "Mirrors Imaging", enable=False)
    prg.add(14617020, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=300.0000, enable=False)
    prg.add(14617020, "Decompress Current 200-100", start_t=200.0000, stop_x=100.000, n_points=300, start_x=0.000, stop_t=300.0000, enable=False)
    prg.add(14620020, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=300.0000, enable=False)
    prg.add(34620020, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(34620020, "Picture Levit 20170908.sub")
    prg.add(34620020, "Config Field OFF.sub", enable=False)
    prg.add(34620020, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(34620020, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(34620155, "TTL2-12 ON")
    prg.add(34628165, "Config Field OFF.sub", enable=False)
    prg.add(34633155, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(36418060, "TTL2-12 OFF")
    prg.add(43450655, "Set MOT NaK.sub")
    prg.add(43950655, "Dark Spot MOT load.sub")
    prg.add(44050655, "Config MOT.sub")
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
