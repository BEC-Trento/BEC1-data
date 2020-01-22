prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1500, "Na Repumper2 (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(-1000, "Na Repumper1 (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(-310, "TTL Repumper MOT ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('Rep_pulsetime')))
    prg.add(-310, "TTL Repumper MOT OFF")
    prg.add(-310, "Pulse uw ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime')), enable=False)
    prg.add(-310, "Pulse uw OFF", enable=False)
    prg.add(-300, "Pulse Trig Stingray 1", comment="atoms", polarity=1, pulse_t=0.10000)
    prg.add(-250, "Pulse Trig Stingray z", comment="atoms", polarity=1, pulse_t=0.10000)
    prg.add(-134, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.00740, enable=False)
    prg.add(0, "Pulse Probe z", polarity=1, pulse_t=0.10000, functions=dict(pulse_t=lambda x: cmd.get_var('probe_pulsetime')*1e-3))
    prg.add(134, "Pulse Probe y", polarity=1, pulse_t=0.00000, functions=dict(pulse_t=lambda x: cmd.get_var('probe_pulsetime')*1e-3))
    prg.add(999910, "Pulse Trig Stingray 1", comment="probe", polarity=1, pulse_t=0.10000)
    prg.add(1000000, "Pulse Trig Stingray z", comment="probe", polarity=1, pulse_t=0.10000)
    prg.add(1001410, "Pulse Probe z", polarity=1, pulse_t=0.08700, functions=dict(pulse_t=lambda x: cmd.get_var('probe_pulsetime')*1e-3))
    prg.add(1001500, "Pulse Probe y", polarity=1, pulse_t=0.10000, functions=dict(pulse_t=lambda x: cmd.get_var('probe_pulsetime')*1e-3))
    prg.add(1010000, "Pulse Repumper MOT", polarity=1, pulse_t=0.10000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('Rep_pulsetime')), enable=False)
    prg.add(1251934, "Shutter Probe/Push Close")
    prg.add(1300000, "Shutter repump Na Close")
    prg.add(2016030, "Pulse Trig Stingray 1", comment="dark", polarity=1, pulse_t=0.10000)
    prg.add(2016500, "Pulse Trig Stingray z", comment="dark", polarity=1, pulse_t=0.10000)
    return prg
