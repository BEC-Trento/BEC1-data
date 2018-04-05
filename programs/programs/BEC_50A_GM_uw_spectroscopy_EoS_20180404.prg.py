prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(12390000, "Synchronize.sub", enable=False)
    prg.add(17390000, "All Shutter Close 2017.sub")
    prg.add(17391490, "TTL2-12 ON")
    prg.add(17391500, "Config Field OFF.sub")
    prg.add(17394500, "MOT lights Off close.sub")
    prg.add(17395000, "Mirrors Imaging")
    prg.add(17396735, "Gray Molasses 2017")
    prg.add(17456735, "empty.sub")
    prg.add(17456735, "Delta 1 Current", 50.000)
    prg.add(17456955, "Config MOT.sub")
    prg.add(17481645, "Delta 1 Voltage", 15.0000)
    prg.add(19481645, "Config MOT to MT compr.sub")
    prg.add(19484910, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(19486555, "B comp x", 915.0)
    prg.add(20486555, "Delta 1 Voltage", 30.0000)
    prg.add(23294910, "All AOM On.sub")
    prg.add(38294910, "empty.sub")
    prg.add(43284910, "TTL2-12 ON")
    prg.add(43294910, "Pulse uw ON")
    prg.add(43294984, "Pulse uw OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False))
    prg.add(43295984, "Picture NaK no Rep Trig2.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False))
    prg.add(43295984, "Picture NaK Trig 2.sub", enable=False)
    prg.add(48295984, "Picture Levit 2017 - 30ms")
    prg.add(48295984, "Picture Levit 2017 - 50ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(48295984, "Picture Levit 2017 - 65ms", enable=False)
    prg.add(48295984, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(48295984, "Picture Levit 2017 - 120ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(48295984, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(50094984, "TTL2-12 ON", enable=False)
    prg.add(51295884, "Picture NaK Trig12.sub", enable=False)
    prg.add(51295884, "Picture NaK.sub", enable=False)
    prg.add(59314524, "TTL2-12 OFF")
    prg.add(59414524, "Pulse uw OFF")
    prg.add(59415784, "Set MOT NaK.sub")
    prg.add(59914524, "Dark Spot MOT load.sub")
    prg.add(60014524, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 20, 3)
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
