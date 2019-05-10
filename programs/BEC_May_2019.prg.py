prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(20000, "Set MOT NaK.sub")
    prg.add(509000, "Dark Spot MOT load.sub")
    prg.add(609000, "Config MOT.sub")
    prg.add(60605000, "Config Field OFF.sub")
    prg.add(60609000, "MOT lights Off TTL.sub")
    prg.add(60610900, "Gray Molasses 2017")
    prg.add(60661900, "Load_Quad")
    prg.add(65661899, "Config Field OFF.sub", functions=dict(time=lambda x: 6066.19+cmd.get_var('Quad_time')))
    prg.add(65691899, "BEC_imaging", functions=dict(time=lambda x: 6066.19+cmd.get_var('Quad_time')+cmd.get_var('tof')))
    prg.add(85700800, "Set MOT NaK.sub")
    prg.add(86871400, "Dark Spot MOT load.sub")
    prg.add(86971400, "Config MOT.sub")
    prg.add(88700800, "TTL12 OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(10, 300, 20)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        Quad_time1 = iters[j]
        cmd.set_var('Quad_time', Quad_time1)
        print('\n')
        print('Run #%d/%d, with variables:\nQuad_time = %g\n'%(j+1, len(iters), Quad_time1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
