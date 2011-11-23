class CreeperObject:
    def __init__(self, name, data, world, owner, team):
        self.is_packet = False
        self.is_moveable = False
        self.is_emitter = False
        self.is_producer = False
        self.data = {}
        self.world = world
        self.owner = owner
        self.team = team
        
    def becomePacket(self, packet_data):
        self.is_packet = True
        
        return
    
    # requires is for stuff like ore rigs that must be adjacent to an ore block
    def becomeProducer(self, production_data, requires=None):
        self.is_producer = True
        self.production_data = production_data
        self.requires = requires
        return
    
    # Emitter types: 'energy', 'missile', 'laser', 'floater', 'phantom', 'creep'
    def becomeEmitter(self, emitter_type):
        return
    
    def update(self, dt, orders=None):
        return
