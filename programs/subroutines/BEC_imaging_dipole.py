prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-702680, "Pulse Trig Stingray 1", comment="F1", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(-3100, "Pulse uw with RF", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime_m1')), enable=False)
    prg.add(-1500, "Pulse Trig Stingray 1", comment="atoms", polarity=1, pulse_t=0.10540)
    prg.add(-310, "Pulse Probe y", polarity=1, pulse_t=0.10000, functions=dict(pulse_t=lambda x: cmd.get_var('probe_pulsetime')*1e-3), enable=False)
    prg.add(-310, "Repumper AOM TTL")
    prg.add(0, "Probe y AOM TTL")
    prg.add(0, "TTL Probe y ON", enable=False)
    prg.add(4, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.10564, enable=False)
    prg.add(699916, "Pulse Trig Stingray 1", comment="probe", polarity=1, pulse_t=0.14400)
    prg.add(701416, "Probe y AOM TTL")
    prg.add(1804381, "Shutter Probe/Push Close")
    prg.add(2016036, "Pulse Trig Stingray 1", comment="dark", polarity=1, pulse_t=0.10000)
    return prg
