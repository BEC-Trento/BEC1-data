prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3000, "TTL Probe y OFF")
    prg.add(-1000, "TTL Repumper MOT OFF")
    prg.add(0, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_det')/2))
    prg.add(500, "Na Probe y (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    return prg
