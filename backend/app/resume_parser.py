import spacy
nlp = spacy.load("en_core_web_sm")

def parse_resume(text: bytes):
    doc = nlp(text.decode(errors="ignore"))
    skills = list(set([token.text for token in doc if token.pos_ == "NOUN"]))
    return {"skills": skills, "summary": doc.text[:500]}
