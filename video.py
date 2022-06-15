from deepface import DeepFace
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
DeepFace.stream('DataSet', source = "true-detective.mp4", detector_backend = backends[0], model_name = models[1])