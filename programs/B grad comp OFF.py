prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "B grad x ramp", start_t=0, stop_x=0, n_points=50, start_x=0.2, stop_t=1, functions=dict(stop_x=lambda x: 0.28, start_x=lambda x: cmd.get_var('Bx_grad_mix')))
    prg.add(100, "B comp x ramp", start_t=0.2, stop_x=0, n_points=50, start_x=0, stop_t=1, functions=dict(stop_x=lambda x: cmd.get_var('Bx_GM')+cmd.get_var('Bx_tof_imaging'), start_x=lambda x: cmd.get_var('Bx_grad_comp')))
    return prg
