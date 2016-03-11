prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(5000, "TTL3-11 ON")
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(119950500, "Melassa Na.sub")
    prg.add(119951500, "Melassa Na amp.sub")
    prg.add(119952000, "Config Field OFF.sub")
    prg.add(120000000, "MOT lights Off.sub")
    prg.add(120004000, "Delta 1 Current", 200.000)
    prg.add(120004010, "Delta 2 Voltage", 30.0000)
    prg.add(120004020, "Config MT compr.sub")
    prg.add(122008040, "All Shutter Close.sub")
    prg.add(125010040, "Mirrors Imaging")
    prg.add(125510040, "IGBT B comp x ON")
    prg.add(126010040, "All AOM On.sub")
    prg.add(129010040, "B comp x", 325.0)
    prg.add(130000000, "Evaporation Ramp.sub")
    prg.add(540999900, "Dipole Trap x ramp", start_t=0.0000, stop_x=7.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(541000400, "Dipole Trap y ramp", start_t=0.0000, stop_x=1.800, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(567003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(567010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(649310900, "Config Field OFF.sub", enable=False)
    prg.add(649319900, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
    prg.add(649319900, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(674300000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=300.0000)
    prg.add(684290000, "Dipole Trap x DAC V", 0.0000)
    prg.add(684290500, "Dipole Trap y DAC V", -0.0900)
    prg.add(684295000, "Picture NaK.sub", enable=False)
    prg.add(684300000, "Picture - Field off at 0ms - Levit 50ms.sub", functions=dict(time=lambda x: x + cmd.get_var("t"), funct_enable=False))
    prg.add(684300000, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(684300000, "Picture - Field off at 0ms - Levit 100ms.sub", functions=dict(time=lambda x: x +  + cmd.get_var("t"), funct_enable=False), enable=False)
    prg.add(708482700, "Set MOT NaK.sub")
    prg.add(708982700, "Dark Spot MOT load.sub")
    prg.add(709082700, "Config MOT.sub")
    prg.add(720847862, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    return prg
def commands(cmd):
    from numpy import arange
    times=list(arange(0,20,1))
    times.reverse()
    while(cmd.running):
        print('actual: ', times[-1])
        print('real hold time : ', 1+times[-1])
        cmd.set_var("t", times.pop())
        print('Remaining: ',times)
        cmd.run()
        cmd.sleep(2000)
        if len(times) == 0:
         cmd.stop()
    return cmd