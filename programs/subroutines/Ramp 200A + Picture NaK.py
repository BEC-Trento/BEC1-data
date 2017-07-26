prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=200.0000)
    prg.add(1000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=200.0000)
    prg.add(2002000, "Config Field OFF.sub")
    prg.add(2010000, "Picture NaK.sub")
    return prg
