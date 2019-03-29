prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT 5 Open")
    prg.add(10, "IGBT 3 Close")
    prg.add(20, "IGBT 4 Close")
    prg.add(40, "Delta 2 Voltage", 0.0000)
    prg.add(1040, "Delta 1 Voltage ramp", start_t=0.0000, stop_x=15.000, n_points=10, start_x=0.000, stop_t=20.0000, enable=False)
    prg.add(1040, "Delta 1 Voltage", 5.0000)
    prg.add(1050, "Delta 1 Current", 10.000)
    prg.add(141050, "IGBT 4 Open")
    prg.add(151050, "Picture NaK.sub", enable=False)
    prg.add(151050, "Picture NaK Ready.sub")
    prg.add(4101994, "B comp y", 0.0000)
    prg.add(4200994, "IGBT B comp y OFF")
    return prg
