prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-100000, "RF sweep DAC V", 0.0000, functions=dict(value=lambda x: cmd.get_var('DAC_V')))
    prg.add(0, "RF Sweep Trig ON")
    prg.add(0, "RF Sweep Trig OFF", functions=dict(time=lambda x: cmd.get_var('siglent1_sweep_time')))
    prg.add(100000, "RF sweep DAC V", 0.0000, functions=dict(time=lambda x: x+ cmd.get_var('siglent1_sweep_time')))
    return prg
