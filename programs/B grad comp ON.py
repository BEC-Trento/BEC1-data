prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-130, "B comp x ramp", start_t=0.2, stop_x=0, n_points=50, start_x=0, stop_t=1, functions=dict(stop_t=lambda x: cmd.get_var('grad_ramp_time'), stop_x=lambda x: cmd.get_var('Bx_grad_comp'), start_x=lambda x: cmd.get_var('Bx_dipole_trap')))
    prg.add(-1, "B grad x ramp", start_t=0, stop_x=0, n_points=50, start_x=0.0, stop_t=1, functions=dict(stop_t=lambda x: cmd.get_var('grad_ramp_time'), stop_x=lambda x: cmd.get_var('Bx_grad_mix'), start_x=lambda x: cmd.get_var('Bx_grad'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')))
    return prg
