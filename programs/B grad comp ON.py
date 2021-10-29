prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-130, "B comp x ramp", start_t=0.2, stop_x=0, n_points=50, start_x=0, stop_t=1, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2'), start_x=lambda x: cmd.get_var('Bx_dipole_trap'), stop_t=lambda x: cmd.get_var('grad_ramp_time'), stop_x=lambda x: cmd.get_var('Bx_grad_comp')))
    prg.add(-1, "B grad x ramp", start_t=0, stop_x=0, n_points=50, start_x=0.0, stop_t=1, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2'), start_x=lambda x: cmd.get_var('Bx_grad'), stop_t=lambda x: cmd.get_var('grad_ramp_time'), stop_x=lambda x: cmd.get_var('Bx_grad_mix')))
    prg.add(10000, "B comp x ramp", start_t=0, stop_x=0, n_points=50, start_x=0, stop_t=0, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+cmd.get_var('grad_ramp_time'), start_x=lambda x: cmd.get_var('Bx_grad_comp'), stop_t=lambda x: cmd.get_var('grad_ramp_time'), stop_x=lambda x: cmd.get_var('Bx_comp_after_ramp')), enable=False)
    prg.add(11000, "B grad x ramp", start_t=0, stop_x=0, n_points=50, start_x=0, stop_t=0, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+cmd.get_var('grad_ramp_time'), start_x=lambda x: cmd.get_var('Bx_grad_mix'), stop_t=lambda x: cmd.get_var('grad_ramp_time'), stop_x=lambda x: cmd.get_var('Bx_grad_after_ramp')), enable=False)
    return prg
