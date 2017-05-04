import physics
import plotly
import plotly.graph_objs as go

def main(rest_angle):
    press = physics.System()

    press.rest_angle = rest_angle
    press.load = 2

    press.spring.constant = 1630
    press.spring.free_length = 0.135
    press.spring.minimum_length = 0.0388

    press_ab_min = 0.02
    press_ab_max = 0.15
    press_ab_inc = 0.005

    x = []
    y_compression = []
    y_spring_force = []
    y_spring_force_maximum = []
    y_press_bc = []
    y_press_ec = []
    y_press_be_minimum = []

    while press_ab_min <= press_ab_max:
        press.ab = press_ab_min
        compression = press.spring_compression()
        press_be_minimum = press.be_minimum()
        try:
            max_spring_force = press.spring.force_at_length(press_be_minimum)
        except AttributeError:
            max_spring_force = 0

        x.append(press_ab_min)
        y_compression.append(compression * 1e+3)
        y_spring_force.append(press.spring.force(compression))
        y_press_bc.append(press.bc() * 1e+3)
        y_press_ec.append(press.ec() * 1e+3)
        y_press_be_minimum.append(press_be_minimum * 1e+3)
        y_spring_force_maximum.append(max_spring_force)

        press_ab_min = round(press_ab_min + press_ab_inc, 12)


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

    figure = {"data" : data, "layout" : {"title": "Screen Press System Analysis - Rest angle: {ang}, {load}kg load".format(
        ang=press.rest_angle, load=press.load)}}

    plotly.offline.plot(figure, filename="{load}kg-load_{Sk}Nm-1_{ang}deg-rest-angle.html".format(
        Sk=press.spring.constant, ang=press.rest_angle, load=press.load))


for angle in [25, 30, 35]:
    main(angle)