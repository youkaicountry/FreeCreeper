class CreeperObject:
    def __init__(self, data, world, owner, team):
        self.is_packet = False
        self.is_moveable = False
        self.is_emitter = False
        self.is_producer = False
        self.data = {}
        self.world = world
        self.owner = owner
        self.team = team
        
    def becomePacket(self, packet_data, path=None):
        self.is_packet = True
        self.packet_data = packet_data
        self.path = path
        return
    
    # requires is for stuff like ore rigs that must be adjacent to an ore block
    def becomeProducer(self, production_data, requires=None):
        self.is_producer = True
        self.production_data = production_data
        self.requires = requires
        return
    
    # Emitter types: 'energy', 'missile', 'laser', 'floater', 'phantom', 'creep'
    #emitter data is the stuff that is consumed when emitting
    def becomeEmitter(self, emitter_type, emitter_data, self.emitter_speed):
        self.is_emitter = True
        self.emitter_type = emitter_type
        self.emitter_data
        self.emitter_speed = emitter_speed
        self.emission_counter = 0
        return
    
    def update(self, dt, orders=None):
        # EMITTER LOGIC
        if self.is_emitter:
            self.emission_counter += dt
            if self.emission_counter >= self.emission_speed:
                #handle emission
                #if can emit to something, then set ready = True
                # Check that the object has the required stuff to emit
                ready = all([self.data[x] >= self.emission_data[x] for x in self.emission_data])
                # If this is an energy emitter, check that something is requesting energy
                if self.emitter_type == 'energy':
                    ene = world.getNextEnergyRequest(owner, team)
                    ready = ene is not None
                if ready:
                    # Set the counter back to 0
                    self.emission_counter = 0
                    # Remove the materials
                    for k in self.emission_data:
                        self.data[k] -= self.emission_data[k]
                    #Make object, and add it to the world
                        if self.emitter_type == 'energy':
                            o = CreeperObject()
                    world.addObject(owner, team, o, False)
        return

class World:
    def __init__(self):
        return
    
    def addObject(self, owner, team, obj, base=False):
        return
