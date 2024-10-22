new_game = """
game_data = {
    "map": "[A]--[B]--[C]\n |    |    |\n[D]--[E]--[F]\n |    |    |\n[G]--[H]--[I]",
    "rooms": {
        "A": {"description": "A dimly lit chamber", 
              "exits": {"north": "H", "east": "B", "south": "D"}},
        "B": {"description": "The main hall", 
              "exits": {"north": "F", "east": "C", "west": "A", "south": "E"}},
        "C": {"description": "The eastern chamber",
              "exits": {"north": "K", "west": "B", "south": "G"}},
        "D": {"description": "The southern dungeon",
              "exits": {"north": "A", "east": "E"}},
        "E": {"description": "The central basement",
              "exits": {"north": "B", "east": "G", "west": "D"}},
        "F": {"description": "The upper hall",
              "exits": {"east": "K", "west": "H", "south": "B"}},
        "G": {"description": "The eastern dungeon",
              "exits": {"north": "C", "west": "E"}},
        "H": {"description": "The western tower",
              "exits": {"east": "F", "south": "A"}},
        "K": {"description": "The eastern tower",
              "exits": {"west": "F", "south": "C"}}
    },
    "player": {
        "current_room": "A",
        "inventory": [],
        "health": 100
    },
    "game_state": {
        "visited_rooms": [],
        "enemies_defeated": 0
    }
}"""