# Este é um projeto baseado no video: https://www.youtube.com/watch?v=5vdEb_pitfc

import os

# Roteiro
# 1- Criar pastas
# 2- Ler arquivos
# 3- Verificar extensão
# 4- Mover arquivos

audios = [".mp3", ".wav"]
videos = [".mp4", ".avi"]
imagens = [".jpg", ".jpeg", ".png"]
documentos = [".txt", ".pdf"]

def pegar_extensao(nome):
    index = str(nome).rfind(".")
    return nome[index:]

def organizar(diretorio):
    DIRETORIO_AUDIOS = os.path.join(diretorio, "audios")
    DIRETORIO_VIDEOS = os.path.join(diretorio, "videos")
    DIRETORIO_IMAGENS = os.path.join(diretorio, "imagens")
    DIRETORIO_DOCUMENTOS = os.path.join(diretorio, "documentos")
    DIRETORIO_OUTROS = os.path.join(diretorio, "outros")

    if not os.path.isdir(DIRETORIO_AUDIOS):
        os.mkdir(DIRETORIO_AUDIOS)
    if not os.path.isdir(DIRETORIO_VIDEOS):
        os.mkdir(DIRETORIO_VIDEOS)
    if not os.path.isdir(DIRETORIO_IMAGENS):
        os.mkdir(DIRETORIO_IMAGENS)
    if not os.path.isdir(DIRETORIO_DOCUMENTOS):
        os.mkdir(DIRETORIO_DOCUMENTOS)
    if not os.path.isdir(DIRETORIO_OUTROS):
        os.mkdir(DIRETORIO_OUTROS)
    
    nome_arquivos = os.listdir(diretorio)
    for arquivo in nome_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            pasta_destino = ""
            extensao = pegar_extensao(arquivo)
            print(extensao)
            if extensao in audios:
                pasta_destino = DIRETORIO_AUDIOS
            elif extensao in videos:
                pasta_destino = DIRETORIO_VIDEOS
            elif extensao in imagens:
                pasta_destino = DIRETORIO_IMAGENS
            elif extensao in documentos:
                pasta_destino = DIRETORIO_DOCUMENTOS
            else:
                pasta_destino = DIRETORIO_OUTROS
            pasta_origem = os.path.join(diretorio, arquivo)
            pasta_destino = os.path.join(pasta_destino, arquivo)
            os.rename(pasta_origem, pasta_destino)

organizar("batatinha")
