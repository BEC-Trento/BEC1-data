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
    prg.add(22095990, "TTL2-12 OFF")
    prg.add(22096000, "Config Field OFF.sub")
    prg.add(22096100, "TTL2-12 ON")
    prg.add(22100000, "MOT lights Off TTL short.sub")
    prg.add(22100010, "TTL2-12 OFF")
    prg.add(22101720, "GM pulse")
    prg.add(22187700, "mot imaging subroutine atoms probe bg", functions=dict(time=lambda x: 2210.7000+cmd.get_var('tof'), funct_enable=False))
    prg.add(22227800, "TTL2-12 ON", enable=False)
    prg.add(27184700, "Set MOT NaK.sub")
    prg.add(27684700, "Dark Spot MOT load.sub")
    prg.add(27784700, "Config MOT.sub")
    prg.add(29079700, "Shutter Probe Na Open", enable=False)
    return prg
