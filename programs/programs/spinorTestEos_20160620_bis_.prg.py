prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(8000, "Pulse uw OFF")
    prg.add(11000, "TTL3-11 ON")
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(40000500, "Melassa Na.sub")
    prg.add(40001500, "Melassa Na amp.sub")
    prg.add(40002000, "Config Field OFF.sub")
    prg.add(40050000, "MOT lights Off.sub")
    prg.add(40054000, "Delta 1 Current", 200.000)
    prg.add(40054010, "Delta 2 Voltage", 30.0000)
    prg.add(40054020, "Config MT compr.sub")
    prg.add(42058040, "All Shutter Close.sub")
    prg.add(45060040, "Mirrors Imaging")
    prg.add(45560040, "IGBT B comp x ON")
    prg.add(46060040, "All AOM On.sub")
    prg.add(49060400, "B comp x", 1000.0)
    prg.add(50050000, "Evaporation Ramp.sub")
    prg.add(200050000, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(200050500, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(226053100, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(226060100, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(308365000, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1000, stop_t=250)
    prg.add(308370000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(309370000, "B comp y ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=130)
    prg.add(309370050, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(310800050, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=200, start_x=2.000, stop_t=10.0000)
    prg.add(310810050, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=10.0000)
    prg.add(311010050, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=6.000, stop_t=10.0000, enable=False)
    prg.add(311020050, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=10.0000, enable=False)
    prg.add(311220050, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(311230050, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(312830050, "LZ -1 to 0", enable=False)
    prg.add(317830050, "MW repump preparation")
    prg.add(320880050, "spin cleaning pinch", enable=False)
    prg.add(323880050, "Bcomp y Sign Minus", enable=False)
    prg.add(324730100, "ReleConfigBackForGravityComp")
    prg.add(324730100, "ReleConfigBackForAntiGravityComp", enable=False)
    prg.add(325230100, "Rabi pulse New Antena", enable=False)
    prg.add(326230100, "Pulse uw ON", enable=False)
    prg.add(326230550, "Pulse uw OFF", enable=False)
    prg.add(326231050, "Dipole Trap y DAC V", -0.1000)
    prg.add(326231450, "Dipole Trap x DAC V", 0.0000)
    prg.add(326231450, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(326231450, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(326231450, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(326231450, "Picture - Field off at 0ms -SternGerlach_ShortTom.sub", enable=False)
    prg.add(326231450, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub", enable=False)
    prg.add(326231450, "Picture - Field off at 0ms -SternGerlach_ShortElena_NoRepump.sub", enable=False)
    prg.add(326231450, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(326231450, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(326231450, "Picture - Field off at 0ms - Levit 30ms-SternGerlach.sub", enable=False)
    prg.add(326231450, "Picture - Field off at 0ms - AntiLevit 50ms.sub", enable=False)
    prg.add(326371550, "Picture NaK.sub")
    prg.add(326371550, "Picture NaK no Rep.sub", enable=False)
    prg.add(327871550, "Dipole Trap x DAC V", 0.0000)
    prg.add(327891550, "Dipole Trap y DAC V", -0.1000)
    prg.add(339764950, "Bias field initialization")
    prg.add(340515650, "Pulse uw OFF")
    prg.add(348750150, "Set MOT NaK.sub")
    prg.add(349250150, "Dark Spot MOT load.sub")
    prg.add(349350150, "Config MOT.sub")
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