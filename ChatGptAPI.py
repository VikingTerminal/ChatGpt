from termcolor import colored
import time
import openai

api_key = input(colored("benvenuto e grazie per aver provato questo tool. guarda altre utility su t.me/VikingTerminal.\n\nInserisci la tua chiave API di OpenAI: ", "green"))
nome_utente = input("Inserisci il tuo nome utente: ")

openai.api_key = api_key

def invia_messaggio(messaggio):
    conversazione = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": messaggio}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=conversazione
    )

    return response['choices'][0]['message']['content']

benvenuto = colored("Benvenuto nella chat con ChatGPT!! Questo tool fa parte del progetto di Viking. Unisciti a\n t.me/VikingTerminal", "green")
istruzioni = colored("Inserisci i tuoi messaggi. Scrivi 'exit' per uscire.", "yellow")
print(f"{benvenuto}\n{istruzioni}")

while True:
    input_utente = input(colored(f"{nome_utente}: ", "blue"))
    if input_utente.lower() == 'exit':
        break

    risposta = invia_messaggio(input_utente)

    for char in risposta:
        print(colored(char, "cyan"), end="", flush=True)
        time.sleep(0.03)
    print()
