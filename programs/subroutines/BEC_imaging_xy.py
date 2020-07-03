prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-310, "Repumper AOM TTL")
    prg.add(-310, "Pulse uw ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime')), enable=False)
    prg.add(-310, "Pulse uw OFF", enable=False)
    prg.add(-300, "Pulse Trig Stingray x", comment="atoms", polarity=1, pulse_t=0.10760)
    prg.add(-250, "Pulse Trig Stingray 1", comment="atoms", polarity=1, pulse_t=0.15740)
    prg.add(0, "Probe y AOM TTL")
    prg.add(999910, "Pulse Trig Stingray x", comment="probe", polarity=1, pulse_t=0.13650)
    prg.add(999960, "Pulse Trig Stingray 1", comment="probe", polarity=1, pulse_t=0.17600)
    prg.add(1100210, "Probe y AOM TTL")
    prg.add(1248633, "Shutter Probe/Push Close", enable=False)
    prg.add(1964663, "Pulse Trig Stingray x", comment="dark", polarity=1, pulse_t=0.10000)
    prg.add(1965133, "Pulse Trig Stingray 1", comment="dark", polarity=1, pulse_t=0.10000)
    return prg
