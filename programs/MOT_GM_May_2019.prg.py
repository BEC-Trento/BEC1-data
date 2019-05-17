prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(100000, "Scope 1 Trigger ON")
    prg.add(200000, "Scope 1 Trigger OFF")
    prg.add(130100000, "Config Field OFF.sub")
    prg.add(130104000, "MOT lights Off TTL.sub")
    prg.add(130105900, "Gray Molasses 2017")
    prg.add(130156000, "Scope 2 Trigger ON")
    prg.add(135186899, "BEC_imaging", functions=dict(time=lambda x: 13015.69+cmd.get_var('Quad_time')+cmd.get_var('tof'), funct_enable=False))
    prg.add(140000000, "Scope 2 Trigger OFF")
    prg.add(150000000, "DarkSpotMOT_19.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(10, 30, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        Quad_voltage1 = iters[j]
        cmd.set_var('Quad_voltage', Quad_voltage1)
        print('\n')
        print('Run #%d/%d, with variables:\nQuad_voltage = %g\n'%(j+1, len(iters), Quad_voltage1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
