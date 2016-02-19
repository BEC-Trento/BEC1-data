prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(89950500, "Melassa Na.sub")
    prg.add(89951500, "Melassa Na amp.sub")
    prg.add(89952000, "Config Field OFF.sub")
    prg.add(90000000, "MOT lights Off.sub")
    prg.add(90004000, "Delta 1 Current", 200.000)
    prg.add(90004010, "Delta 2 Voltage", 30.0000)
    prg.add(90004020, "Config MT compr.sub")
    prg.add(92008040, "All Shutter Close.sub")
    prg.add(95010040, "Mirrors Imaging")
    prg.add(95510040, "IGBT B comp x ON")
    prg.add(96010040, "All AOM On.sub")
    prg.add(99010040, "B comp x", 302.0)
    prg.add(100000000, "Evaporation Ramp.sub")
    prg.add(100010000, "Dipole Trap y DAC V", 5.0000, enable=False)
    prg.add(100020000, "Dipole Trap x DAC V", 3.0000, enable=False)
    prg.add(537003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(537010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(611790000, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(613440000, "Dipole Trap y ramp", start_t=0.0000, stop_x=5.000, n_points=100, start_x=0.000, stop_t=100.0000)
    prg.add(613450000, "Dipole Trap x ramp", start_t=0.0000, stop_x=5.000, n_points=100, start_x=0.000, stop_t=100.0000, enable=False)
    prg.add(613450000, "Config Field OFF.sub", enable=False)
    prg.add(613460000, "Picture NaK.sub", enable=False)
    prg.add(614450000, "Picture NaK.sub")
    prg.add(614460000, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(614460000, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=500, start_x=50.000, stop_t=500.0000, enable=False)
    prg.add(619460000, "Dipole Trap y DAC V", 0.0000)
    prg.add(619465000, "Dipole Trap x DAC V", 0.0000)
    prg.add(629445000, "Set MOT NaK.sub")
    prg.add(629945000, "Dark Spot MOT load.sub")
    prg.add(630045000, "Config MOT.sub")
    return prg
def commands(cmd):
    a=[4,5,6]
    cmd.set_var("hhh", 4)
    while(cmd.running):
        a.pop()
        if len(a) == 0:
         cmd.stop()
    return cmd
