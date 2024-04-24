from .lib.cohere_lib.cohere_logic import CohereLogic
from .lib.cohere_lib.chat_history import ChatHistoryModel
from .lib.cohere_lib.chat import ChatModel

TEMPLATE_CHOICE = "1か2またはqを入力してEnterを押してください。"

system_chat = ChatModel(
    role='SYSTEM', 
    message='貴方はとても優秀アシスタントです。 回答はMarkdown形式で回答をお願いします。',
)

def main():
    chat_bot = None
    print("こんにちは。 使用する生成AIを選択してください。")
    print("1: ComaondR Puls")
    print("2: Groq + Llama3")
    print("q: 終了")

    while True:
        choice = input(TEMPLATE_CHOICE)
        match choice.lower():
            case "1":
                print('Use Command R Puls\n')
                chat_bot = CohereLogic()
                break
            case "2":
                print('Use Groq + Llama3\n')
                print('まだ実装してないので、1 or q を選択してください。')
            case "q":
                print('終了します。')
                exit()
            case _:
                print(TEMPLATE_CHOICE)
    
    text = input("生成AIに質問してください。 また、終了したい場合は'q'を入力してください。\nuser:\n")
    chat_history = None

    while True:
        if text.lower() == 'q':
            exit()
        else:
            if chat_history is None:
                chat_history = ChatHistoryModel(chat_history=[system_chat])

            user_chat = ChatModel(role='USER', message=text)
            response = chat_bot.create_chat(user_chat, chat_history)
            content = response.text
            print(f'chatbot:\n{content}')

            chat_history.add_chat(user_chat)
            chat_history.add_chat(ChatModel(role='CHATBOT', message=content))
        
        text = input('user:\n')

if __name__ == '__main__':
    main()
