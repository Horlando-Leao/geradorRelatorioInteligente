from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Test")

conversation = [
    "Relatório de vendas 2020",
    "Relatorio de vendas 2010 à 2020"
]


trainer = ListTrainer(chatbot)
trainer.train(conversation)

while True:
    quest = input('Você: ')
    response = chatbot.get_response(quest)
    print(response)