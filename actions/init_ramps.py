import libraries.ramp as lib_ramp

def action_list_init(action_list):

# 2017-04-10 brand newer FunctionRamps

    action_list.add("Dipole y Func", lib_ramp.FunctionRamp,
                    categories=["func"],
                    parameters=dict(act_name="Dipole Trap y DAC V", act_var_name="value", act_parameters={}),
                    variables=dict(start_t=0, stop_t=100, n_points=100,
                                   func="amp*sin(2*pi*freq*t)**2", func_args="amp=5, freq=100"),
                    var_formats=dict(start_t="%.4f", stop_t="%.4f", n_points="%d", func="%s", func_args="%s"),
                    comment="time")
    
    action_list.add("Pulse uw Func", lib_ramp.FunctionRamp,
                    categories=["func"],
                    parameters=dict(act_name="Pulse uw", act_var_name="pulse_t", act_parameters={'polarity': 1}),
                    variables=dict(start_t=0, stop_t=100, n_points=100,
                                   func="sin(2*pi*freq*t)**2", func_args=""),
                    var_formats=dict(start_t="%.4f", stop_t="%.4f", n_points="%d", func="%s", func_args="%s"),
                    comment="time")
                    
    action_list.add("MT trap Heating", lib_ramp.FunctionRamp,
                    categories=["func"],
                    parameters=dict(act_name="Delta 1 Current", act_var_name="value", act_parameters={}),
                    variables=dict(start_t=0, stop_t=100, n_points=100,
                                   func="amp*sin(2*pi*freq*t) + offs", func_args="amp=5, freq=200, offs=50"),
                    var_formats=dict(start_t="%.4f", stop_t="%.4f", n_points="%d", func="%s", func_args="%s"),
                    comment="time")  

# 2017-04-10 brand new TTLPulse ramps

    action_list.add("Pulse uw Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Pulse uw", act_var_name="pulse_t", act_parameters={'polarity': 1}),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=400, n_points=5),
                    var_formats=dict(start_x="%.4f", stop_x="%.4f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")  
                    
    action_list.add("TTL2-12 Pulse Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Pulse TTL2-12", act_var_name="pulse_t"),
                    variables=dict(start_x=1, stop_x=2, start_t=0, stop_t=400, n_points=5),
                    var_formats=dict(start_x="%.4f", stop_x="%.4f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")
                    
    action_list.add("Probe Pulse Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Pulse Probe Na", act_var_name="pulse_t"),
                    variables=dict(start_x=.1, stop_x=.1, start_t=0, stop_t=400, n_points=5),
                    var_formats=dict(start_x="%.4f", stop_x="%.4f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")
                                        
    action_list.add("Bottom Evap Pulse Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Pulse Bottom Evap", act_var_name="pulse_t"),
                    variables=dict(start_x=1, stop_x=2, start_t=0, stop_t=400, n_points=5),
                    var_formats=dict(start_x="%.4f", stop_x="%.4f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")
                    
# Analog actions ramps                    

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
                    
    action_list.add("B comp z ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="B comp z", act_var_name="value"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="")

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

    action_list.add("Delta 1 Voltage ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 1 Voltage", act_var_name="value"),
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
                    variables=dict(start_x=200, stop_x=50, start_t=0, stop_t=300, n_points=600),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Delta 1 Current ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 1 Current", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=0),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Decompress Voltage 200-50", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 2 Voltage", act_var_name="value"),
                    variables=dict(start_x=30, stop_x=0, start_t=0, stop_t=600, n_points=150),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Decompress Current 200-100", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 1 Current", act_var_name="value"),
                    variables=dict(start_x=200, stop_x=100, start_t=0, stop_t=600, n_points=150),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Decompress Voltage 200-100", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Delta 2 Voltage", act_var_name="value"),
                    variables=dict(start_x=30, stop_x=0, start_t=0, stop_t=600, n_points=150),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="prova")

    action_list.add("Delta 2 Voltage ramp", lib_ramp.LinearRamp,
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

    action_list.add("B compensation ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="BcompRamp", act_var_name="value"),
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

    action_list.add("RFO ImagingQuatum Ramp - Trig2", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RFO ImagingQuantum - Trig2"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("Picture EoS Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Picture EoS Quantum - Hamamatsu.sub"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")
                    
    action_list.add("Picture Ramp Trig1", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Picture Quantum - 1 shot Trig1"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=400, n_points=4),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

    action_list.add("Picture Ramp Trig2", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Picture Quantum - 1 shot Trig2"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=400, n_points=4),
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

    action_list.add("Bottom Evaporation ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Bottom Evaporation pulse"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=20, n_points=6),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="time")

# AOM amps/freqs
    action_list.add("Na Repumper1 (+) Amp ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Na Repumper1 (+) Amp", act_var_name="amplitude"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="")

    action_list.add("Na 3D MOT cool (+) freq ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Na 3D MOT cool (+) freq", act_var_name="frequency"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="")

    action_list.add("Na 3D MOT cool (-) freq ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Na 3D MOT cool (-) freq", act_var_name="frequency"),
                    variables=dict(start_x=1, stop_x=0, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="")

    action_list.add("GM amp(+) ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="AOM GM Amp ch1 (+)", act_var_name="amplitude"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")
    
    action_list.add("GM Detuning ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="AOM GM Detuning", act_var_name="frequency"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")
                    
    action_list.add("Optical Levit (+) freq ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Optical Levit (+) freq", act_var_name="frequency"),
                    variables=dict(start_x=100, stop_x=140, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="")
                    
    action_list.add("DDS27 ch1 freq ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Optical Levit (+) freq", act_var_name="frequency"),
                    variables=dict(start_x=100, stop_x=140, start_t=0, stop_t=100, n_points=100),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="")
                    
    action_list.add("DDS27 ch2 freq ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="Optical Levit (-) freq", act_var_name="frequency"),
                    variables=dict(start_x=100, stop_x=110, start_t=0, stop_t=20, n_points=400),
                    var_formats=dict(start_x="%.3f", stop_x="%.3f", start_t="%.4f", stop_t="%.4f", n_points="%d"),
                    comment="")                                        


