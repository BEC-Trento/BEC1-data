prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(19951500, "Melassa Na amp.sub")
    prg.add(19952000, "Config Field OFF.sub")
    prg.add(20000000, "MOT lights Off.sub")
    prg.add(20004000, "Delta 1 Current", 200.000)
    prg.add(20004010, "Delta 2 Voltage", 30.0000)
    prg.add(20004020, "Config MT compr.sub")
    prg.add(22008040, "All Shutter Close.sub")
    prg.add(25010040, "Mirrors Imaging")
    prg.add(25510040, "IGBT B comp x ON")
    prg.add(26010040, "All AOM On.sub")
    prg.add(29010040, "B comp x", 277.0)
    prg.add(30000000, "Evaporation Ramp.sub", enable=False)
    prg.add(30010000, "Dipole Trap x DAC V", 0.1000)
    prg.add(30017000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000, enable=False)
    prg.add(48017000, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(48017000, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(106447000, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(106447000, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
    prg.add(106447000, "Config Field OFF.sub", enable=False)
    prg.add(106447000, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(106457000, "Picture NaK.sub")
    prg.add(121057000, "Set MOT NaK.sub")
    prg.add(121557000, "Dark Spot MOT load.sub")
    prg.add(121657000, "Config MOT.sub")
    prg.add(123007000, "Dipole Trap x DAC V", 0.0000)
    return prg
def commands(cmd):
    a=[4,5,6]
    cmd.set_var("hhh", 4)
    while(cmd.running):
        a.pop()
        if len(a) == 0:
         cmd.stop()
    return prg
