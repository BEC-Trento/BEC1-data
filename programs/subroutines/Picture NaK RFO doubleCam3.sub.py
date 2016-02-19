prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "RFO SetImaging+Ref3")
    prg.add(900000, "RFO ImagingQuantum3 Ramp", start_t=0.0000, stop_x=0.000, n_points=26, start_x=1.000, stop_t=600.0000)
    return prg
