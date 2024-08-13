- Imports the webbrowser module: This built-in Python module allows you to open web pages in the default web browser.
- Defines a function named get_search_engine_choice: This function is responsible for displaying search engine options to the user and capturing their choice.
- Displays search engine options: These print statements present the user with three options: Google, Bing, and DuckDuckGo, each associated with a number.
- Captures the user's choice: The input function asks the user to enter the number corresponding to their desired search engine. The chosen number is stored in the variable choice and then returned by the function.
- Defines a function named search_web: This function takes two parameters: search_engine (the user's search engine choice) and query (the search keyword).
-Creates a dictionary of search engine URLs: The search_engines dictionary maps the user's choice (as a string) to the corresponding search engine URL. For example, '1' corresponds to Google's search URL.
- Constructs the full URL: The get method retrieves the URL from the search_engines dictionary based on the user's choice. If the choice is invalid, it defaults to Google. The search query is then appended to the URL.
- Opens the constructed URL in the web browser: The webbrowser.open function launches the web page corresponding to the full URL.
- Defines the main function: This is the entry point of the program. It contains the main loop and handles user input.
- Starts an infinite loop: The while True loop keeps the program running until the user decides to exit.

        search = input("Please Enter your keyword (or type 'exit' to quit): ").strip()

- Prompts the user to enter a search keyword: The input function asks the user to provide a search query. The strip method removes any leading or trailing whitespace from the input.

        if search.lower() == 'exit':
            break

- Checks if the user wants to exit: If the user types "exit" (in any case), the program breaks out of the loop, ending the session.
        if not search:
            print("You must enter a keyword to search!")
            continue

- Validates the search input: If the user enters an empty string (or just spaces), the program warns them and goes back to the beginning of the loop without proceeding further.

        choice = get_search_engine_choice()

- Calls the get_search_engine_choice function: The user's choice of search engine is captured and stored in the choice variable.

        search_web(choice, search)

- Calls the search_web function: This function is called with the user's search engine choice and search query, which opens the web page with the search results.

        print(f"Searching for '{search}'...")
- Provides feedback to the user: A message is printed to the console, confirming what the program is searching for.


if __name__ == "__main__":
    main()

    Ensures the script runs only when executed directly: The if __name__ == "__main__": line checks if the script is being run as the main program. If it is, the main function is called to start the program. This is a common Python idiom that prevents certain code from running when the script is imported as a module in another script.