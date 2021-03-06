from bigtwo import *

def play(hand, roundStart, playToBeat, roundHistory, playerNo, handSize, scores, roundNo):
    if len(playToBeat) == 0:
        if roundStart: return ["3D"]
        elif everyfivecard(hand, "straightflush"): return everyfivecard(hand, "straightflush")[0]
        elif everyfivecard(hand, "fourofakind"): return everyfivecard(hand, "fourofakind")[0]
        elif everyfivecard(hand, "fullhouse"): return everyfivecard(hand, "fullhouse")[0]
        elif everyfivecard(hand, "straight"): return everyfivecard(hand, "straight")[0]
        elif everyfivecard(hand, "flush"): return everyfivecard(hand, "flush")[0]
        elif counttriples(hand): return counttriples(hand)[0]
        elif countpairs(hand): return countpairs(hand)[0]
        else: return [sortcards(hand)[0]]
    
    elif len(playToBeat) == 1 and findlegal(hand, playToBeat, 1): return [findlegal(hand, playToBeat, 1)[0]]
    elif len(playToBeat) == 2 and findlegal(hand, playToBeat, 2): return findlegal(hand, playToBeat, 2)[0]
    elif len(playToBeat) == 3 and findlegal(hand, playToBeat, 3): return findlegal(hand, playToBeat, 3)[0]
    elif len(playToBeat) == 5 and findlegal(hand, playToBeat, 5): return findlegal(hand, playToBeat, 5)[0]

    return []

"""
The parameters to this function are:
* `hand`: A list of card strings that are the card(s) in your hand.
* `is_start_of_round`: A Boolean that indicates whether or not the `play` function is being asked to make the first play of a round.
* `play_to_beat`: The current best play of the trick. If no such play exists (you are the first play in the trick), this will be an empty list.
* `round_history`: A list of *trick_history* entries.
A *trick_history* entry is a list of *trick_play* entries.
Each *trick_play* entry is a `(player_no, play)` 2-tuple, where `player_no` is an integer between 0 and 3 (inclusive) indicating which player made the play, and `play` is the play that said player made, which will be a list of card strings.
* `player_no`: An integer between 0 and 3 (inclusive) indicating which player number you are in the game.
* `hand_sizes`: A 4-tuple of integers representing the number of cards each player has in their hand, in player number order. 
* `scores`: A 4-tuple of integers representing the score of each player at the start of this round, in player number order.
* `round_no`: An integer between 0 and 9 (inclusive) indicating which round number is currently being played.

This function should return an empty list (`[]`) to indicate a pass (see "Playing a Round"), or a list of card strings, indicating that you want to play these cards to the table as a valid play.
"""
