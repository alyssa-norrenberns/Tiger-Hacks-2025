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
class Jupiter:
    def __init__(self):
        self.name = 'Jupiter'          # Store the name in the object
        self.atmosphere = 71492          #km above Venus's surface 
        self.mass = 1.89819 * 10^27
        self.volume = 1.43128 * 10^15
        self.density = 1.32620
        self.gravity = 1.32620
        self.temp = 165
        self.sideral_orbit = 4332.58900
        self.sideral_rotation = -9.92500
        self.moons = 95
        self.radius = 71492            #radius in km
        
        self.core = '15%'            #% of Jupiter that core takes up
        self.core_Silicates = '45%'           #% of Core that Silicates (SiO₂, Mg₂SiO₄) takes up
        self.core_Metals = '30%'            #% of Core that Metals (Fe, Ni) takes up  
        self.core_Ices = '25%'              #% of Core that Ices (H₂O, NH₃, CH₄) takes up 
        
        self.metallic = '75%'          #% of Jupiter that metallic takes up
        self.metallic_hydrogen = '85%'      #% of mantle that hydrogen takes up
        self.metallic_helium = '14%'        #% of mantle that helium takes up  
        self.metallic_other = '1%'         #% of mantle that O, C, N, S takes up
        
        self.envelope = '10%'      #% of atmosphere that the envelope takes up
        self.envelope_H = '89%'        #% of atmosphere that H takes up
        self.envelope_other = '1%'    #% of atmosphere that CH₄, NH₃, H₂O, PH₃ takes up
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
class Mercury:
    def __init__(self):
        self.name = 'Mercury'          # Store the name in the object
        self.atmosphere = 4879            #km above Mercury's surface (traces of Na, K, He, H, O)
        self.mass = 3.30114 * 10^23
        self.volume = 6.083 * 10^10
        self.density = 5.4291
        self.gravity = 3.7
        self.temp = 440
        self.sideral_orbit = 87.969
        self.sideral_rotation = 1407.6
        self.moons = 0
        self.radius = 2440              #radius in km
        
        self.core = '70%'            #% of Mercury that core takes up
        self.core_FE = '60%'           #% of Core that Iron takes up
        self.core_NI = '4%'            #% of Core that Nickel takes up  
        self.core_S = '4%'              #% of Core that Sulfer takes up 
        self.core_Si = '4%'             #% of Core that Silicon takes up 
        
        self.mantle = '30%'          #% of Mercury that mantle takes up
        self.mantle_MgO = '22%'      #% of mantle that MgO takes up
        self.mantle_SiO = '25%'        #% of mantle that SiO takes up  
        self.mantle_CaO = '5%'         #% of mantle that CaO takes up
        self.mantle_AlO = '5%'          #% of mantle that AlO takes up
        self.mantle_FeO =  '3%'          #% of mantle that FeO takes up
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
class Saturn:
    def __init__(self):
        self.name = 'Saturn'          # Store the name in the object
        self.atmosphere = 3390        #km above Saturn's surface 
        self.mass = 6.41712 * 10^23
        self.volume = 1.63180 * 10^11
        self.density = 3.93410
        self.gravity = 3.71000
        self.temp = 210
        self.sideral_orbit = 686.98000
        self.sideral_rotation = 24.622900
        self.moons = 2
        self.radius = 3389.5         #radius in km
        
        self.core = '10%'            #% of Saturn that core takes up
        self.core_Silicates = '50%'           #% of Core that Silicates (SiO₂, Mg₂SiO₄) takes up
        self.core_Metals = '25%'            #% of Core that Metals (Fe, Ni): takes up  
        self.core_Ices = '25%'              #% of Core that Ices (H₂O, CH₄, NH₃) takes up 
       
        self.metallic = '50%'          #% of Saturn that Metallic hydrogen laye takes up
        self.metalic.hydrogen = '80%'      #% of Metallic hydrogen layer that metalic hydrogen takes up
        self.metallic.helium = '19%'        #% of Metallic hydrogen layer that SaO takes up  
        self.metallic.other = '1%'         #% of Metallic hydrogen layer that other materials takes up
        
        
        self.molecular = '40%'      #% of Saturn that Molecular hydrogen/helium envelope takes up
        self.molecular.H = '96%'        #% of Molecular hydrogen/helium envelope that H takes up
        self.molecular.He = '3%'    #% of Molecular hydrogen/helium envelope that He takes up
        self.molecular.other = '1%'    #% of Molecular hydrogen/helium envelope that CH₄, NH₃, PH₃, H₂O takes up
        
        self.atmosphere.H = '96%'       #% of the atmosphere that H takes up
        self.atmosphere.He = '3%'       #% of the atmosphere that He takes up
        self.atmosphere.other = '1%'       #% of the atmosphere that CH₄, NH₃, H₂O takes up
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