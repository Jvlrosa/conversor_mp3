from pytube import YouTube
from moviepy.editor import *
import os

def download_and_convert_to_mp3(youtube_url):
    try:
        # Baixar o vídeo do YouTube
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(only_audio=True).first()
        print("Baixando o áudio...")
        downloaded_file = stream.download()
        
        # Extrair e converter para MP3
        print("Convertendo para MP3...")
        base, ext = os.path.splitext(downloaded_file)
        mp3_file = base + '.mp3'
        
        audio_clip = AudioFileClip(downloaded_file)
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()
        
        # Remover o arquivo original de áudio
        os.remove(downloaded_file)
        
        print(f"Arquivo MP3 salvo como: {mp3_file}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    while True:
        youtube_url = input("Por favor, cole a URL do vídeo do YouTube que deseja baixar a música (ou digite 'sair' para encerrar): ")
        if youtube_url.lower() == 'sair':
            break
        download_and_convert_to_mp3(youtube_url)
        continuar = input("Deseja baixar outra música? (s/n) ")
        if continuar.lower() != 's':
            break