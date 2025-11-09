class Neptune:
    def __init__(self):
        self.name = 'Neptune'          # Store the name in the object
        self.atmosphere = 36184      #km above Neptune's surface 
        self.mass = 1.02413 * 10^26
        self.volume = 6.25400 * 10^13
        self.density = 1.63800
        self.gravity = 11.15000
        self.temp = 55
        self.sideral_orbit = 60189.00000
        self.sideral_rotation = 16.11000
        self.moons = 16
        self.radius = 36185        #radius in km
        
        self.core = '10%'            #% of Neptune that core takes up
        self.core_Silicates = '50%'           #% of Core that Silicates (SiO₂, Mg₂SiO₄) takes up
        self.core_Metals = '25%'            #% of Core that Metals (Fe, Ni): takes up  
        self.core_Ices = '25%'              #% of Core that Ices (H₂O, CH₄, NH₃) takes up 
       
        self.ice_mantle = '60%'          #% of Neptune that ice mantle layer takes up
        self.ice_mantle_H2O = '60%'      #% of ice mantle that H2O takes up
        self.ice_mantle_NH3 = '25%'        #% of ice mantle that NH3 takes up  
        self.ice_mantle_CH4 = '15%'         #% of ice mantle that CH4 takes up
        
        
        self.envelope = '20%'      #% of Neptune that Molecular hydrogen/helium envelope takes up
        self.envelope_H2 = '80%'        #% of Molecular hydrogen/helium envelope that H2 takes up
        self.envelope_He = '19%'    #% of Molecular hydrogen/helium envelope that He takes up
        self.envelope_other = '1%'    #% of Molecular hydrogen/helium envelope that CH₄, CO, C₂H₂, C₂H₆ takes up
        
        self.atmosphere_H = '80%'       #% of the atmosphere that H takes up
        self.atmosphere_He = '19%'       #% of the atmosphere that He takes up
        self.atmosphere_Ch4 = '1%'       #% of the atmosphere that CH₄, NH₃, H₂O takes up