prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4000000, "Shutter 3DMOT cool Na Close")
    prg.add(-3900000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-3850000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2600000, "Shutter repump Na Open")
    prg.add(-2550000, "Shutter Repump2 Open")
    prg.add(-2530000, "TTL Dark Spot OFF")
    prg.add(-2520000, "TTL Repumper MOT OFF")
    prg.add(-2500, "Na Repumper1 (+) Amp", 1000)
    prg.add(-2000, "Na Repumper2 (+) Amp", 1000)
    prg.add(-1600, "Na Repumper Tune (+) freq", 1713.0, functions=dict(frequency=lambda x: x + cmd.get_var('freq'), funct_enable=False))
    prg.add(-1000, "TTL Repumper MOT ON", enable=False)
    return prg
