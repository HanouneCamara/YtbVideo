from pytube import YouTube

# Demandez à l'utilisateur de saisir l'URL de la vidéo YouTube
video_url = input("Entrez l'URL de la vidéo YouTube que vous souhaitez télécharger : ")

# Créez un objet YouTube en passant l'URL de la vidéo
yt = YouTube(video_url)

# Obtenez la vidéo de la meilleure qualité disponible
video = yt.streams.get_highest_resolution()

# Choisissez l'emplacement où vous souhaitez enregistrer la vidéo
save_path = "/chemin/vers/votre/dossier/de/destination/"

# Téléchargez la vidéo
video.download(output_path=save_path)

print("Téléchargement terminé !")
