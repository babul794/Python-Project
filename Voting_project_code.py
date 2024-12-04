# Define the voting options
options = {
    'color': ['Red', 'Blue', 'Green', 'Yellow', 'Pink'],
    'food': ['Pizza', 'Burger', 'Sushi', 'Pasta', 'Salad'],
    'movie': ['Inception', 'Titanic', 'Avatar', 'The Dark Knight', 'The Godfather']
}

# Function to display voting options
def display_options(category):
    print(f"\nPlease vote for your favorite {category}:")
    for i, option in enumerate(options[category], 1):
        print(f"{i}. {option}")
    print(f"{len(options[category]) + 1}. Exit")

# Function to handle the voting process
def vote(category):
    votes = {option: 0 for option in options[category]}  # Initialize vote count
    while True:
        display_options(category)  # Display voting options
        
        try:
            choice = int(input(f"Enter the number of your favorite {category}: "))
            
            if choice == len(options[category]) + 1:
                print("Exiting the voting system.\n")
                break
            elif 1 <= choice <= len(options[category]):
                # Increment the vote count for the chosen option
                selected_option = options[category][choice - 1]
                votes[selected_option] += 1
                print(f"Your vote for '{selected_option}' has been counted!\n")
            else:
                print("Invalid choice. Please choose a valid option.\n")
        
        except ValueError:
            print("Please enter a valid number.\n")
    
    return votes

# Function to display the voting results
def display_results(category, votes):
    print(f"\nVoting results for {category}:")
    for option, count in votes.items():
        print(f"{option}: {count} vote(s)")

# Main function to control the flow of the program
def main():
    print("Welcome to the Simple Voting System!\n")
    while True:
        print("What would you like to vote for?")
        print("1. Favorite Color")
        print("2. Favorite Food")
        print("3. Favorite Movie")
        print("4. Exit")
        
        try:
            category_choice = int(input("Enter your choice (1-4): "))
            
            if category_choice == 1:
                category = 'color'
            elif category_choice == 2:
                category = 'food'
            elif category_choice == 3:
                category = 'movie'
            elif category_choice == 4:
                print("Thank you for using the Voting System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.\n")
                continue
            
            # Start the voting process for the selected category
            votes = vote(category)
            
            # Display the results after voting
            display_results(category, votes)
        
        except ValueError:
            print("Please enter a valid number.\n")

# Run the program
if __name__ == "__main__":
    main()
