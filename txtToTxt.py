from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from openai import OpenAI
import os
from typing import List

app = FastAPI()

templates = Jinja2Templates(directory="templates")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)



class ChatMessage(BaseModel):
    message: str

@app.get("/", response_class = HTMLResponse)
async def read_root(request : Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get("/camera", response_class = HTMLResponse)
async def camera(request: Request):
    return templates.TemplateResponse("camera.html", {"request" : request})

@app.get("/AIimg", response_class = HTMLResponse)
async def ai_img(request: Request):
    return templates.TemplateResponse("imagegenAI .html", {"request": request})

@app.get("/material", response_class = HTMLResponse)
async def material(request: Request):
    return templates.TemplateResponse("materials.html", {"request":request})

@app.get("/materials.html", response_class = HTMLResponse)
async def materials_html(request: Request):
    return templates.TemplateResponse("materials.html", {"request":request})

@app.get("/shorts", response_class = HTMLResponse)
async def shorts(request: Request):
    return templates.TemplateResponse("shorts.html", {"request": request})

@app.get("/shorts.html", response_class = HTMLResponse)
async def shorts_html(request: Request):
    return templates.TemplateResponse("shorts.html", {"request": request})

@app.get("/scheduler.html", response_class = HTMLResponse)
async def scheduler_html(request: Request):
    return templates.TemplateResponse("scheduler.html", {"request": request})

@app.get("/dashboard.html", response_class = HTMLResponse)
async def dashboard_html(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/job.html", response_class = HTMLResponse)
async def job_html(request: Request):
    return templates.TemplateResponse("job.html", {"request": request})

@app.get("/camera.html", response_class = HTMLResponse)
async def camera_html(request: Request):
    return templates.TemplateResponse("camera.html", {"request": request})

@app.get("/assistant.html", response_class = HTMLResponse)
async def assistant_html(request: Request):
    return templates.TemplateResponse("assistant.html", {"request": request})

@app.get("/quiz.html", response_class = HTMLResponse)
async def quiz_html(request: Request):
    return templates.TemplateResponse("quiz.html", {"request": request})

@app.get("/imgTOtext.html", response_class = HTMLResponse)
async def imgtotext_html(request: Request):
    return templates.TemplateResponse("imgTOtext.html", {"request": request})

@app.get("/txtTOvideo.html", response_class = HTMLResponse)
async def txttovideo_html(request: Request):
    return templates.TemplateResponse("txtTOvideo.html", {"request": request})

@app.post("/chat")
async def chat(chat_message: ChatMessage):
    JSONResponceForm = """const AnyTitleOfTheContent = [
            {
                id: 1,
                title: "The Quantum Revolution",
                prompt:"In the early 20th century, physicists discovered that light behaves both as particles and waves. This dual nature sparked the quantum revolution.",
            },
            {
                id: 2,
                title: "Schrödinger's Equation",
                prompt: "Erwin Schrödinger formulated an equation that describes how quantum systems evolve over time. The wave function ψ contains all information about a quantum system."
            },
            {
                id: 3,
                title: "The Uncertainty Principle",
                prompt: "Heisenberg showed that we cannot simultaneously know both the position and momentum of a particle with perfect accuracy. This fundamental limit is known as the uncertainty principle."
            },
            {
                id: 4,
                title: "Quantum Superposition",
                prompt:"Quantum particles can exist in multiple states simultaneously. Schrödinger's famous cat thought experiment illustrates this paradoxical behavior."
            },
            {
                id: 5,
                title: "Quantum Entanglement",
                prompt: "When particles become entangled, they share a quantum connection. Measuring one instantly affects the other, no matter how far apart they are."
            }
        ];"""
    # Conversation handling commented out - needs proper implementation
    # if not hasattr(app, 'conversation'):
    #     app.conversation = Conversation()
    manipulated_prompt = f"you have to generate the response in json format alone. you have to reply in this format '' "

    # app.conversation.messages.append({"role": "user", "content": manipulated_prompt})
    # append_to_aboutme(f"User: {chat_message.message}")

    completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=[{"role": "user", "content": chat_message.message}],
        temperature=1,
        top_p=1,
        max_tokens=2000,
        stream=True
    )

    response = ""
    for chunk in completion:
        if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content
    # app.conversation.messages.append({"role": "assistant", "content": response})

    # append_to_aboutme(f"AI: {response}")

    return {"response": response}
