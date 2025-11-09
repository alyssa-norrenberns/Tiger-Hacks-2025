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