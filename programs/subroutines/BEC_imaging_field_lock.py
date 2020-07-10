prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-701680, "Pulse Trig Stingray 1", comment="field_lock", polarity=1, pulse_t=0.10000)
    prg.add(-12320, "Pulse uw ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(-12320, "Pulse uw OFF")
    prg.add(-12000, "Probe y AOM TTL")
    prg.add(-1000, "Pulse Trig Stingray 1", comment="atoms", polarity=1, pulse_t=0.10540)
    prg.add(-310, "Repumper AOM TTL")
    prg.add(0, "Probe y AOM TTL")
    prg.add(4, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.00564, enable=False)
    prg.add(999916, "Pulse Trig Stingray 1", comment="probe", polarity=1, pulse_t=0.14400)
    prg.add(1001416, "Probe y AOM TTL")
    prg.add(1804381, "Shutter Probe/Push Close")
    prg.add(2016036, "Pulse Trig Stingray 1", comment="dark", polarity=1, pulse_t=0.10000)
    return prg
