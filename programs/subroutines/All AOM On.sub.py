prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Repumper1 (+) Amp", 1000)
    prg.add(400, "Na Repumper2 (+) Amp", 1000)
    prg.add(800, "TTL Dark Spot ON")
    prg.add(1200, "TTL Repumper MOT ON", enable=False)
    prg.add(1600, "Na Zeeman slower (-) Amp", 1000)
    prg.add(2000, "Na Probe/Push (-) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('push_amp')))
    prg.add(2400, "Na Probe/Push (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('push_amp')))
    prg.add(2800, "Na Probe/Push (+) ON")
    prg.add(3200, "Na 3D MOT cool (-) Amp", 1000)
    prg.add(3600, "Na 3D MOT cool (+) Amp", 1000)
    prg.add(4000, "Na 2D MOT (+) Amp", 1000)
    prg.add(4400, "Na 2D MOT (-) Amp", 1000)
    return prg
