import os
import random
import matplotlib.pyplot as plt
import numpy as np

# Function to generate a random force (magnitude, direction), restricting to horizontal or vertical directions
def random_force():
    magnitude = random.randint(1, 10)  # Random magnitude between 1 and 10 newtons
    direction = random.choice([90, 270])  # Only horizontal or vertical directions
    return magnitude, direction

# Generate cards with exactly 2 forces and no resultant force shown
def generate_cards(num_cards):
    cards = []
    for _ in range(num_cards):
        forces = [random_force() for _ in range(2)]  # Exactly 2 forces per card
        cards.append(forces)
    return cards

# Function to plot the forces on a card
def plot_card(forces, card_number, save_directory):
    fig, ax = plt.subplots()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    origin = [0], [0]  # Start all vectors from the origin

    for i, force in enumerate(forces):
        magnitude, direction = force
        color = 'blue' if i == 0 else 'green'  # Use different colors for each force
        ax.quiver(*origin, magnitude * np.cos(np.radians(direction)), 
                  magnitude * np.sin(np.radians(direction)), 
                  angles='xy', scale_units='xy', scale=1, color=color)
        
        # Add text showing the magnitude of the force (in Newtons) next to the vector
        text_x = magnitude * np.cos(np.radians(direction)) + (1 if direction in [0, 180] else 0)
        text_y = magnitude * np.sin(np.radians(direction)) + (1 if direction in [90, 270] else 0)
        ax.text(text_x, text_y, f'{magnitude}N', fontsize=12, color=color)

    plt.title(f'Card {card_number}')
    plt.grid(True)
    
    # Save the figure to the specified directory
    plt.savefig(os.path.join(save_directory, f'card_{card_number}.png'))
    plt.close()

# Generate and save cards
def save_game_cards(num_cards, save_directory):
    # Create directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    cards = generate_cards(num_cards)
    for i, forces in enumerate(cards):
        plot_card(forces, i+1, save_directory)
    return cards

# Directory where cards will be saved
save_directory = r'C:\Users\Anna\Documents\SAIL\Informatics\Python programming\UNO'

# Generate 20 cards for a game of 4 people
cards = save_game_cards(20, save_directory)
print(f'Generated {len(cards)} cards for the game. Cards saved in {save_directory}')

# Example card output (forces on each card)
for i, card in enumerate(cards):
    print(f'Card {i+1}: Forces = {card[0][0]}N @ {card[0][1]}°, {card[1][0]}N @ {card[1][1]}°')
