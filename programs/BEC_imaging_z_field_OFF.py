prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')))
    prg.add(3000000, "B grad comp OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')))
    prg.add(3030000, "IGBT B grad x OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')))
    return prg
