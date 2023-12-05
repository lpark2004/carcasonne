import random  
from typing import Optional  
  
from wingedsheep.carcassonne.carcassonne_game import CarcassonneGame  
from wingedsheep.carcassonne.carcassonne_game_state import CarcassonneGameState  
from wingedsheep.carcassonne.objects.actions.action import Action  
from wingedsheep.carcassonne.tile_sets.supplementary_rules import SupplementaryRule  
from wingedsheep.carcassonne.tile_sets.tile_sets import TileSet  
   
game = CarcassonneGame(  
	players=2,  
	tile_sets=[TileSet.BASE, TileSet.THE_RIVER, TileSet.INNS_AND_CATHEDRALS],  
	supplementary_rules=[SupplementaryRule.ABBOTS, SupplementaryRule.FARMERS]  
)  
  
def random(game: CarcassonneGame):  
    return random.choice(game.get_possible_actions())
