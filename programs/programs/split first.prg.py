prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Picture - Ref Film.sub")
    prg.add(300000, "Pulsed uw.sub")
    prg.add(430000, "Picture - Frame Film.sub")
    prg.add(1210000, "Pulsed uw.sub")
    prg.add(1340000, "Picture - Frame Film.sub")
    prg.add(2050000, "Pulsed uw.sub")
    prg.add(2180000, "Picture - Frame Film.sub")
    prg.add(2890000, "Pulsed uw.sub")
    prg.add(3020000, "Picture - Frame Film.sub")
    prg.add(3730000, "Pulsed uw.sub")
    prg.add(3860000, "Picture - Frame Film.sub")
    prg.add(4570000, "Pulsed uw.sub")
    prg.add(4700000, "Picture - Frame Film.sub")
    prg.add(5410000, "Pulsed uw.sub")
    prg.add(5540000, "Picture - Frame Film.sub")
    prg.add(6250000, "Pulsed uw.sub")
    prg.add(6380000, "Picture - Frame Film.sub")
    return prg
