from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TraducirRequest(BaseModel):
    texto: str
    idioma: str

template = PromptTemplate.from_template(
    "Traduce el siguiente texto al {idioma}. Responde solo con la traducción, sin explicaciones:\n\n{texto}"
)

@app.post("/api/traducir")
async def traducir(req: TraducirRequest):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY no configurada")
    try:
        chat_model = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")
        prompt = template.format(idioma=req.idioma, texto=req.texto)
        respuesta = chat_model.invoke(prompt)
        return {"traduccion": respuesta.content.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health():
    return {"status": "ok"}
