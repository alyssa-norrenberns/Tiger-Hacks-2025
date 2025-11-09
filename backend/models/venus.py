class Venus:
      def __init__(self):
        self.name = 'Venus'          # Store the name in the object
        self.atmosphere = 6052          #km above Venus's surface 
        self.mass = 4.86747 * 10^24
        self.volume = 9.28430 * 10^11
        self.density = 5.24300
        self.gravity = 38.87000
        self.temp = 737
        self.sideral_orbit = 224.70100
        self.sideral_rotation = -5832.50000
        self.moons = 0
        self.radius = 6051             #radius in km
        
        self.core = '30%'            #% of Venus that core takes up
        self.core_FE = '80%'           #% of Core that Iron takes up
        self.core_NI = '5%'            #% of Core that Nickel takes up  
        self.core_S = '5%'              #% of Core that Sulfer takes up 
        self.core_Si = '10%'             #% of Core that Silicon takes up 
        
        self.mantle = '70%'          #% of Venus that mantle takes up
        self.mantle_MgO = '22%'      #% of mantle that MgO takes up
        self.mantle_SiO2 = '45%'        #% of mantle that SaO takes up  
        self.mantle_FeO = '9%'         #% of mantle that FeO takes up
        self.mantle_Al2O3 = '3%'          #% of mantle that AlO takes up
        self.mantle_CaO =  '3%'          #% of mantle that CaO takes up
        
        self.atmosphere_CO2 = '96%'      #% of atmosphere that CO takes up
        self.atmosphere_N = '3%'        #% of atmosphere that N takes up
        self.atmosphere_other = '1%'    #% of atmosphere that SO, H2O, CO takes up