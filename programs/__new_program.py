prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(49000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000)
    prg.add(54000, "RF Sweep Trig ON")
    prg.add(154000, "RF Sweep Trig OFF")
    prg.add(155000, "RF Sweep Trig ON")
    prg.add(655000, "RF Sweep Trig OFF")
    return prg
