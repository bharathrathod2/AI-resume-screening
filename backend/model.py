from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re
from collections import Counter

MODEL_NAME = 'all-MiniLM-L6-v2'

class ResumeScorer:
    def __init__(self, model_name=MODEL_NAME):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)

    def score(self, resume_text, job_description, top_k=5):
        emb_resume = self.embed([resume_text])[0]
        emb_jd = self.embed([job_description])[0]
        sim = cosine_similarity([emb_resume], [emb_jd])[0][0]

        jd_terms = self._extract_keywords(job_description)
        resume_terms = self._extract_keywords(resume_text)
        matched = [t for t in jd_terms if t.lower() in ' '.join(resume_terms).lower()]
        missing = [t for t in jd_terms if t not in matched]

        phrases = self._top_phrases(resume_text, top_k)

        return {
            'match_score': float(round(sim, 4)),
            'matched_skills': matched[:top_k],
            'missing_skills': missing[:top_k],
            'top_resume_phrases': phrases
        }

    def _extract_keywords(self, text):
        tokens = re.findall(r"[A-Za-z0-9+#\.\-]+", text)
        unique = []
        for t in tokens:
            if len(t) > 1 and t.lower() not in unique:
                unique.append(t)
        return unique[:120]

    def _top_phrases(self, text, k):
        words = re.findall(r"\w+", text.lower())
        cnt = Counter(words)
        common = cnt.most_common(k+10)
        return [{'phrase': w, 'weight': float(freq)} for w, freq in common[:k]]