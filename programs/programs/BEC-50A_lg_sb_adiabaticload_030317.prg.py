prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize Experiment.sub")
    prg.add(10, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(11000, "TTL3-11 ON")
    prg.add(20000, "Bx Grad ON", enable=False)
    prg.add(48420, "Optical Levit (-) Amp", 1000)
    prg.add(98420, "B comp y", 0.0000)
    prg.add(108420, "IGBT B comp y ON")
    prg.add(498420, "Bcomp y Sign Plus", enable=False)
    prg.add(1498420, "Set MOT NaK.sub")
    prg.add(1998420, "Dark Spot MOT load.sub")
    prg.add(2098420, "Config MOT.sub")
    prg.add(9998420, "Optical Levit ON")
    prg.add(10998420, "Synchronize.sub")
    prg.add(11098420, "Melassa Na.sub")
    prg.add(11099420, "Melassa Na amp.sub")
    prg.add(11099920, "Config Field OFF.sub")
    prg.add(11147920, "MOT lights Off.sub")
    prg.add(11151920, "Delta 1 Current", 200.000)
    prg.add(11151930, "Delta 2 Voltage", 30.0000)
    prg.add(11151940, "Config MT compr.sub")
    prg.add(13155960, "All Shutter Close.sub")
    prg.add(16157960, "Mirrors Imaging")
    prg.add(16657960, "IGBT B comp x ON")
    prg.add(17157960, "All AOM On.sub")
    prg.add(20157960, "B comp x", 995.0)
    prg.add(21099500, "Evaporation Ramp.sub")
    prg.add(458102500, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(458109500, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(545380000, "Dipole Trap x ramp", start_t=0.0000, stop_x=3.000, n_points=100, start_x=0.000, stop_t=200.0000)
    prg.add(565390000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=100, start_x=50.000, stop_t=200.0000)
    prg.add(565390000, "Config Field OFF.sub", enable=False)
    prg.add(566390000, "Dipole Trap x ramp", start_t=0.0000, stop_x=0.100, n_points=100, start_x=3.000, stop_t=1000.0000)
    prg.add(576890000, "Dipole Trap x DAC V", 0.0000)
    prg.add(576970000, "Picture NaK.sub")
    prg.add(579550000, "Dipole Trap x DAC V", 0.0000, enable=False)
    prg.add(586970000, "Set MOT NaK.sub")
    prg.add(587470000, "Dark Spot MOT load.sub")
    prg.add(587485000, "Bx Grad OFF")
    prg.add(587570000, "Config MOT.sub")
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
