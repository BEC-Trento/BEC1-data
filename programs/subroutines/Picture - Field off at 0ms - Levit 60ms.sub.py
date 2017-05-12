prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-3902000, "Na Repumper1 (+) Amp", 1)
    prg.add(-3862000, "Na Dark Spot Amp", 1)
    prg.add(-3852000, "Na Repumper MOT Amp", 1)
    prg.add(-3502000, "Shutter Probe Na Open")
    prg.add(-3012000, "Na Probe/Push (-) Amp", 1)
    prg.add(-3002000, "Na Probe/Push (+) Amp", 1)
    prg.add(-2512000, "Shutter repump Na Open")
    prg.add(-1529000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-1519000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-1499000, "Shutter 3DMOT cool Na Open")
    prg.add(-550000, "B comp y", 0.0000)
    prg.add(-500000, "IGBT B comp y ON")
    prg.add(-9500, "B comp y", 0.0000)
    prg.add(-8970, "B comp y", 0.2600)
    prg.add(-8450, "B comp y", 0.5300)
    prg.add(-7920, "B comp y", 0.7900)
    prg.add(-7390, "B comp y", 1.0500)
    prg.add(-6870, "B comp y", 1.3200)
    prg.add(-6340, "B comp y", 1.5800)
    prg.add(-5820, "B comp y", 1.8400)
    prg.add(-5290, "B comp y", 2.1100)
    prg.add(-4760, "B comp y", 2.3700)
    prg.add(-4240, "B comp y", 2.6300)
    prg.add(-3710, "B comp y", 2.8900)
    prg.add(-3180, "B comp y", 3.1600)
    prg.add(-2660, "B comp y", 3.4200)
    prg.add(-2130, "B comp y", 3.6800)
    prg.add(-1610, "B comp y", 3.9500)
    prg.add(-1080, "B comp y", 4.2100)
    prg.add(-550, "B comp y", 4.4700)
    prg.add(-30, "B comp y", 4.7400)
    prg.add(0, "IGBT 1 pinch", -10.0000)
    prg.add(20, "IGBT 3 Open")
    prg.add(60, "IGBT 2 pinch+comp", 10.0000)
    prg.add(160, "IGBT 2 pinch+comp", 9.8000)
    prg.add(260, "IGBT 2 pinch+comp", 9.6000)
    prg.add(360, "IGBT 2 pinch+comp", 9.4000)
    prg.add(460, "IGBT 2 pinch+comp", 9.2000)
    prg.add(500, "B comp y", 5.0000)
    prg.add(560, "IGBT 2 pinch+comp", 9.0000)
    prg.add(660, "IGBT 2 pinch+comp", 8.8000)
    prg.add(760, "IGBT 2 pinch+comp", 8.6000)
    prg.add(859, "IGBT 2 pinch+comp", 8.4000)
    prg.add(960, "IGBT 2 pinch+comp", 8.2000)
    prg.add(1060, "IGBT 2 pinch+comp", 8.0000)
    prg.add(1160, "IGBT 2 pinch+comp", 7.8000)
    prg.add(1260, "IGBT 2 pinch+comp", 7.6000)
    prg.add(1360, "IGBT 2 pinch+comp", 7.4000)
    prg.add(1460, "IGBT 2 pinch+comp", 7.2000)
    prg.add(1560, "IGBT 2 pinch+comp", 7.0000)
    prg.add(1660, "IGBT 2 pinch+comp", 6.8000)
    prg.add(1760, "IGBT 2 pinch+comp", 6.6000)
    prg.add(1860, "IGBT 2 pinch+comp", 6.4000)
    prg.add(1960, "IGBT 2 pinch+comp", 6.2000)
    prg.add(2060, "IGBT 2 pinch+comp", 6.0000)
    prg.add(2160, "IGBT 2 pinch+comp", 5.8000)
    prg.add(2260, "IGBT 2 pinch+comp", 5.6000)
    prg.add(2360, "IGBT 2 pinch+comp", 5.4000)
    prg.add(2460, "IGBT 2 pinch+comp", 5.2000)
    prg.add(2560, "IGBT 2 pinch+comp", 5.0000)
    prg.add(2660, "IGBT 2 pinch+comp", 4.8000)
    prg.add(2760, "IGBT 2 pinch+comp", 4.6000)
    prg.add(2859, "IGBT 2 pinch+comp", 4.4000)
    prg.add(2960, "IGBT 2 pinch+comp", 4.2000)
    prg.add(3060, "IGBT 2 pinch+comp", 4.0000)
    prg.add(3160, "IGBT 2 pinch+comp", 3.8000)
    prg.add(3260, "IGBT 2 pinch+comp", 3.6000)
    prg.add(3360, "IGBT 2 pinch+comp", 3.4000)
    prg.add(3459, "IGBT 2 pinch+comp", 3.2000)
    prg.add(3560, "IGBT 2 pinch+comp", 3.0000)
    prg.add(3660, "IGBT 2 pinch+comp", 2.8000)
    prg.add(3760, "IGBT 2 pinch+comp", 2.6000)
    prg.add(3860, "IGBT 2 pinch+comp", 2.4000)
    prg.add(3960, "IGBT 2 pinch+comp", 2.2000)
    prg.add(4060, "IGBT 2 pinch+comp", 2.0000)
    prg.add(4160, "IGBT 2 pinch+comp", 1.8000)
    prg.add(4260, "IGBT 2 pinch+comp", 1.6000)
    prg.add(4360, "IGBT 2 pinch+comp", 1.4000)
    prg.add(4460, "IGBT 2 pinch+comp", 1.2000)
    prg.add(4560, "IGBT 2 pinch+comp", 1.0000)
    prg.add(4660, "IGBT 2 pinch+comp", 0.8000)
    prg.add(4760, "IGBT 2 pinch+comp", 0.6000)
    prg.add(4860, "IGBT 2 pinch+comp", 0.4000)
    prg.add(4960, "IGBT 2 pinch+comp", 0.2000)
    prg.add(5060, "IGBT 2 pinch+comp", 0.0000)
    prg.add(5160, "IGBT 2 pinch+comp", -0.2000)
    prg.add(5260, "IGBT 2 pinch+comp", -0.4000)
    prg.add(5360, "IGBT 2 pinch+comp", -0.6000)
    prg.add(5460, "IGBT 2 pinch+comp", -0.8000)
    prg.add(5560, "IGBT 2 pinch+comp", -1.0000)
    prg.add(5659, "IGBT 2 pinch+comp", -1.2000)
    prg.add(5760, "IGBT 2 pinch+comp", -1.4000)
    prg.add(5860, "IGBT 2 pinch+comp", -1.6000)
    prg.add(5960, "IGBT 2 pinch+comp", -1.8000)
    prg.add(6060, "IGBT 2 pinch+comp", -2.0000)
    prg.add(6160, "IGBT 2 pinch+comp", -2.2000)
    prg.add(6260, "IGBT 2 pinch+comp", -2.4000)
    prg.add(6360, "IGBT 2 pinch+comp", -2.6000)
    prg.add(6460, "IGBT 2 pinch+comp", -2.8000)
    prg.add(6560, "IGBT 2 pinch+comp", -3.0000)
    prg.add(6660, "IGBT 2 pinch+comp", -3.2000)
    prg.add(6760, "IGBT 2 pinch+comp", -3.4000)
    prg.add(6860, "IGBT 2 pinch+comp", -3.6000)
    prg.add(6959, "IGBT 2 pinch+comp", -3.8000)
    prg.add(7060, "IGBT 2 pinch+comp", -4.0000)
    prg.add(7160, "IGBT 2 pinch+comp", -4.2000)
    prg.add(7260, "IGBT 2 pinch+comp", -4.4000)
    prg.add(7360, "IGBT 2 pinch+comp", -4.6000)
    prg.add(7460, "IGBT 2 pinch+comp", -4.8000)
    prg.add(7560, "IGBT 2 pinch+comp", -5.0000)
    prg.add(7660, "IGBT 2 pinch+comp", -5.2000)
    prg.add(7760, "IGBT 2 pinch+comp", -5.4000)
    prg.add(7860, "IGBT 2 pinch+comp", -5.6000)
    prg.add(7960, "IGBT 2 pinch+comp", -5.8000)
    prg.add(8060, "IGBT 2 pinch+comp", -6.0000)
    prg.add(8159, "IGBT 2 pinch+comp", -6.2000)
    prg.add(8260, "IGBT 2 pinch+comp", -6.4000)
    prg.add(8360, "IGBT 2 pinch+comp", -6.6000)
    prg.add(8460, "IGBT 2 pinch+comp", -6.8000)
    prg.add(8560, "IGBT 2 pinch+comp", -7.0000)
    prg.add(8660, "IGBT 2 pinch+comp", -7.2000)
    prg.add(8760, "IGBT 2 pinch+comp", -7.4000)
    prg.add(8860, "IGBT 2 pinch+comp", -7.6000)
    prg.add(8960, "IGBT 2 pinch+comp", -7.8000)
    prg.add(9060, "IGBT 2 pinch+comp", -8.0000)
    prg.add(9160, "IGBT 2 pinch+comp", -8.2000)
    prg.add(9260, "IGBT 2 pinch+comp", -8.4000)
    prg.add(9360, "IGBT 2 pinch+comp", -8.6000)
    prg.add(9460, "IGBT 2 pinch+comp", -8.8000)
    prg.add(9560, "IGBT 2 pinch+comp", -9.0000)
    prg.add(9660, "IGBT 2 pinch+comp", -9.2000)
    prg.add(9760, "IGBT 2 pinch+comp", -9.4000)
    prg.add(9860, "IGBT 2 pinch+comp", -9.6000)
    prg.add(9960, "IGBT 2 pinch+comp", -9.8000)
    prg.add(10060, "IGBT 2 pinch+comp", -10.0000)
    prg.add(10100, "IGBT 4 Open")
    prg.add(10120, "IGBT 5 Open")
    prg.add(10350, "IGBT 1 pinch", -10.0000)
    prg.add(10360, "IGBT 2 pinch+comp", -10.0000)
    prg.add(10370, "IGBT 3 Close")
    prg.add(10380, "IGBT 4 Close")
    prg.add(10390, "IGBT 5 Open")
    prg.add(10400, "Delta 2 Voltage", 0.0000)
    prg.add(10410, "Delta 1 Current", 15.500)
    prg.add(10450, "B comp x", 1200.0)
    prg.add(10500, "B comp y", 5.0000)
    prg.add(11030, "B comp y", 4.7400)
    prg.add(11550, "B comp y", 4.4700)
    prg.add(12080, "B comp y", 4.2100)
    prg.add(12609, "B comp y", 3.9500)
    prg.add(13130, "B comp y", 3.6800)
    prg.add(13660, "B comp y", 3.4200)
    prg.add(14180, "B comp y", 3.1600)
    prg.add(14710, "B comp y", 2.8900)
    prg.add(15240, "B comp y", 2.6300)
    prg.add(15760, "B comp y", 2.3700)
    prg.add(16290, "B comp y", 2.1100)
    prg.add(16820, "B comp y", 1.8400)
    prg.add(17340, "B comp y", 1.5800)
    prg.add(17870, "B comp y", 1.3200)
    prg.add(18390, "B comp y", 1.0500)
    prg.add(18920, "B comp y", 0.7900)
    prg.add(19450, "B comp y", 0.5300)
    prg.add(19970, "B comp y", 0.2600)
    prg.add(20500, "B comp y", 0.0000)
    prg.add(530000, "IGBT B comp z OFF")
    prg.add(545000, "IGBT 1 pinch", -10.0000)
    prg.add(545010, "IGBT 2 pinch+comp", -10.0000)
    prg.add(545020, "IGBT 3 Open")
    prg.add(545030, "IGBT 4 Open")
    prg.add(545040, "IGBT 5 Open")
    prg.add(550000, "IGBT B comp z OFF")
    prg.add(582000, "B comp y", 1.0000)
    prg.add(597000, "Na Repumper1 (+) Amp", 1000)
    prg.add(597500, "Na Repumper Tune (+) freq", 1713.0)
    prg.add(598000, "Na Repumper MOT Amp", 1000)
    prg.add(599799, "Na Probe/Push (+) freq", 110.00)
    prg.add(600200, "Na Probe/Push (-) freq", 110.00)
    prg.add(600500, "Trig ON Stingray 1")
    prg.add(600600, "Na Probe/Push (+) Amp", 1000)
    prg.add(601000, "Na Probe/Push (-) Amp", 1000)
    prg.add(602000, "Na Probe/Push (-) Amp", 1)
    prg.add(602500, "Trig OFF Stingray 1")
    prg.add(851000, "Shutter Probe Na Close")
    prg.add(1600500, "Trig ON Stingray 1")
    prg.add(1601000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1602000, "Na Probe/Push (-) Amp", 1)
    prg.add(1602500, "Trig OFF Stingray 1")
    prg.add(1611000, "Na Repumper MOT Amp", 1)
    prg.add(1621000, "Na Repumper1 (+) Amp", 1)
    prg.add(2600500, "Trig ON Stingray 1")
    prg.add(2602500, "Trig OFF Stingray 1")
    prg.add(3600500, "Trig ON Stingray 1")
    prg.add(3602500, "Trig OFF Stingray 1")
    prg.add(4100000, "Shutter Optical Levit Close")
    prg.add(4601000, "B comp y", 0.0000)
    prg.add(4700000, "IGBT B comp y OFF")
    prg.add(9100000, "Optical Levit ON")
    return prg
