import random

def print_board(heap):
    print(f"Current heap: {'|' * heap}")

def get_user_move(heap):
    while True:
        try:
            sticks_to_remove = int(input(f"Enter the number of sticks to remove (minimum 1, maximum {min(heap, heap // 2)}): "))
            if 1 <= sticks_to_remove <= min(heap, heap // 2):
                return sticks_to_remove
            else:
                print(f"Invalid number of sticks. Please enter a number between 1 and {min(heap, heap // 2)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_computer_move(heap):
    xor_sum = heap ^ (heap // 2)
    return 1 if xor_sum == 0 else max(1, min(heap, heap - xor_sum))

def nim_game():
    heap, player_turn = 15, 1

    while heap > 1:
        print_board(heap)
        sticks_to_remove = get_user_move(heap) if player_turn == 1 else get_computer_move(heap)
        heap -= sticks_to_remove
        print(f"{'Player 1' if player_turn == 2 else 'Computer'} removes {sticks_to_remove} sticks.")
        player_turn = 3 - player_turn

    print_board(heap)
    print(f"Player {player_turn} picks the last stick")
    print(f"\n{'Player 1' if player_turn == 2 else 'Computer'} is the winner!")

if __name__ == "__main__":
    nim_game()
