class Mars:
    def __init__(self):
        self.name = 'Mars'          # Store the name in the object
        self.atmosphere = 3390        #km above Venus's surface 
        self.mass = 6.41712 * 10^23
        self.volume = 1.63180 * 10^11
        self.density = 3.93410
        self.gravity = 3.71000
        self.temp = 210
        self.sideral_orbit = 686.98000
        self.sideral_rotation = 24.622900
        self.moons = 2
        self.radius = 3389.5         #radius in km
        
        self.core = '30%'            #% of Venus that core takes up
        self.core_FE = '85%'           #% of Core that Iron takes up
        self.core_NI = '5%'            #% of Core that Nickel takes up  
        self.core_S = '10%'              #% of Core that Sulfer takes up 
       
        self.mantle = '70%'          #% of Venus that mantle takes up
        self.mantle_MgO = '22%'      #% of mantle that MgO takes up
        self.mantle_SiO2 = '45%'        #% of mantle that SaO takes up  
        self.mantle_FeO = '18%'         #% of mantle that FeO takes up
        self.mantle_Al2O3 = '5%'          #% of mantle that AlO takes up
        self.mantle_CaO =  '3%'          #% of mantle that CaO takes up
        self.mantle_other = '7%'        #% of mantle that CaO takes up
        
        self.atmosphere_CO2 = '95%'      #% of atmosphere that CO takes up
        self.atmosphere_N = '2.7%'        #% of atmosphere that N takes up
        self.atmosphere_other = '1.6%'    #% of atmosphere that SO, H2O, CO takes up