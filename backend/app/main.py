from fastapi import FastAPI, UploadFile
from resume_parser import parse_resume
from job_matcher import match_jobs
from cover_letter import generate_cover_letter

app = FastAPI(title="AI Job Application Assistant")

@app.post("/upload-resume")
async def upload_resume(file: UploadFile):
    content = await file.read()
    return parse_resume(content)

@app.post("/match-jobs")
def match(resume: dict):
    return match_jobs(resume)

@app.post("/cover-letter")
def cover(data: dict):
    return generate_cover_letter(data)
