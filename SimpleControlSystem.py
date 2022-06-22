# Libraries
import numpy as np
import sympy
import control
import matplotlib.pyplot as plt
import math
import random

"""     Model build up      """
# transfer function of the system
dt = 0.001
system_tf = control.tf([0, 0, 1],[0, 1, 0])
system_tf_z = control.c2d(system_tf, dt)
print("\n\nSystem transfer functions")
print(system_tf)
print(system_tf_z)

# transfer function of the controller
Kp = 1.
Ki = 0.
Kd = 0.
num = [Kd, Kp]
den = [Ki, 1]
controller_tf = control.tf(num, den)
controller_tf_z = control.c2d(controller_tf, dt)
print("\n\nController transfer functions")
print(controller_tf)
print(controller_tf_z)

open_loop_tf = control.series(controller_tf, system_tf)
open_loop_tf_z = control.c2d(open_loop_tf, dt)
print("\n\nOpen loop transfer functions")
print(open_loop_tf)
print(open_loop_tf_z)

closed_loop_tf = control.feedback(open_loop_tf)
closed_loop_tf_z = control.c2d(closed_loop_tf, dt)
print("\n\nClosed loop transfer functions")
print(closed_loop_tf)
print(closed_loop_tf_z)

"""     Time domain analysis    """
# step response
t_step = np.arange(0, 20, 0.001)
t_step_z = np.arange(0, 20, 0.001)
step_time, step_resp_integrator = control.step_response(open_loop_tf, T=t_step)
step_time_z, step_resp_integrator_z = control.step_response(open_loop_tf, T=t_step_z)

fig1 = plt.figure(figsize=(12, 8))
axs = fig1.subplots(2)
axs[0].plot(step_time, step_resp_integrator)
axs[1].plot(step_time_z, step_resp_integrator_z)


# Bode plots
fig2 = plt.figure(figsize=(12, 8))
control.bode_plot(system_tf_z)

# Nichols
fig3 = plt.figure(figsize=(12, 8))
control.nichols_plot(system_tf_z)

plt.show()

