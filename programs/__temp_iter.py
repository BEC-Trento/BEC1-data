prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(4100000, "Synchronize.sub")
    prg.add(9000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(9000490, "Pulse TTL2-12", polarity=1, pulse_t=0.56900, enable=False)
    prg.add(12000000, "B comp x", 775.0)
    prg.add(27000000, "Evaporation Ramp.sub")
    prg.add(464003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(464010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(626010000, "empty.sub", enable=False)
    prg.add(631009060, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(631009990, "Config Field OFF.sub", enable=False)
    prg.add(631009990, "Picture FastStingray", enable=False)
    prg.add(631009990, "Picture FastStingray uw rep extra probe pic", enable=False)
    prg.add(631209990, "Config Field OFF.sub", enable=False)
    prg.add(631212370, "Picture Levit 2017 - setup")
    prg.add(631214470, "Delta 1 Current", 13.200)
    prg.add(631704470, "Config Field OFF.sub")
    prg.add(631714470, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(631714500, "Picture FastStingray")
    prg.add(647454925, "Set MOT NaK.sub")
    prg.add(647954925, "Dark Spot MOT load.sub")
    prg.add(648054925, "Config MOT.sub")
    return prg
