prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(2110000, "B comp x", 850.0, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False))
    prg.add(2120000, "B comp y", 0.0000, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False))
    prg.add(2130000, "Analog71", 0.3500, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False))
    prg.add(192130000, "Synchronize.sub", enable=False)
    prg.add(199680000, "Shutter Probe Na Open")
    prg.add(202281500, "Config Field OFF.sub")
    prg.add(202282105, "TTL2-12 ON")
    prg.add(202282155, "MOT lights Off close.sub")
    prg.add(202282155, "empty.sub", enable=False)
    prg.add(202324010, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(211124330, "TTL2-12 OFF")
    prg.add(211231510, "Set MOT NaK.sub")
    prg.add(211731510, "Dark Spot MOT load.sub")
    prg.add(211831510, "Config MOT.sub")
    return prg
