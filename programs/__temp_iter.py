prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1489000, "Trigger LZ OFF")
    prg.add(1490000, "Trigger LZ ON")
    prg.add(1491000, "Trigger LZ OFF")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(22096000, "Config Field OFF.sub")
    prg.add(22100000, "MOT lights Off TTL short.sub")
    prg.add(22102000, "TTL2-12 OFF")
    prg.add(22103000, "TTL2-12 ON")
    prg.add(22104989, "TTL2-12 OFF")
    prg.add(22105000, "Gray Molasses 29-03-2019")
    prg.add(22158000, "empty.sub", enable=False)
    prg.add(22206000, "mot imaging subroutine atoms probe bg", functions=dict(time=lambda x: 2210.7000+cmd.get_var('tof')), enable=False)
    prg.add(27163000, "Set MOT NaK.sub", enable=False)
    prg.add(27663000, "Dark Spot MOT load.sub", enable=False)
    prg.add(27763000, "Config MOT.sub", enable=False)
    prg.add(29058000, "Shutter Probe Na Open", enable=False)
    return prg
