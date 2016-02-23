prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "uniform B field x Rele IGBT config")
    prg.add(1500000, "Decompress Current 200-50", start_t=0.0000, stop_x=108.000, n_points=300, start_x=0.000, stop_t=250.0000)
    prg.add(4100000, "Decompress Current 200-50", start_t=0.0000, stop_x=109.000, n_points=300, start_x=108.000, stop_t=25.0000)
    prg.add(4101000, "RF mag sweep 0 level")
    prg.add(4450000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=109.000, stop_t=250.0000)
    return prg
