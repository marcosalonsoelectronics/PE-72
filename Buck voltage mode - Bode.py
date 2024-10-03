# -*- coding: utf-8 -*-
"""
Buck converter with voltage-mode control
"""
from math import pi, log10, sqrt
import numpy as np
from control import tf, bode_plot, margin, step_response
import matplotlib.pyplot as plt
# Create Laplace variable
s = tf('s')
Vi=12; f=100e3; w= 2*pi*f; Vpp= 1;
L= 100e-6; C=10e-6; rL=50e-3; rc=0.2; R=5
fo= 1/(2*pi*sqrt(L*C)) ;fz=1/(2*pi*rc*C)
# Buck converter
Gd= Vi*(1 + rc*C*s)/( L*C*(1+rc/R)*s**2 + \
                         (L/R + rc*C + rL*C + rL*rc*C/R)*s + 1 + rL/R  )
# PWM modulator
wc= sqrt(12)*f; fc=wc/(2*pi); xi=sqrt(3)/2
# xi= sqrt(3)/2
Gm= (1/Vpp)*wc**2/( s**2 + 2*xi*wc*s + wc**2)
Gc=Gm*Gd

print("fo (kHz)= ", fo/1000); print("fz (kHz)= ", fz/1000);
print("fc (kHz)= ", fc/1000); print("xi= ", xi)


# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz

mag, phase, omega = bode_plot(Gd, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="blue", label="Gd(s)" )
    
print("Gd-----") 
i=60
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 
i=65
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 


mag, phase, omega = bode_plot(Gm, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="red", label="Gm(s)" )
    
mag, phase, omega = bode_plot(Gc, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="green", label="Gc(s)" )
    
ax1,ax2 = plt.gcf().axes     # get subplot axes
plt.sca(ax1)                 # select magnitude plot
plt.ylim(-80,60)
plt.yticks(np.arange(-80, 60, 20)) 
plt.sca(ax2)                 # select magnitude plot
plt.ylim(-270, 45, 45)
plt.yticks(np.arange(-270, 45, 45)) 
plt.legend()
    

print("Gc-----") 
i=60
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 
i=65
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 






















