from gtts import gTTS
import pygame
from random import randint
from speech_list import INSULT_LIST, CONDITION_LIST

insult_list = INSULT_LIST.get('all')
condition_list = CONDITION_LIST.get('all')


def get_insult(phrase):
    """
    Função responsável por receber as palavras do usuário e responder com algo do speech_list.
    """
    user_said = phrase.upper().split()

    response = ''

    coquet = [word.upper() for word in condition_list.get('coquet')]
    common_things = [word.upper() for word in condition_list.get('common_things')]
    satanic_call = [word.upper() for word in condition_list.get('satanic_call')]
    coquet_points = 0
    satanic_points = 0
    common_points = 0

    for i in range(len(user_said)):  
            if user_said[i] in coquet:
                coquet_points += 1 if user_said[i] in coquet else 0
            
            if user_said[i] in satanic_call:
                satanic_points += 1 if user_said[i] in coquet else 0

            if user_said[i] in common_things:
                common_points += 1 if user_said[i] in common_things else 0

    if coquet_points >= satanic_points and coquet_points > common_points:
        response = random_response(insult_list.get('coquet'))

    if satanic_points > common_points:
        response = random_response(insult_list.get('satanic_call'))
    
    else:
        coin = randint(0,1)

        if coin == 1:
            response = random_response(insult_list.get('common_things'))
        else:
            response = random_response(insult_list.get('say_something'))
    
    return response


def random_response(phrase):
    """
    Função responsável por responder com frase aleatória de um dicionário.
    """
    index = ''
    index = randint(0, len(phrase)-1)

    return phrase[index]

