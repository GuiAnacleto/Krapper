"""
    Name:       TikTok Search Engine
    Author:     Guilherme Anacleto Ferreira
    Email:      guilhermeanacleto@hotmail.com
    Modified:   2021-02-23
    A program that returns an file with tiktok info.
"""

import PySimpleGUI as sg
import os
import pandas as pd
from TikTokApi import TikTokApi
import numpy as np

#This Object create an csv archive in already passed directory
class spreadSheet:
    def __init__(self, lista, path, name):
        dataframe_array = pd.DataFrame(lista)
        dataframe_array.to_csv(path + '\\' + name + '.csv')

#This class is the heart of the program, here we have some methods that copntrol all program.
class tiktokapi:
    #In init we define the tiktok object, passing the language and the endpoints.
    #For more about this library consult: https://github.com/davidteather/TikTok-Api
    def __init__(self):
        self.api = TikTokApi.get_instance(
            use_test_endpoints=True, language='pt')

    #This method is responsible for return all information in a list, he uses some features like:
    # Hashtag name an the quantityu of results you want.
    def hashWrapp(self, hashtag, qtd):        
        tiktoks = self.api.byHashtag(hashtag, count=qtd)
        lista = np.chararray((qtd + 1, 14), unicode='utf-8', itemsize=250)
        lista[0][0] = 'Usuario'
        lista[0][1] = 'Usuario_Verificado'
        lista[0][2] = 'Usuario_Seguindo'
        lista[0][3] = 'Usuario_Seguidores'
        lista[0][4] = 'Usuario_Curtidas'
        lista[0][5] = 'Usuario_NumeroVideos'
        lista[0][6] = 'Video_Curtidas'
        lista[0][7] = 'Video_Comentarios'
        lista[0][8] = 'Video_Compartilhamentos'
        lista[0][9] = 'Video_Reproducoes'
        lista[0][10] = 'Video_URL'
        lista[0][11] = 'Musica_Titulo'
        lista[0][12] = 'Musica_Url'
        lista[0][13] = 'Musica_Duracao'

        line = 1

        for tiktok in tiktoks:
            lista[line][0] = tiktok['author']['uniqueId']
            lista[line][1] = tiktok['author']['verified']
            lista[line][2] = tiktok['authorStats']['followingCount']
            lista[line][3] = tiktok['authorStats']['followerCount']
            lista[line][4] = tiktok['authorStats']['heartCount']
            lista[line][5] = tiktok['authorStats']['videoCount']
            lista[line][6] = tiktok['stats']['diggCount']
            lista[line][7] = tiktok['stats']['commentCount']
            lista[line][8] = tiktok['stats']['shareCount']
            lista[line][9] = tiktok['stats']['playCount']
            lista[line][10] = ("https://www.tiktok.com/@" + tiktok['author']['uniqueId'] + "/video/" + tiktok['video']
                               ['id'] + "?sender_device=pc&sender_web_id=6932110861134595590&is_from_webapp=v2&is_copy_url=0 ")
            lista[line][11] = tiktok['music']['title']
            lista[line][12] = tiktok['music']['playUrl']
            lista[line][13] = tiktok['music']['duration']

            line += 1

        return lista

    #This method is literaly a copy os the HashtagMewthod, unique diference is that this method
    #do not need an hashtag, just the quantity, it returns the trending videos on tiktok.
    def trendingWrapp(self, qtd):        
        tiktoks = self.api.trending(count=qtd)
        lista = np.chararray((qtd + 1, 14), unicode='utf-8', itemsize=250)
        lista[0][0] = 'Usuario'
        lista[0][1] = 'Usuario_Verificado'
        lista[0][2] = 'Usuario_Seguindo'
        lista[0][3] = 'Usuario_Seguidores'
        lista[0][4] = 'Usuario_Curtidas'
        lista[0][5] = 'Usuario_NumeroVideos'
        lista[0][6] = 'Video_Curtidas'
        lista[0][7] = 'Video_Comentarios'
        lista[0][8] = 'Video_Compartilhamentos'
        lista[0][9] = 'Video_Reproducoes'
        lista[0][10] = 'Video_URL'
        lista[0][11] = 'Musica_Titulo'
        lista[0][12] = 'Musica_Url'
        lista[0][13] = 'Musica_Duracao'

        line = 1

        for tiktok in tiktoks:
            lista[line][0] = tiktok['author']['uniqueId']
            lista[line][1] = tiktok['author']['verified']
            lista[line][2] = tiktok['authorStats']['followingCount']
            lista[line][3] = tiktok['authorStats']['followerCount']
            lista[line][4] = tiktok['authorStats']['heartCount']
            lista[line][5] = tiktok['authorStats']['videoCount']
            lista[line][6] = tiktok['stats']['diggCount']
            lista[line][7] = tiktok['stats']['commentCount']
            lista[line][8] = tiktok['stats']['shareCount']
            lista[line][9] = tiktok['stats']['playCount']
            lista[line][10] = ("https://www.tiktok.com/@" + tiktok['author']['uniqueId'] + "/video/" + tiktok['video']
                               ['id'] + "?sender_device=pc&sender_web_id=6932110861134595590&is_from_webapp=v2&is_copy_url=0 ")
            lista[line][11] = tiktok['music']['title']
            lista[line][12] = tiktok['music']['playUrl']
            lista[line][13] = tiktok['music']['duration']

            line += 1

        return lista


