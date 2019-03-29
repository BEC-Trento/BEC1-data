prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-9600, "B comp x ramp", start_t=0, stop_x=2000, n_points=20, start_x=1000, stop_t=1, enable=False)
    prg.add(-9500, "B comp y ramp", start_t=0, stop_x=5, n_points=20, start_x=0, stop_t=1, enable=False)
    prg.add(0, "IGBT 1 pinch", 10.0000)
    prg.add(10, "IGBT 4 Close")
    prg.add(20, "Delta 1 Voltage", 5.0000)
    prg.add(2000, "Config Levitation zero current.sub")
    prg.add(2100, "Delta 1 Current", 13.850)
    prg.add(5500, "B comp y ramp", start_t=0, stop_x=0, n_points=20, start_x=5, stop_t=1, enable=False)
    prg.add(5600, "B comp x ramp", start_t=0, stop_x=1369, n_points=20, start_x=2000, stop_t=1, enable=False)
    prg.add(640000, "Config Field OFF.sub")
    prg.add(650000, "Picture NaK for Levit 2017.sub")
    prg.add(4652000, "B comp y", 0.0000)
    return prg
