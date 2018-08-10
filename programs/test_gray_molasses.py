prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1510000, "Set MOT NaK.sub")
    prg.add(2010000, "Dark Spot MOT load.sub")
    prg.add(2110000, "Config MOT.sub")
    prg.add(2120000, "B comp x", 710.0, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False), enable=False)
    prg.add(2120100, "Bcomp y Sign Minus", enable=False)
    prg.add(2130000, "B comp y", 0.0700, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False), enable=False)
    prg.add(2140000, "B comp z", 1.0050, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False), enable=False)
    prg.add(32140000, "Synchronize.sub", enable=False)
    prg.add(39500000, "Shutter Probe Na Open")
    prg.add(42291500, "Config Field OFF.sub")
    prg.add(42291555, "MOT lights Off close.sub", enable=False)
    prg.add(42291555, "Melassa Na.sub", enable=False)
    prg.add(42291555, "Melassa Na amp.sub", enable=False)
    prg.add(42291555, "TTL2-12 ON")
    prg.add(42291605, "MOT lights Off close.sub")
    prg.add(42293840, "Gray Molasses Pulse 2017", enable=False)
    prg.add(42293840, "Gray Molasses 2017")
    prg.add(62293840, "empty.sub", enable=False)
    prg.add(62418865, "startup.prg")
    return prg
