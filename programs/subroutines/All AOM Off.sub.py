prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Repumper1 (+) Amp", 0)
    prg.add(400, "Na Repumper2 (+) Amp", 0)
    prg.add(800, "TTL Dark Spot OFF")
    prg.add(1600, "Na Zeeman slower (-) Amp", 0)
    prg.add(2000, "Na Probe/Push (-) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('push_amp'), funct_enable=False))
    prg.add(2400, "Na Probe/Push (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('push_amp'), funct_enable=False))
    prg.add(2800, "Na Probe/Push (+) OFF")
    prg.add(3200, "Na 3D MOT cool (-) Amp", 0)
    prg.add(3600, "Na 3D MOT cool (+) Amp", 0)
    prg.add(4000, "Na 2D MOT (+) Amp", 0)
    prg.add(4400, "Na 2D MOT (-) Amp", 0)
    return prg
