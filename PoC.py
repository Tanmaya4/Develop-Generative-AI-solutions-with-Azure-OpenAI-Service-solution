import os
from dotenv import load_dotenv
import utils
from openai import AzureOpenAI  # Import AzureOpenAI

def main(): 
    try:
        load_dotenv()
        utils.initLogFile()
        
        # Load environment variables
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_model = os.getenv("AZURE_OAI_MODEL")
        
        # Define Azure OpenAI client
        client = AzureOpenAI(
            azure_endpoint=azure_oai_endpoint, 
            api_key=azure_oai_key,  
            api_version="2024-02-15-preview"  # Adjust to your required API version
        )

        function_map = {
            "1": function1,
            "2": function2,
            "3": function3,
            "4": function4
        }

        while True:
            print('1: Validate PoC\n' +
                  '2: Company chatbot\n' +
                  '3: Developer tasks\n' +
                  '4: Use company data\n' +
                  '\'quit\' to exit the program\n')
            command = input('Enter a number:')
            if command.strip() in function_map:
                function_map[command](client, azure_oai_model)
            elif command.strip().lower() == 'quit':
                print('Exiting program...')
                break
            else:
                print("Invalid input. Please enter number 1, 2, 3, or 4.")

    except Exception as ex:
        print(ex)


# Task 1: Validate PoC
def function1(aiClient, aiModel):
    inputText = utils.getPromptInput("Task 1: Validate PoC", "sample-text.txt")
    
    # Build messages to send to Azure OpenAI model
    messages = [
        {"role": "user", "content": inputText}
    ]
    
    # Define argument list
    apiParams = {
        "messages": messages,
    }
    
    utils.writeLog("API Parameters:\n", apiParams)

    # Call chat completion connection
    response = aiClient.chat.completions.create(
        model=aiModel,
        **apiParams
    )
    
    utils.writeLog("Response:\n", str(response))
    print("Response: " + response.choices[0].message.content + "\n")
    return response


# Task 2: Company chatbot
def function2(aiClient, aiModel):
    inputText = utils.getPromptInput("Task 2: Company chatbot", "sample-text.txt")
    
    messages = [
        {"role": "user", "content": inputText}
    ]
    
    apiParams = {
        "messages": messages,
    }
    
    utils.writeLog("API Parameters:\n", apiParams)

    response = aiClient.chat.completions.create(
        model=aiModel,
        **apiParams
    )
    
    utils.writeLog("Response:\n", str(response))
    print("Response: " + response.choices[0].message.content + "\n")
    return response


# Task 3: Developer tasks
def function3(aiClient, aiModel):
    inputText = utils.getPromptInput("Task 3: Developer tasks", "sample-text.txt")
    
    messages = [
        {"role": "user", "content": inputText}
    ]
    
    apiParams = {
        "messages": messages,
    }
    
    utils.writeLog("API Parameters:\n", apiParams)

    response = aiClient.chat.completions.create(
        model=aiModel,
        **apiParams
    )
    
    utils.writeLog("Response:\n", str(response))
    print("Response: " + response.choices[0].message.content + "\n")
    return response 


# Task 4: Use company data
def function4(aiClient, aiModel):
    inputText = utils.getPromptInput("Task 4: Use company data", "sample-text.txt")
    
    messages = [
        {"role": "user", "content": inputText}
    ]
    
    apiParams = {
        "messages": messages,
    }
    
    utils.writeLog("API Parameters:\n", apiParams)

    response = aiClient.chat.completions.create(
        model=aiModel,
        **apiParams
    )
    
    utils.writeLog("Response:\n", str(response))
    print("Response: " + response.choices[0].message.content + "\n")
    return

# Call main function. Do not modify.
if __name__ == '__main__': 
    main()
