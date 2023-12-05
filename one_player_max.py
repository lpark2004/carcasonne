import random  
import copy
from typing import Optional  
  
from wingedsheep.carcassonne.carcassonne_game import CarcassonneGame  
from wingedsheep.carcassonne.carcassonne_game_state import CarcassonneGameState  
from wingedsheep.carcassonne.objects.actions.action import Action  
from wingedsheep.carcassonne.tile_sets.supplementary_rules import SupplementaryRule  
from wingedsheep.carcassonne.tile_sets.tile_sets import TileSet  
from wingedsheep.carcassonne.utils.points_collector import PointsCollector
from wingedsheep.carcassonne.utils.state_updater import StateUpdater
from wingedsheep.carcassonne.objects.actions.pass_action import PassAction
   
def max_heuristic(game:CarcassonneGame, heuristic):    
    max_score = float('-inf')
    best_action = random.choice(game.get_possible_actions())

    for action in game.get_possible_actions():
        new_game_state = StateUpdater.apply_action(game.state, action)
        score = heuristic(new_game_state, action)
        if score != None:
            if score > max_score:
                max_score = score
                best_action = action
    return best_action

def heuristic(game_state: CarcassonneGameState, action):
    score = 0
    # reward holding meeples

    # penalize placing mepples

    # 
    pass

def max(game: CarcassonneGame):

    best_action = random.choice(game.get_possible_actions())
    new_game_state = StateUpdater.apply_action(game.state, best_action)
    final_scores = PointsCollector.count_final_scores(new_game_state)
    if final_scores:
        score =  PointsCollector.count_final_scores(new_game_state) + new_game_state.scores[0]
    else:
        score = new_game_state.scores[0]
    max_score = score

    for action in game.get_possible_actions():
        new_game_state = StateUpdater.apply_action(game.state, action)
        final_scores = PointsCollector.count_final_scores(new_game_state)
        if final_scores:
            score =  PointsCollector.count_final_scores(new_game_state) + new_game_state.scores[0]   
        else:
            score = new_game_state.scores[0]
        if score != None:
            if score > max_score:
                max_score = score
                best_action = action
    return best_action

def max_heuristic(game: CarcassonneGame):

    best_action = random.choice(game.get_possible_actions())
    new_game_state = StateUpdater.apply_action(game.state, best_action)
    final_scores = PointsCollector.count_final_scores(new_game_state)
    if final_scores:
        score =  PointsCollector.count_final_scores(new_game_state) + new_game_state.scores[0] + 2 * new_game_state.meeples[0] 
    else:
        score = new_game_state.scores[0] + 2 * new_game_state.meeples[0]
    max_score = score

    for action in game.get_possible_actions():
        new_game_state = StateUpdater.apply_action(game.state, action)
        final_scores = PointsCollector.count_final_scores(new_game_state)
        if final_scores:
            score =  PointsCollector.count_final_scores(new_game_state) + new_game_state.scores[0] + 2 * new_game_state.meeples[0]
        else:
            score = new_game_state.scores[0] + 2 * new_game_state.meeples[0]
        if score != None:
            if score > max_score:
                max_score = score
                best_action = action
    return best_action

def max_baseline(game: CarcassonneGame):

    best_action = random.choice(game.get_possible_actions())
    new_game_state = StateUpdater.apply_action(game.state, best_action)
    max_score = new_game_state.scores[0]

    for action in game.get_possible_actions():
        new_game_state = StateUpdater.apply_action(game.state, action)
        final_scores = PointsCollector.count_final_scores(new_game_state)
        if final_scores:
            score =  PointsCollector.count_final_scores(new_game_state) + new_game_state.scores[0]   
        else:
            score = new_game_state.scores[0]
        if score != None:
            if score > max_score:
                max_score = score
                best_action = action
    return best_action

def random_policy(game: CarcassonneGame):  
    return random.choice(game.get_possible_actions())        
        
def evaluate(policy):
    game = CarcassonneGame(  
	players=1,  
	tile_sets=[TileSet.BASE],  
	supplementary_rules=[]  
    )  
    counter = 0
    while not game.is_finished():  
        player: int = game.get_current_player()

        if len(game.get_possible_actions()) != 0:  
            best_action = policy(game)
            game.step(player, best_action)
        #game.render() 
    return game.state.scores[0]

def test_policy(policy, num_iters):
    average_baseline = 0
    list_scores = []
    for i in range(num_iters):
        average_baseline += evaluate(policy)
        print(average_baseline)
    print(average_baseline / num_iters)
    print(list_scores)


test_policy(random_policy, 10)







# test_policy(max, 10) # 148
# test_policy(random_policy, 10) # 32.1
# test_policy(max_baseline, 10) # 125.9
#test_policy(max_heuristic, 10) # 153.7


  

