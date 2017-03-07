import libraries.action as lib_action
def action_list_init(act_lst):
    act_lst.add("Na Repumper MOT Amp", lib_action.DdsAction,
                board="DDS20",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Dark Spot Amp", lib_action.DdsAction,
                board="DDS20",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Repumper MOT freq", lib_action.DdsAction,
                board="DDS20",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na Repumper Dark Spot freq", lib_action.DdsAction,
                board="DDS20",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na Repumper MOT/Dark Spot", lib_action.DdsAction,
                board="DDS20",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Na Repumper Tune (+) freq", lib_action.DdsAction,
                board="DDS21",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.1f"),
                categories=["actions", "DDS"],
                comment="1632.5-1792.5 (1.6) MHz")
    act_lst.add("Na Repumper1 (+) Amp", lib_action.DdsAction,
                board="DDS21",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Repumper2 (+) Amp", lib_action.DdsAction,
                board="DDS21",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Repumper (+)", lib_action.DdsAction,
                board="DDS21",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Na Lock (+) freq", lib_action.DdsAction,
                board="DDS22",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na Lock (+) Amp", lib_action.DdsAction,
                board="DDS22",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Zeeman slower (-) freq", lib_action.DdsAction,
                board="DDS22",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.1f"),
                categories=["actions", "DDS"],
                comment="120-318 (0.5) MHz")
    act_lst.add("Na Zeeman slower (-) Amp", lib_action.DdsAction,
                board="DDS22",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Zeeman slower (-)", lib_action.DdsAction,
                board="DDS22",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Na Probe/Push (-) freq", lib_action.DdsAction,
                board="DDS23",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na Probe/Push (-) Amp", lib_action.DdsAction,
                board="DDS23",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Probe/Push (+) freq", lib_action.DdsAction,
                board="DDS23",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na Probe/Push (+) Amp", lib_action.DdsAction,
                board="DDS23",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Probe/Push", lib_action.DdsAction,
                board="DDS23",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Na 3D MOT cool (-) freq", lib_action.DdsAction,
                board="DDS24",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na 3D MOT cool (-) Amp", lib_action.DdsAction,
                board="DDS24",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na 3D MOT cool (+) freq", lib_action.DdsAction,
                board="DDS24",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na 3D MOT cool (+) Amp", lib_action.DdsAction,
                board="DDS24",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na 3D MOT cool", lib_action.DdsAction,
                board="DDS24",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Na 2D MOT (-) freq", lib_action.DdsAction,
                board="DDS25",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na 2D MOT (-) Amp", lib_action.DdsAction,
                board="DDS25",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na 2D MOT (+) freq", lib_action.DdsAction,
                board="DDS25",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na 2D MOT (+) Amp", lib_action.DdsAction,
                board="DDS25",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na 2D MOT", lib_action.DdsAction,
                board="DDS25",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Dipole Trap x AOM (+) freq", lib_action.DdsAction,
                board="DDS26",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Dipole Trap x AOM (+) Amp", lib_action.DdsAction,
                board="DDS26",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Dipole Trap y AOM (-) freq", lib_action.DdsAction,
                board="DDS26",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Dipole Trap y AOM (-) Amp", lib_action.DdsAction,
                board="DDS26",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Dipole Trap", lib_action.DdsAction,
                board="DDS26",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Optical Levit (+) freq", lib_action.DdsAction,
                board="DDS27",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Optical Levit (+) Amp", lib_action.DdsAction,
                board="DDS27",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Optical Levit (-) freq", lib_action.DdsAction,
                board="DDS27",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Optical Levit (-) Amp", lib_action.DdsAction,
                board="DDS27",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Optical Levit", lib_action.DdsAction,
                board="DDS27",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("K Lock (+) freq", lib_action.DdsAction,
                board="DDS30",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("K Lock (+) Amp", lib_action.DdsAction,
                board="DDS30",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("K Lock (+)", lib_action.DdsAction,
                board="DDS30",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("K Cooler 2p (+) freq", lib_action.DdsAction,
                board="DDS31",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("K Cooler 2p (+) Amp", lib_action.DdsAction,
                board="DDS31",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("K Cooler 1p (-) freq", lib_action.DdsAction,
                board="DDS31",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("K Cooler 1p (-) Amp", lib_action.DdsAction,
                board="DDS31",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("K Cooler 1p (-)", lib_action.DdsAction,
                board="DDS31",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("K Repumper 2p (+) freq", lib_action.DdsAction,
                board="DDS32",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("K Repumper 2p (+) Amp", lib_action.DdsAction,
                board="DDS32",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("K Repumper 1p (+) freq", lib_action.DdsAction,
                board="DDS32",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("K Repumper 1p (+) Amp", lib_action.DdsAction,
                board="DDS32",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("K Repumper 1p (+)", lib_action.DdsAction,
                board="DDS32",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("K probe Repumper (+) freq", lib_action.DdsAction,
                board="DDS33",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("K probe Repumper (+) Amp", lib_action.DdsAction,
                board="DDS33",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("K probe Cooler (-) freq", lib_action.DdsAction,
                board="DDS33",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("K probe Cooler (-) Amp", lib_action.DdsAction,
                board="DDS33",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("K probe (-)", lib_action.DdsAction,
                board="DDS33",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("DDS34 freq", lib_action.DdsAction,
                board="DDS34",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("DDS34 Amp", lib_action.DdsAction,
                board="DDS34",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("DDS34", lib_action.DdsAction,
                board="DDS34",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Na Bragg relative freq 80 pm 2 MHz", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="78.01 to 81.99 (0.01) MHz")
    act_lst.add("Na Bragg relative freq 80 pm 20 MHz", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.1f"),
                categories=["actions", "DDS"],
                comment="60.1 to 99.9 (0.1) MHz")
    act_lst.add("Na Bragg (-) freq", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na Bragg (-) Amp", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Bragg ch1 Amp", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Bragg (+) freq", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na Bragg (+) Amp", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Bragg ch2 Amp", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Bragg", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Na Gray molasses (+) freq", lib_action.DdsAction,
                board="DDS19",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na Gray molasses (+) Amp", lib_action.DdsAction,
                board="DDS19",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Gray molasses (-) freq", lib_action.DdsAction,
                board="DDS19",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60-159 (0.25) MHz")
    act_lst.add("Na Gray molasses (-) Amp", lib_action.DdsAction,
                board="DDS19",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Na Gray molasses", lib_action.DdsAction,
                board="DDS19",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
# Copying Gray molasses --> Phase Imprint 2016-11-29 AMPLITUDE ONLY
    act_lst.add("Phase Imprint 2016 ch1 Amp", lib_action.DdsAction,
                board="DDS19",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("Phase Imprint 2016", lib_action.DdsAction,
                board="DDS19",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Evaporation", lib_action.DdsAction,
                board="DDS50",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Evaporation uw", lib_action.DdsAction,
                board="DDS51",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("RFO1 Amp", lib_action.DdsAction,
                board="DDS52",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("RFO1 freq", lib_action.DdsAction,
                board="DDS52",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.3f"),
                categories=["actions", "DDS"],
                comment=".65-1.05 (0.001) MHz")
    act_lst.add("RFO2 Amp", lib_action.DdsAction,
                board="DDS52",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("RFO2 freq", lib_action.DdsAction,
                board="DDS52",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.3f"),
                categories=["actions", "DDS"],
                comment=".65-1.05 (0.001) MHz")
    act_lst.add("RFO", lib_action.DdsAction,
                board="DDS52",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("B comp y", lib_action.AnalogAction,
                board="ANG60",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="A")
    act_lst.add("B comp x", lib_action.AnalogAction,
                board="ANG61",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.1f"),
                categories=["actions", "analog"],
                comment="mA")
    act_lst.add("IGBT 1 pinch", lib_action.AnalogAction,
                board="ANG62",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="V")
    act_lst.add("IGBT 2 pinch+comp", lib_action.AnalogAction,
                board="ANG63",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="V")
    act_lst.add("Delta 1 Voltage", lib_action.AnalogAction,
                board="ANG64",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="V")
    act_lst.add("Delta 1 Current", lib_action.AnalogAction,
                board="ANG65",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.3f"),
                categories=["actions", "analog"],
                comment="A")
    act_lst.add("Delta 2 Voltage", lib_action.AnalogAction,
                board="ANG66",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="V")
    act_lst.add("Delta 2 Current", lib_action.AnalogAction,
                board="ANG67",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.3f"),
                categories=["actions", "analog"],
                comment="A")
    act_lst.add("DDS10 test", lib_action.DdsAction,
                board="DDS10",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    act_lst.add("Dipole Trap y DAC V", lib_action.AnalogAction,
                board="ANG69",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")
    act_lst.add("Dipole Trap x DAC V", lib_action.AnalogAction,
                board="ANG70",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")
    act_lst.add("Analog71", lib_action.AnalogAction,
                board="ANG71",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 5V")
    act_lst.add("RFO FM amp", lib_action.AnalogAction,
                board="ANG72",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 5V")
    act_lst.add("Initialize 0 TTL0", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]),
                categories=["actions", "TTL"])
    act_lst.add("Initialize 1 TTL0", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]),
                categories=["actions", "TTL"])
    act_lst.add("Initialize Test IGBT", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False]),
                categories=["actions", "TTL"])
    act_lst.add("Initialize MOT TTL0", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[False, False, False, False, True, False, False, True, False, True, True, False, False, False, False, False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL RF OFF", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[1], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL RF ON", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[1], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Trigger LZ OFF", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[2], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Trigger LZ ON", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[2], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT 4 Close", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[3], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT 4 Open", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[3], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Trig OFF Stingray 2", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[4], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Trig ON Stingray 2", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[4], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 3 Open", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[5], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 3 Close", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[5], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL broken OFF", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[6], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL broken ON", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[6], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 5 Open", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[7], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 5 Close", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[7], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT 3 Open", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[8], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT 3 Close", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[8], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL0-9 broken OFF", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[9], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL0-9 broken ON", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[9], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT 5 Open", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[10], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT 5 Close", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[10], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 1 Open", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[11], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 1 Close", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[11], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 2 Open", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[12], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 2 Close", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[12], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL0-13 broken OFF", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[13], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL0-13 broken ON", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[13], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 4 Open", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[14], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Rele 4 Close", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[14], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Breakpoint Main Table TTL OFF", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[15], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Breakpoint Main Table TTL ON", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[15], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("RF02 OFF", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[16], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("RF02 ON", lib_action.DigitalAction,
                board="TTL0",
                parameters=dict(channel=[16], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL1 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[1], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL1 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[1], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[2], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[2], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL3 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[3], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL3 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[3], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL4 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[4], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL4 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[4], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL5 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[5], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL5 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[5], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL6 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[6], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL6 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[6], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL7 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[7], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL7 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[7], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL8 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[8], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL8 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[8], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL9 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[9], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL9 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[9], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL10 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[10], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL10 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[10], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL11 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[11], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL11 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[11], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL12 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[12], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL12 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[12], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL13 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[13], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL13 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[13], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL14 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[14], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL14 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[14], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL15 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[15], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL15 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[15], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL16 OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[16], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL16 ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[16], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Initialize 0 TTL2", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False]),
                categories=["actions", "TTL"])
    act_lst.add("Initialize 1 TTL2", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]),
                categories=["actions", "TTL"])
    act_lst.add("Bcomp z Sign Plus", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[1], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Bcomp z Sign Minus", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[1], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("RFO Sweep Trig 2 OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[2], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("RFO Sweep Trig 2 ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[2], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Bcomp y Sign Minus", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[3], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Bcomp y Sign Plus", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[3], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Pulse 2 uw ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[4], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Pulse 2 uw OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[4], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2 5 OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[5], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2 5 ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[5], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Mirrors Imaging", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[6, 7, 8], status=[True, True, False]),
                categories=["actions", "TTL"])
    act_lst.add("Mirrors Imaging Bragg", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[6, 7, 8], status=[True, False, True]),
                categories=["actions", "TTL"])
    act_lst.add("Mirrors MOT", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[6, 7, 8], status=[False, False, False]),
                categories=["actions", "TTL"])
    act_lst.add("Bx Grad OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[9], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Bx Grad ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[9], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-10 OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[10], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-10 ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[10], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-11 OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[11], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-11 ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[11], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-12 OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[12], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-12 ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[12], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-13 OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[13], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-13 ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[13], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-14 OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[14], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-14 ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[14], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-15 OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[15], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-15 ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[15], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-16 OFF", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[16], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL2-16 ON", lib_action.DigitalAction,
                board="TTL2",
                parameters=dict(channel=[16], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Initialize 0 TTL3", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]),
                categories=["actions", "TTL"])
    act_lst.add("Initialize 1 TTL3", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Probe Na Close", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[1], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Probe Na Open", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[1], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Push Na Close", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[2], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Push Na Open", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[2], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter 3DMOT cool Na Close", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[3], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter 3DMOT cool Na Open", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[3], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter EOM Na Close", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[4], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter EOM Na Open", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[4], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter repump Na Close", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[5], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter repump Na Open", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[5], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Bragg Close", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[6], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Bragg Open", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[6], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Repumper D1 OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[7], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Repumper D1 ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[7], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Phase Imprint Close", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[8], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Phase Imprint Open", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[8], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Gray molasses Open", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[9], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Gray molasses Close", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[9], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Bragg D1 Open", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[8, 9], status=[True, False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Bragg D1 Close", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[8, 9], status=[False, True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL3-10 OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[10], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL3-10 ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[10], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL3-11 OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[11], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL3-11 ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[11], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Bragg burst OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[12], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Bragg burst ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[12], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("TTL3-13 OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[13], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("TTL3-13 ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[13], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Breakpoint Na Table TTL OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[14], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Breakpoint Na Table TTL ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[14], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Na Probe/Push (+) OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[15], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Na Probe/Push (+) ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[15], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Na 3D MOT cool (-) OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[16], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Na 3D MOT cool (-) ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[16], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Bragg OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[16], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Bragg ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[16], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Initialize 0 TTL4", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False]),
                categories=["actions", "TTL"])
    act_lst.add("Initialize 1 TTL4", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]),
                categories=["actions", "TTL"])
    act_lst.add("Trigger uw sweep OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[1], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Trigger uw sweep ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[1], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Trigger uw amp OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[2], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Trigger uw amp ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[2], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Pulse MOT Na ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[3], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Pulse MOT Na OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[3], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Pulse MOT K OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[4], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Pulse MOT K ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[4], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Optical Levit OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[5], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Optical Levit ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[5], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Optical Levit Close", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[6], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Shutter Optical Levit Open", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[6], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Trig OFF Stingray 1", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[7, 8], status=[False, False]),
                categories=["actions", "TTL"])
    act_lst.add("Trig ON Stingray 1", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[7, 8], status=[True, True]),
                categories=["actions", "TTL"])
    act_lst.add("Bottom Evaporation OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[9], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Bottom Evaporation ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[9], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT B comp z OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[10], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT B comp z ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[10], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT B comp x OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[11], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT B comp x ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[11], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT B comp y OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[12], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT B comp y ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[12], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Trig Slow Stingray OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[13], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Trig Slow Stingray ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[13], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT 6 Open", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[14], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("IGBT 6 Close", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[14], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("Pulse uw OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[15], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("Pulse uw ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[15], status=[True]),
                categories=["actions", "TTL"])
    act_lst.add("RFO Sweep Trig OFF", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[16], status=[False]),
                categories=["actions", "TTL"])
    act_lst.add("RFO Sweep Trig ON", lib_action.DigitalAction,
                board="TTL4",
                parameters=dict(channel=[16], status=[True]),
                categories=["actions", "TTL"])


