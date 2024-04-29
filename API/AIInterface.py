# AIInterface.py

class AIInterface:
    def __init__(self, language_model_api):
        self.language_model_api = language_model_api

    def query_language_model(self, user_input):
        # Query the language model API with the user input
        response = self.language_model_api.query(user_input)
        return response

    def process_response(self, response):
        # Process the response from the language model API
        processed_response = self.language_model_api.process_response(response)
        return processed_response

# Example usage
if __name__ == "__main__":
    # Initialize the AIInterface with a specific language model API
    ai_interface = AIInterface(language_model_api)

    # Query the language model API
    user_input = "How do I sort a list of numbers in Python?"
    response = ai_interface.query_language_model(user_input)

    # Process the response
    processed_response = ai_interface.process_response(response)
