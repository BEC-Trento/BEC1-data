import libraries.ramp as lib_ramp

def action_list_init(action_list):

    action_list.add("B comp x ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="B comp x", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="prova")
    
    action_list.add("B comp y ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="B comp y", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="prova")

    action_list.add("Rampa GM per test", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Na Gray molasses (-) Amp", act_var_name="amplitude"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")
    
    action_list.add("Delta 1 Current ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 1 Current", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Delta 2 Voltage ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 2 Voltage", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")
    
    action_list.add("Grav Comp ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Grav Comp", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Decompress Current 200-50", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 1 Current", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Decompress Voltage 200-50", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 2 Voltage", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Decompress Current 200-100", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 1 Current", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Decompress Voltage 200-100", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 2 Voltage", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")


    action_list.add("IGBT 1 ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="IGBT 1 pinch", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("IGBT 2 ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="IGBT 2 pinch+comp", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

                    
    action_list.add("Dipole Trap x ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Dipole Trap x DAC V", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=1, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="Tom")

                    
    action_list.add("Dipole Trap y ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Dipole Trap y DAC V", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=1, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="Tom")
                   

    action_list.add("RFO FM amp ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO FM amp", act_var_name="value"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="0-10")

    action_list.add("Analog71 Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Analog71", act_var_name="value"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="")

    action_list.add("Pinning Lock ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Pinning Lock", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=1, start_t=0, stop_t=100, n_points=50),
                    comment="prova")

# Time repetition ramps:

    action_list.add("RFO Trig Sweep burst", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO Sweep Trig Pulse"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("RFO SingleSweepTrig Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO SingleSweepTrig"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("RFO ImagingQuatum Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO ImagingQuantum"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("Picture EoS Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Picture EoS Quantum - Hamamatsu.sub"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("RFO FM ampQuantum Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO FM ampQuantum"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("RFO ImagingQuantum3 Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO ImagingQuantum3"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("RFO ImagingQuantum2-12 Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO ImagingQuantum2-12"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("RFO ImagingQuantum2-12-Hamamatsu Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO ImagingQuantum2-12-Hamamatsu"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("RFO ImagingQuantum-solo-Hamamatsu Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO ImagingQuantum-solo-Hamamatsu"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("RFO DoubleSweepTrig Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO DoubleSweepTrig"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("RFO SingleSweepTrig12 Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO SingleSweepTrig12"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")


