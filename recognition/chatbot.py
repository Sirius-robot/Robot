import os
import dialogflow

REACTIONS_MAPPING = {
    "аргументация":"argumentation",
    "бездействие":"inactivity",
    "бесздействие":"inactivity",
    "гнев":"anger",
    "грусть":"sadness",
    "задумчивость":"thinking",
    "извинение":"excuses",
    "компенсация+бездействие":"inactivity",
    "недоумение":"nedoumenie",
    "неоумение":"nedoumenie",
    "обобщение":"suming-up",
    "отрицание":"negation",
    "перечисление":"enumeration",
    "подытоживание":"suming-up",
    "приветствие":"greeting",
    "привлечение внимания":"attract attention",
    "привлечение внмания":"attract attention",
    "прощание":"goodbye",
    "радость":"joy",
    "размышление":"thinking",
    "смущение":"confusion",
    "согласие":"agree",
    "удивление":"amaze",
}

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.getcwd(),'credential.json')
project_id = "small-talk-1-dc0b5"
session_id = "SmallTalkSession"
language_code = "ru"

def detect_intent_texts(project_id, session_id, text, language_code):
    '''Шлет запросы в dialogflow.
        project_id – id проекта, 
        session_id – id сессии, 
        text – текст входящего сообщения,
        language_code – язык.
        Sends requests to dialogflow.'''

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text == "": text = "черешенка1315"

    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(
        session=session, query_input=query_input)
    return response.query_result.fulfillment_text

def chat_bot(input_text):
    '''Получает от пользователя текст, возвращает ответ и тег.
        Gets input text, returns text answer and tag.'''

    output = (detect_intent_texts(project_id, session_id, input_text, language_code))
    try:
        tag = REACTIONS_MAPPING[output[output.find('<')+1:output.find('>')].lower()]
    except:
        tag = 'inactivity'
    text = output[:output.find('<')]
    
    return text, tag

# print(chat_bot("привет"))