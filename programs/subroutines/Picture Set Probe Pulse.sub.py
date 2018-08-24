prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Pulse Probe Na", polarity=1, pulse_t=0.10000)
    return prg
