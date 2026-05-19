from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  

app = FastAPI(title= "Notes API", description="A simple API for managing notes")

@app.get("/health")
async def health_check():  #async is a keyword that allows the function to run asynchronously, meaning it can handle multiple requests at the same time without blocking the main thread.
    return {"status": "healthy", "message": "The API is up and running!"} 

@app.get("/")
async def root():
    return {"message": "Welcome to the Notes API! Use /docs for API documentation."}

NOTES = [
    {"id": 1, "title": "Learn FastAPI", "content": "Build REST APIs with Python"},
    {"id": 2, "title": "Build Projects", "content": "Create 40 projects in 40 days"}
]

class Note(BaseModel):
    title: str
    content: str

@app.get("/notes")
async def get_notes():
    # This is a placeholder for fetching notes from a database or in-memory store
    return [Note(**note) for note in NOTES]  # Return a list of Note objects

@app.post("/notes")
async def create_note(note: Note):
    # This is a placeholder for saving the note to a database or in-memory store
    new_note = {"id": len(NOTES) + 1, "title": note.title, "content": note.content}
    NOTES.append(new_note)
    return Note(**new_note)  # Return the created Note object

@app.get("/notes/{note_id}")
async def get_note(note_id: int):
    # Find the note with matching id
    for note in NOTES:
        if note["id"] == note_id:
            return note
    
    # If we reach here, the note wasn't found
    raise HTTPException(status_code=404, detail="Note not found")

@app.put("/notes/{note_id}")
async def update_note(note_id: int, updated_note: Note):
    for i, note in enumerate(NOTES):
        if note["id"] == note_id:
            NOTES[i] = {"id": note_id, "title": updated_note.title, "content": updated_note.content}
            return Note(**NOTES[i])  # Return the updated Note object
    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}", status_code=204)
async def delete_note(note_id: int):
    for i, existing in enumerate(NOTES):
        if existing["id"] == note_id:
            NOTES.pop(i)  # Remove from list
            return  # 204 status means "success, no body"
    
    raise HTTPException(status_code=404, detail="Note not found")


