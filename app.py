import streamlit as st
import random

# Initialize game state
if 'positions' not in st.session_state:
    st.session_state.positions = [0, 0, 0, 0]  # For 4 players
    st.session_state.game_over = False

def roll_dice():
    return random.randint(1, 6)

def move_player(player_index, steps):
    st.session_state.positions[player_index] += steps
    if st.session_state.positions[player_index] >= 29:  # Assuming 30 positions (0 to 29)
        st.session_state.positions[player_index] = 29
        st.session_state.game_over = True

st.title("Ludo Game")

# Player selection
num_players = st.sidebar.slider("Number of Players", 2, 4, 2)

if st.button("Roll Dice"):
    if st.session_state.game_over:
        st.warning("Game Over! Reset to play again.")
    else:
        for player_index in range(num_players):
            dice_roll = roll_dice()
            st.write(f"Player {player_index + 1} rolled a {dice_roll}.")
            move_player(player_index, dice_roll)
            st.write(f"Player {player_index + 1} is at position {st.session_state.positions[player_index]}.")

if st.session_state.game_over:
    st.success("Game Over! Restarting...")
    st.session_state.positions = [0] * 4
    st.session_state.game_over = False
