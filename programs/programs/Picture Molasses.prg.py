prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(57550000, "Shutter Probe Na Open")
    prg.add(59950560, "Compress MOT Na", enable=False)
    prg.add(60150560, "Config Field OFF.sub")
    prg.add(60151560, "TTL2-12 ON")
    prg.add(60153560, "Melassa Na.sub")
    prg.add(60154560, "Melassa Na amp.sub")
    prg.add(60209560, "MOT lights Off close.sub")
    prg.add(60511127, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(60511127, "Picture close no repump.sub", enable=False)
    prg.add(68511127, "TTL2-12 OFF")
    prg.add(68611127, "Set MOT NaK.sub")
    prg.add(69111127, "Dark Spot MOT load.sub")
    prg.add(69211127, "Config MOT.sub")
    return prg
