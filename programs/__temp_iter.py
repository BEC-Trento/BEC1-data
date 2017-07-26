prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(197000000, "Shutter Probe Na Open")
    prg.add(200001650, "Config Field OFF.sub")
    prg.add(200001800, "MOT lights Off close.sub")
    prg.add(200072516, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(208897500, "Set MOT NaK.sub")
    prg.add(209397500, "Dark Spot MOT load.sub")
    prg.add(209497500, "Config MOT.sub")
    return prg
