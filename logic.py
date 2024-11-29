import speech_recognition as sr


def transcribe_audio(file_path: str) -> str:
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
    try:
        return recognizer.recognize_google_cloud(audio_data)
    except sr.UnknownValueError:
        raise ValueError("Unable to understand the audio")
    except sr.RequestError as e:
        raise RuntimeError(f"API unavailable: {e}")


from typing import List


def find_songs_with_lyrics(lyrics: str) -> List[dict]:
    songs = [
        {"title": "Song A", "lyrics": "sample lyrics here", "tags": ["pop", "happy"]},
        {"title": "Song B", "lyrics": "another sample", "tags": ["rock", "sad"]},
    ]
    matching_songs = [song for song in songs if lyrics.lower() in song["lyrics"].lower()]
    return matching_songs


def find_similar_songs(tags: List[str]) -> List[dict]:
    songs = [
        {"title": "Song A", "tags": ["pop", "happy"]},
        {"title": "Song C", "tags": ["pop", "dance"]},
    ]
    similar_songs = [song for song in songs if any(tag in song["tags"] for tag in tags)]
    return similar_songs
