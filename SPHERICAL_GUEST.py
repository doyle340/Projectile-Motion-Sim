class SPHERICAL_GUEST():
	"""
	Class contains the definitions of spherical object.
	Libraries needed: 
		numpy imported as np
	
    Parameters
    ----------
	guestMass: float
		Mass of the guest object
	guestRadius: float
		Radius of the guest object
	
	Methods
	-------
	guestDensity(guestMass, guestRadius)
		Returns the density of the guest object
		given the mass and radius
	"""
    def __init__(self, guestMass, guestRadius):
        self.guestMass = guestMass
		self.guestRadius = guestRadius
	
	def guestDensity(self, guestMass, guestRadius):
		"""
		This function returns the density of the guest object.
		D = M/V (Density: D, Mass: M,Volume: V)
		Volume of a Sphere: (4/3)*PI*R^3 (Radius: R)
        guestDensity = guestMass / ((4/3)*PI*guestRadius^3)
        Returns
        -------
        guestDensity
        """
		guestDensity = guestMass / ((4.0/3.0)*np.pi*guestRadius**3)
		
		return guestDensity