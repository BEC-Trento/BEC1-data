prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3011000, "IGBT B comp y OFF", enable=False)
    prg.add(-1000500, "Pulse Trig Extra Hamamatsu", polarity=1, pulse_t=0.10000)
    prg.add(-201000, "B comp y", 0.0500, enable=False)
    prg.add(-40000, "IGBT B comp y ON", enable=False)
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(0, "Pulse Probe Na", polarity=1, pulse_t=0.01000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('probe_tau')))
    prg.add(1050, "Trig OFF Stingray 1")
    prg.add(199500, "Trig ON Stingray 1")
    prg.add(200000, "Pulse Probe Na", polarity=1, pulse_t=0.01000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('probe_tau')))
    prg.add(201050, "Trig OFF Stingray 1")
    prg.add(399500, "Trig ON Stingray 1")
    prg.add(401050, "Trig OFF Stingray 1")
    prg.add(599500, "Trig ON Stingray 1")
    prg.add(601050, "Trig OFF Stingray 1")
    prg.add(1599550, "B comp y", 0.0000, enable=False)
    prg.add(1609550, "IGBT B comp y OFF", enable=False)
    return prg
