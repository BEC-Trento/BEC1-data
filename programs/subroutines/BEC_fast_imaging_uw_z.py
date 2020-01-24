prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-500, "Probe z AOM TTL", functions=dict(time=lambda x: x - cmd.get_var('probe_z_pulsetime')*1e-3))
    prg.add(-100, "Trig ON Stingray z", 'F1', functions=dict(time=lambda x: x - cmd.get_var('cam4_ExposureTime')*1e-3))
    prg.add(400, "Trig OFF Stingray z", functions=dict(time=lambda x: x - cmd.get_var('cam4_ExposureTime')*1e-3))
    prg.add(534, "Trig ON Stingray z", 'atoms')
    prg.add(900, "Pulse uw ON", functions=dict(time=lambda x: x - cmd.get_var('marconi1_pulsetime')*1e-3))
    prg.add(900, "Pulse uw OFF")
    prg.add(1000, "Probe z AOM TTL")
    prg.add(1400, "Trig OFF Stingray z")
    prg.add(50000, "Trig ON Stingray z", 'probe', functions=dict(time=lambda x: x+ cmd.get_var('cam4_ExposureTime')*1e-3))
    prg.add(51390, "Trig OFF Stingray z", functions=dict(time=lambda x: x + cmd.get_var('cam4_ExposureTime')*1e-3))
    prg.add(51490, "Probe z AOM TTL", functions=dict(time=lambda x: x + cmd.get_var('cam4_ExposureTime')*1e-3))
    prg.add(150290, "Trig ON Stingray z", 'dark', functions=dict(time=lambda x: x+ 2*cmd.get_var('cam4_ExposureTime')*1e-3))
    prg.add(151290, "Trig OFF Stingray z", functions=dict(time=lambda x: x + 2*cmd.get_var('cam4_ExposureTime')*1e-3))
    return prg
