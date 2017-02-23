prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(8000, "Pulse uw OFF")
    prg.add(11000, "TTL3-11 ON")
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(120000, "Bx Grad OFF")
    prg.add(1510000, "Set MOT NaK.sub")
    prg.add(2010000, "Dark Spot MOT load.sub")
    prg.add(2110000, "Config MOT.sub")
    prg.add(10010000, "Optical Levit ON")
    prg.add(11010000, "Synchronize.sub")
    prg.add(12010000, "Melassa Na.sub")
    prg.add(12011000, "Melassa Na amp.sub")
    prg.add(12011500, "Config Field OFF.sub")
    prg.add(12059500, "MOT lights Off.sub")
    prg.add(12063500, "Delta 1 Current", 200.000)
    prg.add(12063510, "Delta 2 Voltage", 30.0000)
    prg.add(12063520, "Config MT compr.sub")
    prg.add(14067540, "All Shutter Close.sub")
    prg.add(17069540, "Mirrors Imaging")
    prg.add(17569540, "IGBT B comp x ON")
    prg.add(18069540, "All AOM On.sub")
    prg.add(21069900, "B comp x", 1025.0)
    prg.add(22059500, "Evaporation Ramp.sub")
    prg.add(172059500, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.500, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(172060000, "Dipole Trap y ramp", start_t=0.0000, stop_x=3.500, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(196910000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(196917000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(280367000, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1045, stop_t=250)
    prg.add(280372000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(281372000, "B comp y ramp", start_t=0, stop_x=3, n_points=200, start_x=0, stop_t=130)
    prg.add(281372050, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(282802050, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.500, n_points=200, start_x=2.000, stop_t=100.0000, enable=False)
    prg.add(282812050, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=2.000, stop_t=100.0000, enable=False)
    prg.add(284412050, "heating dipole", enable=False)
    prg.add(294412050, "LZ -1 to 0", enable=False)
    prg.add(300912050, "spin cleaning pinch", enable=False)
    prg.add(304412050, "Rabi preparation 2", enable=False)
    prg.add(308782100, "ReleConfigBackForGravityComp", enable=False)
    prg.add(309282100, "Rabi pulse New Antena", enable=False)
    prg.add(309282100, "Bx Grad OFF", enable=False)
    prg.add(309282100, "Bx Grad ON", enable=False)
    prg.add(309282100, "heating dipole", enable=False)
    prg.add(309286400, "Dipole Trap x DAC V", 0.0000)
    prg.add(309286500, "Dipole Trap y DAC V", -0.1000)
    prg.add(309286500, "Picture NaK.sub", enable=False)
    prg.add(309286500, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(309286500, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(309286500, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(309286500, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(309286500, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub")
    prg.add(309286500, "Picture - Field off at 0ms -SternGerlach_Ele.sub", enable=False)
    prg.add(309286500, "Picture - Field off at 0ms -SternGerlach_ShortTom15ms.sub", enable=False)
    prg.add(309286500, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(309286500, "Picture - Field off at 0ms -SternGerlach_ShortTom.sub", enable=False)
    prg.add(309286500, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub", enable=False)
    prg.add(309456500, "Picture NaK.sub", enable=False)
    prg.add(309456500, "Picture NaK no Rep.sub", enable=False)
    prg.add(310000000, "Dipole Trap x DAC V", 0.0000)
    prg.add(314456500, "Bx Grad OFF")
    prg.add(326229899, "Bias field initialization")
    prg.add(327080599, "Pulse uw OFF")
    prg.add(335315099, "Set MOT NaK.sub")
    prg.add(335815099, "Dark Spot MOT load.sub")
    prg.add(335915099, "Config MOT.sub")
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
