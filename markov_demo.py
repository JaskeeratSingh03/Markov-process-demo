import numpy as np

def explain_markov():
    print("Welcome to the Markov Process Demonstration!")
    print("------------------------------------------------")
    print("A Markov process is a sequence of states where the probability")
    print("of moving to the next state depends ONLY on the current state,")
    print("not on the history of past states.")
    print("\nWe represent this with a transition matrix P where:")
    print("- Rows = current states")
    print("- Columns = next states")
    print("- P[i][j] = probability of moving from state i to state j\n")

def get_user_input():
    n = int(input("Enter the number of states in your Markov process: "))
    print(f"\nGreat! You have {n} states.")
    print("Now enter the transition matrix row by row (each row should sum to 1).")
    
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if abs(sum(row) - 1.0) > 1e-6:
            print("⚠️ Warning: Row probabilities don’t sum to 1. Adjusting automatically.")
            row = [x/sum(row) for x in row]
        matrix.append(row)
    
    return np.array(matrix)

def simulate_markov(P, steps=5):
    n = P.shape[0]
    current_state = int(input(f"\nEnter the starting state (0 to {n-1}): "))
    print(f"\nStarting simulation for {steps} steps...\n")
    
    for step in range(steps):
        print(f"Step {step}: State {current_state}")
        current_state = np.random.choice(range(n), p=P[current_state])
    print(f"Step {steps}: State {current_state}")

if __name__ == "__main__":
    explain_markov()
    P = get_user_input()
    simulate_markov(P)
