from clawpack import riemann
from clawpack.riemann.shallow_roe_with_efix_2D_constants import num_eqn, depth, x_momentum, y_momentum
import numpy as np

def setup(qinit, kernel_language='Fortran', use_petsc=False, outdir='./_output',
          solver_type='classic', riemann_solver='roe',disable_output=False, xlower = -3, xupper = 3,
          ylower = -3, yupper = 3, mx = 150, my = 150, tfin = 3, n_t = 100):

    if use_petsc:
        import clawpack.petclaw as pyclaw
    else:
        from clawpack import pyclaw

    if riemann_solver.lower() == 'roe':
        rs = riemann.shallow_roe_with_efix_2D
    elif riemann_solver.lower() == 'hlle':
        rs = riemann.shallow_hlle_2D

    solver = pyclaw.ClawSolver2D(rs)
    solver.limiters = pyclaw.limiters.tvd.MC
    solver.dimensional_split = 1

    solver.bc_lower[0] = pyclaw.BC.extrap
    solver.bc_upper[0] = pyclaw.BC.wall
    solver.bc_lower[1] = pyclaw.BC.extrap
    solver.bc_upper[1] = pyclaw.BC.wall

    x = pyclaw.Dimension(xlower, xupper, mx, name='x')
    y = pyclaw.Dimension(ylower, yupper, my, name='y')
    domain = pyclaw.Domain([x, y])

    state = pyclaw.State(domain, num_eqn)

    # Gravitational constant
    state.problem_data['grav'] = 10.0

    qinit(state)

    claw = pyclaw.Controller()
    claw.tfinal = tfin
    claw.solution = pyclaw.Solution(state, domain)
    claw.solver = solver
    if disable_output:
        claw.output_format = None
    claw.outdir = outdir
    claw.num_output_times = n_t
    claw.keep_copy = True
    claw.write_aux_always = True

    return claw

def z_values(qinit, tlim, frames, meshgrid_num,xlim, ylim):
    claw = setup(qinit, tfin=tlim[1], n_t=frames, xlower=xlim[0], xupper=xlim[1], ylower=ylim[0], yupper=ylim[1], mx=meshgrid_num, my=meshgrid_num)
    claw.run()
    values = [np.zeros((meshgrid_num, meshgrid_num))] * len(claw.frames)

    for i in range (len(claw.frames)):
        values[i] = claw.frames[i].state.q[0]

    return values

