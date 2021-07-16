prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1001, "IGBT B grad x OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')+1.115))
    prg.add(-1001, "B grad comp OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')+1.7))
    prg.add(0, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')+cmd.get_var('tof2')-cmd.get_var('t_cfo')+1))
    prg.add(0, "Config Levitation dipole", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')+1))
    prg.add(0, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('tof2')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')+1))
    return prg


