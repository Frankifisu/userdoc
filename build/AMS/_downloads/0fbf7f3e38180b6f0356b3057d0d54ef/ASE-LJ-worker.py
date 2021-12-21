from scm.amspipe import ASEPipeWorker
from ase.calculators.lj import LennardJones

calculator = LennardJones()
calculator.parameters.epsilon = 0.0102996
calculator.parameters.sigma = 3.4
calculator.parameters.rc = 12.0

engine = ASEPipeWorker(calculator=calculator)
engine.run()
