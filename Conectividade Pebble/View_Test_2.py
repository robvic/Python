import re                                                           #Importa o package de RegularExpressions
                                                                    #Abre arquivo LinhaDoTempo txt
                                                                    #Armazena readline
                                                                    #Dá split na string
                                                                    #Concatena string de arquivo + data = Log

f = open('A) MIDIAS - USER LOG_2016-05-27_00-00-00.txt', 'r')       #Abre o arquivo de Log txt

for line in f:                                                      #Percorre cada linha do Log txt
    fLine = f.readline()                                            #Lê a linha do Log txt
    fLineExtract = re.match(\s*\d{,4}\s*\w*\s*\d{,4}\s*\w*\s*\d\s*\d{1,2}\s*\w*)
    dataLog = ""
    horaLog = ""
    bucketLog = ""
    usuarioLog = ""
    tituloLog = ""
    duracaoLog = ""

f.close()                                                           #Fecha o objeto Log


