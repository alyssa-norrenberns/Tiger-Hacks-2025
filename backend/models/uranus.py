class Uranus:
    def __init__(self):
        self.name = 'Uranus'          # Store the name in the object
        self.atmosphere = 15760      #km above Uranus's surface 
        self.mass = 8.68127 * 10^25
        self.volume = 6.83300 * 10^13
        self.density = 1.27000
        self.gravity = 38.87000
        self.temp = 76
        self.sideral_orbit = 30685.40000
        self.sideral_rotation = -17.24000
        self.moons = 2
        self.radius = 15759        #radius in km
        
        self.core = '15%'            #% of Uranus that core takes up
        self.core_Silicates = '55%'           #% of Core that SiO₂, Mg₂SiO₄ takes up
        self.core_Metals = '20%'            #% of Core that Fe and Ni takes up  
        self.core_Ices = '25%'              #% of Core that H₂O, CH₄, NH₃ takes up 
       
        self.ice_mantle = '60%'          #% of Uranus that ice mantle takes up
        self.ice_mantle_H2O = '55%'      #% of ice mantle that H2O takes up
        self.ice_mantle_NH3 = '25%'        #% of ice mantle that NH3 takes up  
        self.ice_mantle_Ch4 = '20%'         #% of ice mantle that Ch4 takes up
        
        self.envelope = '25%'      #% of Uranus that envelope takes up
        self.envelope_H2 = '82%'        #% of envelope that H2 takes up
        self.envelope_He = '15%'    #% of envelope that He takes up
        self.envelope_CH4 = '3%'    #% of envelope that Ch4 takes up
        
        self.atmosphere_H2 = '82%'      #% of Uranus that atmosphere takes up
        self.atmosphere_He = '15%'        #% of atmosphere that H2 takes up
        self.envelope_Ch4 = '2%'    #% of atmosphere that Ch4 takes up
        self.envelope_other = '1%'    #% of atmosphere that C₂H₂ and C₂H₆ takes up