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
    prg.add(10010000, "Dipole Trap x DAC V", 5.0000)
    prg.add(10020000, "Dipole Trap y DAC V", 5.0000)
    prg.add(119950500, "Melassa Na.sub")
    prg.add(119951500, "Melassa Na amp.sub")
    prg.add(119952000, "Config Field OFF.sub")
    prg.add(120000000, "MOT lights Off.sub")
    prg.add(120010000, "Mirrors Imaging")
    prg.add(122210000, "Picture NaK.sub")
    prg.add(126210000, "Dipole Trap x DAC V", 0.0000)
    prg.add(126220000, "Dipole Trap y DAC V", 0.0000)
    prg.add(131210000, "Set MOT NaK.sub")
    prg.add(131710000, "Dark Spot MOT load.sub")
    prg.add(131810000, "Config MOT.sub")
    return prg
def commands(cmd):
    a=[4,5,6]
    cmd.set_var("hhh", 4)
    while(cmd.running):
        a.pop()
        if len(a) == 0:
         cmd.stop()
    return cmd
