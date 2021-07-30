prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "B grad x ramp", start_t=0, stop_x=0.28, n_points=50, start_x=0.2, stop_t=1)
    prg.add(100, "B comp x ramp", start_t=0.2, stop_x=0, n_points=50, start_x=0, stop_t=1, functions=dict(start_x=lambda x: cmd.get_var('Bx_dipole_trap'), stop_x=lambda x: cmd.get_var('Bx_grad_comp')))
    prg.add(200, "B grad x ramp", start_t=0, stop_x=0, n_points=50, start_x=0.28, stop_t=1, functions=dict(stop_x=lambda x: cmd.get_var('Bx_grad_mix'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+18))
    return prg
