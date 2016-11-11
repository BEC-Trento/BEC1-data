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
    prg.add(120000, "Bx Grad OFF")
    prg.add(1510000, "Set MOT NaK.sub")
    prg.add(2010000, "Dark Spot MOT load.sub")
    prg.add(2110000, "Config MOT.sub")
    prg.add(10010000, "Optical Levit ON")
    prg.add(160010000, "Melassa Na.sub")
    prg.add(160011000, "Melassa Na amp.sub")
    prg.add(160011500, "Config Field OFF.sub")
    prg.add(160059500, "MOT lights Off.sub")
    prg.add(160063500, "Delta 1 Current", 200.000)
    prg.add(160063510, "Delta 2 Voltage", 30.0000)
    prg.add(160063520, "Config MT compr.sub")
    prg.add(162067540, "All Shutter Close.sub")
    prg.add(165069540, "Mirrors Imaging")
    prg.add(165569540, "IGBT B comp x ON")
    prg.add(166069540, "All AOM On.sub")
    prg.add(169069900, "B comp x", 1030.0)
    prg.add(170059500, "Evaporation Ramp.sub")
    prg.add(320059500, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(320060000, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(344910000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(344917000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(428367000, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1000, stop_t=250)
    prg.add(428372000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(429372000, "B comp y ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=130)
    prg.add(429372050, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(430802000, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.500, n_points=100, start_x=2.000, stop_t=500.0000)
    prg.add(430802050, "Dipole Trap y ramp", start_t=0.0000, stop_x=1.000, n_points=200, start_x=2.000, stop_t=500.0000)
    prg.add(436002050, "LZ -1 to 0")
    prg.add(440502050, "Rabi preparation_Z")
    prg.add(443552050, "spin cleaning pinch", enable=False)
    prg.add(447402100, "ReleConfigBackForGravityComp")
    prg.add(447902100, "Rabi pulse_Z")
    prg.add(447907600, "Dipole Trap x DAC V", 0.0000)
    prg.add(447908100, "Dipole Trap y DAC V", -0.1000)
    prg.add(447909500, "Picture NaK.sub", enable=False)
    prg.add(447909500, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(447909500, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(447909500, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(447909500, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(447909500, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub")
    prg.add(447909500, "Picture - Field off at 0ms -SternGerlach_ShortTom15ms.sub", enable=False)
    prg.add(447909500, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(447909500, "Picture - Field off at 0ms -SternGerlach_ShortTom.sub", enable=False)
    prg.add(447909500, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub", enable=False)
    prg.add(448040999, "Picture NaK.sub", enable=False)
    prg.add(448040999, "Picture NaK no Rep.sub", enable=False)
    prg.add(453040999, "Bx Grad OFF", enable=False)
    prg.add(464814398, "Bias field initialization")
    prg.add(465665098, "Pulse uw OFF")
    prg.add(473899598, "Set MOT NaK.sub")
    prg.add(474399598, "Dark Spot MOT load.sub")
    prg.add(474499598, "Config MOT.sub")
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
