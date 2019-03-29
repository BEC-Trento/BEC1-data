prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "RFO SetImaging+Ref")
    prg.add(900000, "RFO ImagingQuantum")
    prg.add(1200000, "RFO ImagingQuantum", enable=False)
    prg.add(2200000, "RFO ImagingQuantumNoProbe")
    prg.add(3200000, "RFO ImagingQuantumNoProbe")
    return prg
