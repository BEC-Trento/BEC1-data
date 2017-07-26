prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(2000000, "Rele 5 Open")
    prg.add(2000010, "Rele 3 Close")
    prg.add(2000020, "Rele 1 Close")
    prg.add(2000030, "Rele 2 Open")
    prg.add(2000040, "Rele 4 Open")
    prg.add(2000050, "IGBT 6 Close")
    prg.add(2000060, "IGBT 5 Close")
    prg.add(2000070, "IGBT 1 pinch", 10.0000)
    prg.add(2000080, "IGBT 2 pinch+comp", -10.0000)
    prg.add(2000089, "IGBT 3 Open")
    prg.add(2000100, "IGBT 4 Open")
    prg.add(3000100, "Delta 1 Current", 12.000)
    prg.add(4001040, "Delta 2 Current", 200.000)
    prg.add(4002040, "Delta 1 Voltage", 30.0000)
    prg.add(4003040, "Delta 2 Voltage", 0.0000)
    prg.add(5000000, "Set MOT NaK.sub")
    prg.add(5100000, "Dark Spot MOT load.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(100, 501, 80)
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
