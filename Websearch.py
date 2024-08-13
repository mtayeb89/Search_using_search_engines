'''import webbrowser
search=input("Please Enter your keyword: ")
webbrowser.open("https://www.google.com/search?q=" + search)'''

# Import the webbrowser module to open web pages in the default browser
import webbrowser


# Function to display search engine options and get the user's choice
def get_search_engine_choice():
    # Display search engine choices to the user
    print("Choose a search engine:")
    print("1. Google")
    print("2. Bing")
    print("3. DuckDuckGo")

    # Get the user's choice of search engine
    choice = input("Enter the number of your choice: ")
    # Return the user's choice
    return choice


# Function to perform the web search based on the user's input
def search_web(search_engine, query):
    # Dictionary to map the user's choice to the corresponding search engine URL
    search_engines = {
        '1': "https://www.google.com/search?q=",
        '2': "https://www.bing.com/search?q=",
        '3': "https://duckduckgo.com/?q="
    }
    # Construct the full URL by appending the query to the chosen search engine URL
    url = search_engines.get(search_engine, "https://www.google.com/search?q=") + query
    # Open the constructed URL in the web browser
    webbrowser.open(url)


# Main function to handle user input and control the flow of the program
def main():
    # Start an infinite loop to allow multiple searches
    while True:
        # Prompt the user to enter a search keyword or exit the program
        search = input("Please Enter your keyword (or type 'exit' to quit): ").strip()

        # Check if the user wants to exit the program
        if search.lower() == 'exit':
            # Exit the loop and end the program
            break

        # Validate that the user entered a non-empty search query
        if not search:
            # Warn the user if the input is empty and continue the loop
            print("You must enter a keyword to search!")
            continue

        # Get the user's choice of search engine
        choice = get_search_engine_choice()
        # Perform the search with the selected engine and query
        search_web(choice, search)

        # Provide feedback to the user that the search is being performed
        print(f"Searching for '{search}'...")


# Entry point of the script: call the main function if this file is executed directly
if __name__ == "__main__":
    main()

