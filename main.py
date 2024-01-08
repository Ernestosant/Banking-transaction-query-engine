from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
import shutil
import uvicorn
import os
import models
import untils



app = FastAPI()

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        with open("data.pdf", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"filename": "data.pdf"}
    except Exception as e:
        # You can customize the exception message or status code as needed
        raise HTTPException(status_code=500, detail=f"Error uploading file: {e}")

@app.post("/query/")
async def get_query_response(query: models.QueryRequest):
    try:
        response = untils.gpt_request(query=query.content)
        return {"response": response}
    except Exception as e:
        # You can customize the exception message or status code as needed
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")

if __name__ == "__main__":
    uvicorn.run(app, port=int(os.environ.get("PORT", 8000)), host="0.0.0.0")
