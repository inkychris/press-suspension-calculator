import physics
import plotly
import plotly.graph_objs as go

press = physics.System()
press.spring.constant = 3190
press.spring.free_length = 0.098
press.spring.minimum_length = 0.0359

press_ab = 0.02
press_ab_max = 0.2
press_ab_inc = 0.001

x = []
y_compression = []
y_spring_force = []
y_spring_force_maximum = []
y_press_bc = []
y_press_ec = []
y_press_be_minimum = []

while press_ab <= press_ab_max:
    press.ab = press_ab
    compression = press.spring_compression()
    press_be_minimum = press.be_minimum()
    try:
        max_spring_force = press.spring.force_at_length(press_be_minimum)
    except AttributeError:
        max_spring_force = 0

    x.append(press_ab)
    y_compression.append(compression * 1e+3)
    y_spring_force.append(press.spring.force(compression))
    y_press_bc.append(press.bc() * 1e+3)
    y_press_ec.append(press.ec() * 1e+3)
    y_press_be_minimum.append(press_be_minimum * 1e+3)
    y_spring_force_maximum.append(max_spring_force)

    press_ab = round(press_ab + press_ab_inc, 12)


trace_compression = go.Trace(
    x = x,
    y = y_compression,
    name = "Spring Compression Rest (mm)"
)

trace_spring_force = go.Trace(
    x = x,
    y = y_spring_force,
    name = "Spring Force Rest (N)"
)

trace_press_bc = go.Trace(
    x = x,
    y = y_press_bc,
    name = "bc Rest (mm)"
)

trace_press_ec = go.Trace(
    x = x,
    y = y_press_ec,
    name = "ec (mm)"
)

trace_press_be_minimum = go.Trace(
    x = x,
    y = y_press_be_minimum,
    name = "Spring Length Min (mm)"
)

trace_spring_force_maximum = go.Trace(
    x = x,
    y = y_spring_force_maximum,
    name = "Spring Force Max (N)"
)

data = [trace_compression, trace_spring_force, trace_press_bc, trace_press_ec, trace_press_be_minimum, trace_spring_force_maximum]
plotly.offline.plot(data)