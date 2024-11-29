from fastapi import FastAPI, UploadFile, HTTPException
from logic import transcribe_audio
from logic import find_songs_with_lyrics, find_similar_songs
import os

app = FastAPI()

@app.post("/transcribe/")
async def transcribe_voice(file: UploadFile):
    file_location = f"temp/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    try:
        text = transcribe_audio(file_location)
        os.remove(file_location)
        return {"transcribed_text": text}
    except Exception as e:
        os.remove(file_location)
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/search-songs/")
async def search_songs(lyrics: str):
    matching_songs = find_songs_with_lyrics(lyrics)
    if not matching_songs:
        return {"message": "No matching songs found"}
    tags = matching_songs[0].get("tags", [])
    similar_songs = find_similar_songs(tags)
    return {
        "matching_songs": matching_songs,
        "similar_songs": similar_songs
    }
