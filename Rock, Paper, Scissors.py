import random

options = ("🪨", "📄", "✂️")

while True:
    print("\n============== ' Rock Paper Scissors ' ==============")
    print("1) '🪨' 2) '📄' 3) '✂️'")

    player_choice_input = input("Pick a number:")

    player = None
    computer = random.choice(options)

    if player_choice_input == '1':
        player = "🪨"
    elif player_choice_input == '2':
        player = "📄"
    elif player_choice_input == '3':
        player = "✂️"

    if player is None:
        print("Input tidak valid. Harap pilih 1, 2, atau 3.")
        continue
    
    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("Hasil: Seri!")
    elif (player == "🪨" and computer == "✂️") or \
         (player == "📄" and computer == "🪨") or \
         (player == "✂️" and computer == "📄"):
        print("Hasil: Kamu Menang!")
    else:
        print("Hasil: Kamu Kalah!")

    play_again = input("\nMain lagi? (y/n): ").lower()
    if play_again != "y":
        break

print("\nTerima kasih sudah bermain!")