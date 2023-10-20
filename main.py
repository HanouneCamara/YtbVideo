from pytube import YouTube

# Demandez à l'utilisateur de saisir l'URL de la vidéo YouTube
video_url = "https://youtu.be/r6RknuT-mmA?si=oJGdgq3RuyenCkA_"

# Créez un objet YouTube en passant l'URL de la vidéo
yt = YouTube(video_url)

# Obtenez la vidéo de la meilleure qualité disponible
video = yt.streams.get_highest_resolution()

# Choisissez l'emplacement où vous souhaitez enregistrer la vidéo
save_path = "../Documents"

# Téléchargez la vidéo
video.download(output_path=save_path)

print("Téléchargement terminé !")
