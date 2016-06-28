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
    prg.add(60000500, "Melassa Na.sub")
    prg.add(60001500, "Melassa Na amp.sub")
    prg.add(60002000, "Config Field OFF.sub")
    prg.add(60050000, "MOT lights Off.sub")
    prg.add(60054000, "Delta 1 Current", 200.000)
    prg.add(60054010, "Delta 2 Voltage", 30.0000)
    prg.add(60054020, "Config MT compr.sub")
    prg.add(62058040, "All Shutter Close.sub")
    prg.add(65060040, "Mirrors Imaging")
    prg.add(65560040, "IGBT B comp x ON")
    prg.add(66060040, "All AOM On.sub")
    prg.add(69060400, "B comp x", 1000.0)
    prg.add(70050000, "Evaporation Ramp.sub")
    prg.add(220050000, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=300, start_x=0.000, stop_t=2000.0000)
    prg.add(220050500, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=300, start_x=-0.100, stop_t=2000.0000)
    prg.add(246053100, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(246060100, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(328365000, "B comp x ramp", start_t=0, stop_x=1369, n_points=300, start_x=1000, stop_t=250)
    prg.add(328370000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=200.0000)
    prg.add(329370000, "B comp y ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=130)
    prg.add(329370050, "Analog71 Ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.325, stop_t=130.0000)
    prg.add(330800050, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=200, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(330810050, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(331010050, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=6.000, stop_t=10.0000, enable=False)
    prg.add(331020050, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=10.0000, enable=False)
    prg.add(331220050, "Dipole Trap y ramp", start_t=0.0000, stop_x=6.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(331230050, "Dipole Trap x ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=2.000, stop_t=10.0000, enable=False)
    prg.add(333730050, "LZ -1 to 0")
    prg.add(343730050, "MW repump preparation")
    prg.add(346230050, "spin cleaning pinch")
    prg.add(348230050, "Pulse uw ON", enable=False)
    prg.add(348240050, "B comp x ramp", start_t=0, stop_x=2980, n_points=400, start_x=1369, stop_t=1000, enable=False)
    prg.add(358240050, "B comp x ramp", start_t=0, stop_x=3020, n_points=1000, start_x=2980, stop_t=10000, enable=False)
    prg.add(459240050, "Pulse uw OFF")
    prg.add(459250050, "Dipole Trap y DAC V", -0.1000)
    prg.add(459250450, "Dipole Trap x DAC V", 0.0000)
    prg.add(459255450, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(459255450, "Picture - Field off at 0ms -SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(459255450, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(459255450, "Picture -DipoleLoad-SternGerlach_Levit 10ms.sub", enable=False)
    prg.add(459255450, "Picture - Field off at 0ms -SternGerlach_ShortTom.sub", enable=False)
    prg.add(459255450, "Picture - Field off at 0ms -SternGerlach_ShortElena.sub")
    prg.add(459255450, "Picture - Field off at 0ms -SternGerlach_ShortElena_NoRepump.sub", enable=False)
    prg.add(459255450, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(459255450, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(459255450, "Picture - Field off at 0ms - Levit 30ms-SternGerlach.sub", enable=False)
    prg.add(459255450, "Picture - Field off at 0ms - AntiLevit 50ms.sub", enable=False)
    prg.add(459425450, "Picture NaK.sub", enable=False)
    prg.add(471298850, "Bias field initialization")
    prg.add(472049550, "Pulse uw OFF")
    prg.add(480284050, "Set MOT NaK.sub")
    prg.add(480784050, "Dark Spot MOT load.sub")
    prg.add(480884050, "Config MOT.sub")
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
