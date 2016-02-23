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
    prg.add(129010400, "B comp x", 325.0)
    prg.add(130000000, "Evaporation Ramp.sub")
    prg.add(540999900, "Dipole Trap x ramp", start_t=0.0000, stop_x=7.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(541000400, "Dipole Trap y ramp", start_t=0.0000, stop_x=1.800, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(567003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(567010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(674295000, "B comp x ramp", start_t=0, stop_x=0, n_points=300, start_x=319, stop_t=250)
    prg.add(676800000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(678810000, "LZ -1 to 0")
    prg.add(685770000, "spin cleaning pinch")
    prg.add(687780000, "ReleConfigBackForGravityComp")
    prg.add(688780000, "Rabi oscillation 0 to 1-1", enable=False)
    prg.add(688780000, "Rabi oscillation 0 to 1-1 New Antena")
    prg.add(689300000, "Dipole Trap y DAC V", 0.0000)
    prg.add(689301000, "Dipole Trap x DAC V", 0.0000)
    prg.add(689306000, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub")
    prg.add(689477000, "Picture NaK.sub", enable=False)
    prg.add(699495200, "Set MOT NaK.sub")
    prg.add(699995200, "Dark Spot MOT load.sub")
    prg.add(700095200, "Config MOT.sub")
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