#Search is a link function by the frontend, and the backend.
#this function exists to security all functions in program.
def search(values, window):
    window['-INFO-'].update(value='Searching for TikToks...')
    toker = tiktokapi()

    try:
        if values['-HASHTAG-'] == True:
            lista = toker.hashWrapp(values['-TERM-'], int(values['-QTD-']))
            spreadSheet(lista, values['-PATH-'], values['-FILENAME-'])
            window['-INFO-'].update('Enter a search term and press `Search`')
            sg.PopupOK('Finished!')
    except Exception as e:
        sg.PopupOK(e)
        window['-INFO-'].update('Enter a search term and press `Search`')

    try:
        if values['-TRENDING-'] == True:
            lista = toker.trendingWrapp(int(values['-QTD-']))
            spreadSheet(lista, values['-PATH-'], values['-FILENAME-'])
            window['-INFO-'].update('Enter a search term and press `Search`')
            sg.PopupOK('Finished!')
    except Exception as e:
        sg.PopupOK(e)
        window['-INFO-'].update('Enter a search term and press `Search`')


#Here we have the frontend design, this design is based on: https://www.youtube.com/watch?v=IWDC9vcBIFQ&t=936s
#For details acess the video :)
sg.change_look_and_feel('Black')
layout = [
    [sg.Text('Search Term', size=(11, 1)), sg.Input('', size=(40, 1), key='-TERM-'),
     sg.Radio('HASHTAG', group_id='search_type', size=(
         10, 1), default=True, key='-HASHTAG-'),
     sg.Radio('TRENDING', group_id='search_type',
              size=(10, 1), key='-TRENDING-')],

    [sg.Text('Result Quantiy', size=(11, 1)), sg.Input('50', size=(40, 1), key='-QTD-'),
     sg.Button('+10', size=(10, 1), key='-PLUS-'),
     sg.Button('-10', size=(10, 1), key='-SUB-')],

    [sg.Text('Search Path', size=(11, 1)), sg.Input('/..', size=(40, 1), key='-PATH-'),
     sg.FolderBrowse(size=(10, 1), key='-BROWSE-')],

    [sg.Text('File Name', size=(11, 1)), sg.Input(
        '', size=(40, 1), key='-FILENAME-'), sg.Button('Search', size=(10, 1), key='-SEARCH-')],

    [sg.Text('Enter a search term and press `Search`', key='-INFO-')]]

# [sg.Listbox(values=results, size=(100, 28), enable_events=True, key='-RESULTS-')]]

window = sg.Window('TikTok Search Engine', layout=layout,
                   finalize=True, return_keyboard_events=True)


#Finally the active program, this makes all funtions and screen be funtional.
#In frontend video, we have some similar thing.
while True:
    event, values = window.read()
    if event is None:
        break
    if event == '-SEARCH-':
        search(values, window)
    if event == '-PLUS-':
        value = int(values['-QTD-']) + 10
        values['-QTD-'] = str(value)
        window['-QTD-'].update(value=value)
    if event == '-SUB-':
        value = int(values['-QTD-']) - 10
        values['-QTD-'] = str(value)
        window['-QTD-'].update(value=value)
