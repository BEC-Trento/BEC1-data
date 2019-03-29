prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "GM ON")
    prg.add(5000, "AOM GM Detuning", 120.000, enable=False)
    prg.add(5000, "AOM GM Amp ch1 (+)", 1)
    prg.add(5500, "AOM GM Amp ch2 (-)", 1)
    prg.add(6000, "AOM GM Amp ch2 (-)", 1000, enable=False)
    prg.add(7500, "GM amp(+) ramp", start_t=0, stop_x=750, n_points=15, start_x=1000, stop_t=1, enable=False)
    prg.add(18000, "GM amp(+) ramp", start_t=0, stop_x=200, n_points=30, start_x=750, stop_t=3, enable=False)
    prg.add(38000, "GM amp(+) ramp", start_t=0, stop_x=200, n_points=10, start_x=350, stop_t=1, enable=False)
    prg.add(48050, "TTL Repumper GM OFF", enable=False)
    prg.add(48500, "AOM GM Detuning", 40.000, enable=False)
    prg.add(49000, "AOM GM Amp ch1 (+)", 1000, enable=False)
    prg.add(53851, "Shutter Gray molasses Close")
    prg.add(10053351, "AOM GM Amp ch1 (+)", 1000)
    prg.add(10063351, "AOM GM Amp ch2 (-)", 1000)
    prg.add(10073351, "TTL Repumper GM ON")
    return prg
