import requests

# URL do vídeo
video_url = "https://www.youtube.com/watch?v=EYpQgmHCS3o"

# Nome do arquivo para salvar
output_file = "video.mp4"

# Faz o download do vídeo
response = requests.get(video_url, stream=True)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024*1024):  # Baixa em blocos de 1MB
            file.write(chunk)
    print("Download concluído: ", output_file)
else:
    print("Erro no download. Código de status:", response.status_code)
