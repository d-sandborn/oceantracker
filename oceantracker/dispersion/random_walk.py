import numpy as np
from oceantracker.util.parameter_checking import ParamValueChecker as PVC
from oceantracker.dispersion._base_dispersion import _BaseTrajectoryModifer
from numba import njit, types as nbtypes
from random import normalvariate

class RandomWalk(_BaseTrajectoryModifer):
    # add random walk using velocity modifier
    def __init__(self):
        # set up default params
        super().__init__()  # required in children to get parent defaults
        self.add_default_params({'A_H': PVC(1.0,float,min=0.), 'A_V': PVC(0.001,float,min=0.), } )

    def initial_setup(self):
        si = self.shared_info
        info = self.info
        dt = si.model_time_step
        info['random_walk_size'] = np.array((self.calc_walk(self.params['A_H'], dt), self.calc_walk(self.params['A_H'], dt), self.calc_walk(self.params['A_V'], dt)))
        if not si.hydro_model_is3D:
            info['random_walk_size'] = info['random_walk_size'][:2]

        info['random_walk_velocity'] = info['random_walk_size'] /si.solver_info['model_time_step']  # velocity equivalent of random walk distance

    def calc_walk(self, A_turb, dt):
        # this is variance of particle motion in each vector direction,
        # ( factor of 2 would  be 6 , if wanting 3D isotropic variance, rather than its separate effect on 1D components used above)
        return np.sqrt(2. * np.abs(dt) * np.abs(A_turb))

    # apply random walk
    def update(self,time_sec, active):
        # add up 2D/3D diffusion coeff as random walk done using velocity_modifier
        #todo remove nb param,  when changed to using arbitary time step, not substeping

        si= self.shared_info
        self._add_random_walk_velocity_modifier(self.info['random_walk_velocity'], active, si.classes['particle_properties']['velocity_modifier'].data)

    @staticmethod
    @njit()
    #@guvectorize([(float64[:],int32[:],float64[:,:])],' (m), (l)->(n,m)') #, does not work needs n on LHS
    # below signature does not increase  speed much?
    #@njit(nbtypes.void(nbtypes.float64[:],nbtypes.int32[:],nbtypes.float64[:,:]))
    def _add_random_walk_velocity_modifier(random_walk_velocity, active, velocity_modifier):
        for n in active:
            for m in range(velocity_modifier.shape[1]):
                # todo below slow? is allocating memory??, try math.random random.Genetaor.normal  and get 2-3 at same time above?
                velocity_modifier[n,m] += normalvariate(0., random_walk_velocity[m])
