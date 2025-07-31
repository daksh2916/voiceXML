from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.get("/voice")
def voice_response():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say voice="alice">Hello Mom, this is a test call from Daksh Tiwari</Say>
    </Response>"""
    return Response(content=xml, media_type="application/xml")
