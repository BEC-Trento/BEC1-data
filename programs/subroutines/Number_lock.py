prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-20000, "Pulse uw", polarity=1, pulse_t=0.00700, enable=False)
    prg.add(-5000, "Setup_microwave_imaging")
    prg.add(-5000, "Setup_imaging", enable=False)
    prg.add(-2500, "Na Repumper1 (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')), enable=False)
    prg.add(-2000, "Na Repumper2 (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')), enable=False)
    prg.add(-310, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(-310, "TTL Repumper MOT ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('Rep_pulsetime')), enable=False)
    prg.add(-310, "TTL Repumper MOT OFF", enable=False)
    prg.add(-300, "Trig ON Stingray 1", 'nlock')
    prg.add(-10, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, enable=False)
    prg.add(0, "TTL Probe y ON")
    prg.add(0, "TTL Probe y OFF", functions=dict(time=lambda x: x + cmd.get_var('probe_pulsetime')*1e-3))
    prg.add(700, "Trig OFF Stingray 1")
    prg.add(10000, "Imaging_lights_off.sub")
    return prg
