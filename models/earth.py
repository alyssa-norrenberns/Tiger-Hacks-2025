class Earth:
    def __init__(self):
        self.name = 'Earth'          # Store the name in the object
        self.atmosphere = 6371           #km above Earth's surface (traces of Na, K, He, H, O)
        self.mass = 5.97237 * 10^24
        self.volume = 1.08321 * 10^12
        self.density = 5.51360
        self.gravity = 9.80000
        self.temp = 288
        self.sideral_orbit = 365.25600
        self.sideral_rotation = 23.93450
        self.moons = 1
        self.radius = 6371             #radius in km
        
        self.inner_core = '1.7%'            #% of Earth that core takes up
        self.inner_core_FE = '80%'           #% of inner Core that Iron takes up
        self.inner_core_NI = '10%'            #% of inner Core that Nickel takes up  
        self.inner_core_Other = '10%'              #% of inner Core that other elements take up 
        
        self.outer_core = '30%'            #% of Earth that core takes up
        self.outer_core_FE = '85%'           #% of outer Core that Iron takes up
        self.outer_core_NI = '5%'            #% of outer Core that Nickel takes up  
        self.outer_core_Other = '10%'              #% of outer Core that S/Si/O takes up 
        
        self.mantle = '67%'          #% of Earth's mass that mantle takes up
        self.mantle_MgO = '36%'      #% of mantle that MgO takes up
        self.mantle_SiO = '45%'        #% of mantle that SiO takes up  
        self.mantle_CaO = '3%'         #% of mantle that CaO takes up
        self.mantle_AlO = '4%'          #% of mantle that AlO takes up
        self.mantle_FeO = '8%'          #% of mantle that FeO takes up
        
        self.crust = '1%'          #% of Earth's mass that crust takes up
        self.crust_MgO = '5%'      #% of crust that MgO takes up
        self.crust_SiO = '60%'        #% of crust that SiO takes up  
        self.crust_CaO = '6%'         #% of crust that CaO takes up
        self.crust_AlO = '15%'          #% of crust that AlO takes up
        self.crust_FeO = '5%'          #% of crust that FeO takes up
        self.crust_Other = '9%'
        
        self.atmosphere_N = '78%'          #% of Earth's mass that mantle takes up
        self.atmosphere_O2 = '21%'      #% of mantle that o2 takes up
        self.atmosphere_Ar = '.93%'        #% of mantle that Ar takes up  
        self.atmosphere_CO2 = '.04%'         #% of mantle that CO2 takes up
    
        
        