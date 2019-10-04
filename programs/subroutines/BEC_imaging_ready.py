prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-310, "TTL Repumper MOT ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('Rep_pulsetime')))
    prg.add(-310, "TTL Repumper MOT OFF")
    prg.add(-300, "Trig ON Stingray 1")
    prg.add(-10, "Scope 1 Trigger ON", enable=False)
    prg.add(0, "Na Probe/Push (+) ON")
    prg.add(0, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + cmd.get_var('probe_pulsetime')*1e-3))
    prg.add(700, "Trig OFF Stingray 1")
    prg.add(990, "Scope 1 Trigger OFF", enable=False)
    prg.add(999910, "Trig ON Stingray 1")
    prg.add(1000910, "Trig OFF Stingray 1")
    prg.add(1001410, "Na Probe/Push (+) ON")
    prg.add(1001410, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + cmd.get_var('probe_pulsetime')*1e-3))
    prg.add(1001914, "Shutter Probe Na Close")
    prg.add(2016010, "Trig ON Stingray 1")
    prg.add(2017010, "Trig OFF Stingray 1")
    prg.add(3816010, "Na Probe/Push (+) ON")
    return prg
