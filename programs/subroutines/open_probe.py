prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Probe y (+) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(5000, "Na Probe z (+) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_z_amp')))
    prg.add(10000, "Na Probe/Push (-) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_push_amp')))
    prg.add(20000, "Na Probe y (+) freq", 0.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(25000, "Na Probe z (+) freq", 0.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(30000, "Na Probe/Push (-) freq", 0.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_det')/2))
    prg.add(35000, "TTL Probe y ON")
    prg.add(40000, "TTL Probe z ON")
    prg.add(45000, "Mirrors Imaging")
    prg.add(115000, "Shutter Probe/Push Open")
    prg.add(156245, "Shutter repump Na Open")
    prg.add(185000, "Na Repumper1 (+) Amp", 800, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(195000, "Na Repumper2 (+) Amp", 800, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(205000, "TTL Repumper MOT ON")
    return prg
