import os 
import shutil 
import tkinter as tk
from tkinter import *
from tkinter import filedialog 


#Função para orgnaizar os arquivos
def organizar_arquivos(caminho_diretorio):
    files = [f for f in os.listdir(caminho_diretorio) if os.path.isfile(os.path.join(caminho_diretorio,f))]
    for file in files:
        extensao_arquivo = os.path.splitext(file)[1][1: ]
        pasta_nome = extensao_arquivo.upper() + "_Files"
        
        if not os.path.exists(os.path.join(caminho_diretorio, pasta_nome)):
            os.mkdir(os.path.join(caminho_diretorio, pasta_nome))
    
        shutil.move(os.path.join(caminho_diretorio, file), os.path.join(caminho_diretorio, pasta_nome, file))
    
    
    print("Organização completa.")
    
# Função para escolher o diretório	
def escolher_diretorio():
    caminho_diretorio = filedialog.askdirectory()
    if caminho_diretorio:
        organizar_arquivos(caminho_diretorio)
    else:
        print("Nenhum diretório selecionado.")
#Botão
root = Tk()
root.title("Organizador de arquivos")
root.geometry("300x100")

b1 = Button(root, text="Organizar", command=escolher_diretorio, font = "Verdana 12 bold", height = 2, width = 10)
b1.pack()
root.mainloop()