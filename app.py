import speech_recognition as sr
from gtts import gTTS
import pygame
import secrets

# Inicializa o reconhecedor de voz
r = sr.Recognizer()

# Inicializa o pygame
pygame.init()

# Loop do chatbot
while True:
    # Captura a entrada de áudio
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = r.listen(source)
    try:
        # Tenta reconhecer a fala
        text = r.recognize_google(audio, language="pt-BR")
        print("Você disse: " + text)

        # Se o usuário disser "sair", sai do loop
        if text == "sair":
            break

        # Gera a resposta do chatbot
        if "como você está" in text:
            response = "Eu estou bem, obrigado por perguntar!"
        elif "qual é o seu nome" in text:
            response = "Meu nome é Bot."
        else:
            response = "Desculpe, não entendi o que você disse."

        # Gera o arquivo de áudio da resposta
        name = secrets.token_hex(16)
        tts = gTTS(response, lang="pt")
        tts.save(f"audio/{name}.mp3")

        # Toca o arquivo de áudio
        pygame.mixer.music.load(f"audio/{name}.mp3")
        pygame.mixer.music.play()

    except sr.UnknownValueError:
        # Caso o reconhecimento de voz falhe
        print("Não entendi")
    except sr.RequestError as e:
        # Caso ocorra algum erro durante o processo
        print("Erro ao chamar o serviço de reconhecimento de voz: {0}".format(e))
