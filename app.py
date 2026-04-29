from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import tensorflow_hub as hub
import librosa
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# cargar modelo preentrenado YAMNet
model = hub.load("https://tfhub.dev/google/yamnet/1")

# etiquetas del modelo
class_names = []
with open("yamnet_class_map.csv", "r") as f:
    next(f)
    for line in f:
        class_names.append(line.strip().split(",")[2])

#def detectar_instrumentos(audio_path):
    #waveform, sr = librosa.load(audio_path, sr=16000)

    #scores, embeddings, spectrogram = model(waveform)

    #scores_np = scores.numpy()
    #mean_scores = np.mean(scores_np, axis=0)

    #top_indices = np.argsort(mean_scores)[-5:][::-1]

    #resultados = []
    #for i in top_indices:
        #resultados.append({
            #"instrumento": class_names[i],
            #"confianza": float(mean_scores[i] * 100)
        #})

    #return resultados
def detectar_instrumentos(audio_path):
    waveform, sr = librosa.load(audio_path, sr=16000)

    scores, embeddings, spectrogram = model(waveform)

    scores_np = scores.numpy()
    mean_scores = np.mean(scores_np, axis=0)

    instrumentos_clave = [
        "piano",
        "guitar",
        "drum",
        "violin",
        "cello",
        "flute",
        "trumpet",
        "saxophone",
        "clarinet",
        "harp",
        "bass",
        "organ",
        "ukulele",
        "synthesizer"
    ]

    resultados = []

    for i, score in enumerate(mean_scores):
        nombre = class_names[i].lower()

        if any(inst in nombre for inst in instrumentos_clave):
            if score > 0.01:
                resultados.append({
                    "instrumento": class_names[i],
                    "confianza": float(score * 100)
                })

    resultados = sorted(resultados, key=lambda x: x["confianza"], reverse=True)

    if not resultados:
        return [{"instrumento": "No se detectaron instrumentos claramente", "confianza": 0}]

    return resultados[:5]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    audio = request.files["audio"]
    path = os.path.join(app.config["UPLOAD_FOLDER"], audio.filename)
    audio.save(path)

    resultados = detectar_instrumentos(path)

    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)