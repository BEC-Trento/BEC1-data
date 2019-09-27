prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-500000, "Green Light AOM amp", 0)
    prg.add(-310, "TTL Repumper MOT ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('Rep_pulsetime')))
    prg.add(-310, "TTL Repumper MOT OFF")
    prg.add(-200, "Trig ON Stingray 1")
    prg.add(-10, "Scope 1 Trigger ON")
    prg.add(0, "Na Probe/Push (+) ON", enable=False)
    prg.add(0, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + cmd.get_var('probe_pulsetime')*1e-3), enable=False)
    prg.add(0, "Setup_imaging")
    prg.add(20, "Green Light AOM amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('DMD_amp')))
    prg.add(20, "Green Light AOM amp", 0, functions=dict(time=lambda x: x + 1e-3*cmd.get_var('DMD_pulsetime')))
    prg.add(700, "Trig OFF Stingray 1")
    prg.add(990, "Scope 1 Trigger OFF")
    prg.add(999910, "Trig ON Stingray 1", enable=False)
    prg.add(1000910, "Trig OFF Stingray 1", enable=False)
    prg.add(1001110, "Scope 2 Trigger OFF", enable=False)
    prg.add(1001210, "Scope 2 Trigger ON", enable=False)
    prg.add(1001310, "Scope 2 Trigger OFF", enable=False)
    prg.add(1001410, "Na Probe/Push (+) ON", enable=False)
    prg.add(1001410, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + cmd.get_var('probe_pulsetime')*1e-3), enable=False)
    prg.add(1001900, "Scope 1 Trigger OFF")
    prg.add(1001914, "Shutter Probe Na Close")
    prg.add(2016010, "Trig ON Stingray 1")
    prg.add(2017010, "Trig OFF Stingray 1")
    prg.add(3816010, "Na Probe/Push (+) ON")
    prg.add(4000000, "Green Light AOM amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('DMD_amp')))
    return prg