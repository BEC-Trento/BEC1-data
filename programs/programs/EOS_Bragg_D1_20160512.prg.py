prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(11000, "TTL3-11 ON")
    prg.add(48420, "Optical Levit (-) Amp", 1000)
    prg.add(98420, "B comp y", 0.0000)
    prg.add(108420, "IGBT B comp y ON")
    prg.add(498420, "Bcomp y Sign Plus", enable=False)
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(49950500, "Melassa Na.sub")
    prg.add(49951500, "Melassa Na amp.sub")
    prg.add(49952000, "Config Field OFF.sub")
    prg.add(50000000, "MOT lights Off.sub")
    prg.add(50004000, "Delta 1 Current", 200.000)
    prg.add(50004010, "Delta 2 Voltage", 30.0000)
    prg.add(50004020, "Config MT compr.sub")
    prg.add(52008040, "All Shutter Close.sub")
    prg.add(55010040, "Mirrors Imaging")
    prg.add(55510040, "IGBT B comp x ON")
    prg.add(56010040, "All AOM On.sub")
    prg.add(59010040, "B comp x", 1005.0)
    prg.add(60000000, "Evaporation Ramp.sub")
    prg.add(497003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(497010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(614500000, "Bragg pulse D1", enable=False)
    prg.add(614500000, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(614500000, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(614500000, "Picture - Field off at 0ms - Levit 80ms.sub", enable=False)
    prg.add(614500000, "Picture - Field off at 0ms - Levit 60ms.sub", enable=False)
    prg.add(614500000, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(614500000, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(614500000, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(614530000, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var("t"), funct_enable=False))
    prg.add(614531000, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var("t"), funct_enable=False))
    prg.add(622161000, "Set MOT NaK.sub")
    prg.add(622661000, "Dark Spot MOT load.sub")
    prg.add(622761000, "Config MOT.sub")
    return prg
def commands(cmd):
    from numpy import arange
    times=list(arange(0, 5, 1))
    times.reverse()
    while(cmd.running):
        print('actual: ', times[-1])
        cmd.set_var("t", times.pop())
        print('Remaining: ',times)
        print('Using: ', cmd.get_var('t'))
        cmd.run()
        cmd.sleep(2000)
        if len(times) == 0:
         cmd.stop()
    return cmd
