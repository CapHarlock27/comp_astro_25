import numpy as np 
import batman
import matplotlib.pyplot as plt




class TransitModel:

    def __init__(self):
        
        # self.params = batman.TransitParams()
        # self.params.t0 = params_dict.get("t0", 0.0)                                         #time of inferior conjunction
        # self.params.per = params_dict.get("per", 32.939623)                                 #orbital period
        # self.params.rp = params_dict.get("rp", 0.0212)                                      #planet radius (in units of stellar radii)
        # self.params.a = params_dict.get("a", 30.73)                                         #semi-major axis (in units of stellar radii)
        # self.params.inc = params_dict.get("inc", 89.5785)                                   #orbital inclination (in degrees)
        # self.params.ecc = params_dict.get("ecc", 0.2)                                       #eccentricity
        # self.params.w = params_dict.get("w", 354.3)                                         #longitude of periastron (in degrees)
        # self.params.u = params_dict.get("[u1, u2]", [0.391617, 0.019183])                   #limb darkening coefficients [u1, u2]
        # self.params.limb_dark = params_dict.get("limb darkening model", "quadratic")        #limb darkening model
        self.name = "K2-18_b"
        self.params = batman.TransitParams()
        self.params.t0 = 0.                       #time of inferior conjunction
        self.params.per = 32.939623                     #orbital period
        self.params.rp = 0.0212                       #planet radius (in units of stellar radii)
        self.params.a = 30.73                       #semi-major axis (in units of stellar radii)
        self.params.inc = 89.5785                    #orbital inclination (in degrees)
        self.params.ecc = 0.2                      #eccentricity
        self.params.w = 354.3                       #longitude of periastron (in degrees)
        self.params.u = [0.391617, 0.019183]                #limb darkening coefficients [u1, u2]
        self.params.limb_dark = "quadratic"       #limb darkening model

    def plot(self):
        t = np.linspace(-0.5, 0.5, 100)
        m = batman.TransitModel(self.params, t)    #initializes model
        flux = m.light_curve(self.params)          #calculates light curve
        plt.plot(t, flux)
        plt.xlabel("Time from central transit")
        plt.ylabel("Relative flux")
        plt.title(f"Light curve of {self.name}")
        plt.grid()
        plt.tight_layout()
        plt.savefig("K2-18_b_assignment1_taskF.png")