prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5013000, "Shutter repump Na Open")
    prg.add(-5000000, "TTL Repumper MOT OFF")
    prg.add(-4403000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4363000, "Na Dark Spot Amp", 1)
    prg.add(-4353000, "Na Repumper MOT Amp", 1)
    prg.add(-4003000, "Shutter Probe Na Open")
    prg.add(-3990000, "Na Probe/Push (+) OFF")
    prg.add(-3980000, "Na Probe/Push (-) Amp", 1)
    prg.add(-3970000, "Na Probe/Push (+) Amp", 1)
    prg.add(-3011000, "IGBT B comp y OFF", enable=False)
    prg.add(-3000000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2990000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-2980000, "Shutter 3DMOT cool Na Open")
    prg.add(-1000500, "Pulse Trig Extra Hamamatsu", polarity=1, pulse_t=0.10000)
    prg.add(-201000, "B comp y", 0.0500, enable=False)
    prg.add(-199500, "Na Repumper Tune (+) freq", 1713.0)
    prg.add(-199000, "Na Repumper1 (+) Amp", 1000)
    prg.add(-101000, "Na Probe/Push (+) Amp", 1000)
    prg.add(-100500, "Na Probe/Push (-) Amp", 1000)
    prg.add(-91199, "Na Probe/Push (+) freq", 110.00, functions=dict(frequency=lambda x: x + cmd.get_var('probe_det')/2.0))
    prg.add(-90800, "Na Probe/Push (-) freq", 110.00, functions=dict(frequency=lambda x: x - cmd.get_var('probe_det')/2.0))
    prg.add(-39954, "IGBT B comp y ON", enable=False)
    prg.add(-7650, "IGBT B comp x OFF")
    prg.add(-2600, "TTL Repumper MOT ON")
    prg.add(-1000, "Trig ON Stingray 1")
    prg.add(-100, "TTL Repumper MOT OFF")
    prg.add(0, "Pulse Probe Na", polarity=1, pulse_t=0.10000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('probe_tau')))
    prg.add(2100, "Trig OFF Stingray 1")
    prg.add(999000, "Trig ON Stingray 1")
    prg.add(1000000, "Pulse Probe Na", polarity=1, pulse_t=0.10000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('probe_tau')))
    prg.add(1002099, "Trig OFF Stingray 1")
    prg.add(1010000, "Shutter Probe Na Close")
    prg.add(1020000, "Na Repumper1 (+) Amp", 1)
    prg.add(2019000, "Trig ON Stingray 1")
    prg.add(2022100, "Trig OFF Stingray 1")
    prg.add(3019000, "Trig ON Stingray 1")
    prg.add(3022100, "Trig OFF Stingray 1")
    prg.add(4020000, "B comp y", 0.0000, enable=False)
    prg.add(4030000, "IGBT B comp y OFF")
    return prg
