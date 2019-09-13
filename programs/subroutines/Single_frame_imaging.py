prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2600, "TTL Repumper MOT ON", enable=False)
    prg.add(-2600, "TTL Repumper MOT OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('Rep_pulsetime')), enable=False)
    prg.add(-1500, "Trig ON Stingray 1")
    prg.add(-500, "Trig OFF Stingray 1")
    prg.add(0, "Na Probe/Push (+) ON")
    prg.add(0, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + cmd.get_var('probe_pulsetime')*1e-3))
    return prg
