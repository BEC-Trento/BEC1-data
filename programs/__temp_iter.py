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
    prg.add(32095990, "TTL2-12 OFF")
    prg.add(32096000, "Config Field OFF.sub")
    prg.add(32100000, "MOT lights Off TTL short.sub")
    prg.add(32101700, "TTL2-12 ON")
    prg.add(32101750, "TTL2-12 OFF")
    prg.add(32101800, "GrayMolassesPulse", enable=False)
    prg.add(32101800, "GM pulse", enable=False)
    prg.add(32101900, "Gray Molasses 2017", enable=False)
    prg.add(32176900, "mot imaging subroutine atoms probe bg", functions=dict(time=lambda x: 2212.5000+cmd.get_var('tof'), funct_enable=False))
    prg.add(39136600, "Set MOT NaK.sub")
    prg.add(39636600, "Dark Spot MOT load.sub")
    prg.add(39736600, "Config MOT.sub")
    prg.add(41031600, "Shutter Probe Na Open", enable=False)
    return prg
