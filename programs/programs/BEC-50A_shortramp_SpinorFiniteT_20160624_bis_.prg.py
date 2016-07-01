prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Bx Grad OFF")
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
    prg.add(110000500, "Melassa Na.sub")
    prg.add(110001500, "Melassa Na amp.sub")
    prg.add(110002000, "Config Field OFF.sub")
    prg.add(110050000, "MOT lights Off.sub")
    prg.add(110054000, "Delta 1 Current", 200.000)
    prg.add(110054010, "Delta 2 Voltage", 30.0000)
    prg.add(110054020, "Config MT compr.sub")
    prg.add(112058040, "All Shutter Close.sub")
    prg.add(115060040, "Mirrors Imaging")
    prg.add(115560040, "IGBT B comp x ON")
    prg.add(116060040, "All AOM On.sub")
    prg.add(119060400, "B comp x", 1000.0)
    prg.add(120050000, "Evaporation Ramp.sub")
    prg.add(270050000, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(270050500, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(296053100, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(296060100, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(378365000, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1000, stop_t=250)
    prg.add(378370000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(379370000, "B comp y ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=130)
    prg.add(379370050, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(380800050, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=200, start_x=2.000, stop_t=50.0000)
    prg.add(380810050, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=50.0000)
    prg.add(381010050, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=6.000, stop_t=10.0000, enable=False)
    prg.add(381020050, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=10.0000, enable=False)
    prg.add(381220050, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(381230050, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(382830050, "LZ -1 to 0")
    prg.add(387330050, "Rabi preparation 2")
    prg.add(390380050, "spin cleaning pinch")
    prg.add(393380050, "Bcomp y Sign Minus", enable=False)
    prg.add(394230100, "ReleConfigBackForGravityComp")
    prg.add(394230100, "ReleConfigBackForAntiGravityComp", enable=False)
    prg.add(394730100, "Rabi pulse New Antena")
    prg.add(394735100, "Pulse uw ON")
    prg.add(399739400, "Dipole Trap y DAC V", -0.1000)
    prg.add(399739800, "Dipole Trap x DAC V", 0.0000)
    prg.add(399740000, "Pulse uw OFF", enable=False)
    prg.add(399744800, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(399744800, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub")
    prg.add(399744800, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(399744800, "Picture - Field off at 0ms -SternGerlach_ShortTom.sub", enable=False)
    prg.add(399744800, "Picture - Field off at 0ms -SternGerlach_ShortTom15ms.sub", enable=False)
    prg.add(399744800, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub", enable=False)
    prg.add(399754800, "Picture NaK no Rep.sub", enable=False)
    prg.add(399754800, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(399754800, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(399754800, "Picture - Field off at 0ms - Levit 30ms-SternGerlach.sub", enable=False)
    prg.add(399754800, "Picture - Field off at 0ms - AntiLevit 50ms.sub", enable=False)
    prg.add(399924800, "Picture NaK.sub", enable=False)
    prg.add(411798200, "Bias field initialization")
    prg.add(412548900, "Pulse uw OFF")
    prg.add(420783400, "Set MOT NaK.sub")
    prg.add(421283400, "Dark Spot MOT load.sub")
    prg.add(421383400, "Config MOT.sub")
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