from datetime import datetime
"""
Logs the game result to a file with a timestamp.
this will help track game history and could be useful for future applications such as:
- player statistics
(note to self... if the project evolves, consider adding the logger file to the .gitignore file)
arguments:
    player_name: name of the player
    difficulty: game difficulty (easy, normal, hard)
    esult: game outcome (win, loss, draw)
"""
def log_game(player_name: str, difficulty: str, result: str, depth: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f'{timestamp} | Player: {player_name} | Difficulty: {difficulty} | Depth: {depth} | Result: {result}\n'

        try:
            with open('game_history.log', 'a') as log_file:
                log_file.write(log_entry)
        except IOError as e:
            print(f'Error saving the game... {e}')