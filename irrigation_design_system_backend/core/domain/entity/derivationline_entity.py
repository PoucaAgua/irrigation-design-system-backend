from decimal import Decimal
from dataclasses import dataclass

@dataclass
class DerivationlineEntity:
  friction_factor: Decimal
  flow: Decimal                    
  load_loss: Decimal                
  pipe_length: Decimal              