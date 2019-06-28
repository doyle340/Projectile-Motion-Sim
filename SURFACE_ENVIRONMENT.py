class SURFACE_ENVIRONMENT():
    """
    Class Contains the definitions for  surface environment 
     
    Parameters
    ----------
    hostMass: float 
        The mass in kg of the surface body mass
    isFric: string
        Must be either 'True' or 'False'.
        If true, the environment has some non-zero frictional coefficient.
        If false, there is no surface friction, hostFricCo = 0        
    hostFricCo: float
        The frictional coefficient of the host body's surface
    isGrav: string
        Must be either 'True' or 'False'.
        If true, there is some non-zero gravity.
        If false, there is no gravity, gravCon = 0
    gravCon: float 
        The gravitational acceleration constant
	isDrag: string
        Must be either 'True' or 'False'.
        If true, there is some non-zero drag.
        If false, there is no drag		

    """
    def __init__(self, hostMass, isFric, hostFricCo, isGrav, gravCon
                ):
        self.hostMass = hostMass
        self.isFric = isFric
        self.hostFricCo = hostFricCo
        self.isGrav = isGrav
        self.gravCon = gravCon
		self.isDrag = isDrag