@fast.agent(
    "character-creator",
    servers=["elicitation_forms_server"],
    # Register our handler from game_character_handler.py
    elicitation_handler=game_character_elicitation_handler,
)