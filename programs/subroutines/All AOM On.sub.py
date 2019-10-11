prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Repumper1 (+) Amp", 1000)
    prg.add(400, "Na Repumper2 (+) Amp", 1000)
    prg.add(800, "TTL Dark Spot ON")
    prg.add(1200, "TTL Repumper MOT ON", enable=False)
    prg.add(1300, "Na Zeeman slower (-) Amp", 1000)
    prg.add(1500, "Na Probe/Push (-) freq", 60.00)
    prg.add(2000, "Na Push (+) freq", 60.00)
    prg.add(2500, "Na Probe y (+) freq", 60.00)
    prg.add(3000, "Na Probe z (+) freq", 60.00)
    prg.add(3050, "TTL Push ON")
    prg.add(3100, "TTL Probe y ON")
    prg.add(3150, "TTL Probe z ON")
    prg.add(3200, "Na 3D MOT cool (-) Amp", 1000)
    prg.add(3600, "Na 3D MOT cool (+) Amp", 1000)
    prg.add(4000, "Na 2D MOT (+) Amp", 1000)
    prg.add(4400, "Na 2D MOT (-) Amp", 1000)
    prg.add(5000, "Na Probe/Push (-) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(5500, "Na Push (+) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('push_amp')))
    prg.add(6000, "Na Probe y (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(6500, "Na Probe z (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    return prg
