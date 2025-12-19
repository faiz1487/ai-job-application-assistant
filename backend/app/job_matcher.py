from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer("all-MiniLM-L6-v2")

def match_jobs(resume):
    resume_emb = model.encode(" ".join(resume["skills"]))
    jobs = [
        "DevOps Engineer AWS Docker Kubernetes",
        "Cloud Support Engineer Linux"
    ]
    return [
        {"job": j, "score": round(util.cos_sim(resume_emb, model.encode(j)).item() * 100, 2)}
        for j in jobs
    ]
