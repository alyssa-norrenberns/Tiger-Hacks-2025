class Saturn:
    def __init__(self):
        self.name = 'Saturn'          # Store the name in the object
        self.atmosphere = 36184      #km above Saturn's surface 
        self.mass = 5.68336 * 10^26
        self.volume = 8.27130 * 10^14
        self.density = 0.68710
        self.gravity = 10.44000
        self.temp = 134
        self.sideral_orbit = 10759.22000
        self.sideral_rotation = 10.65600
        self.moons = 274
        self.radius = 36185        #radius in km
        
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
        
        
        