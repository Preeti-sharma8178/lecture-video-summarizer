from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_clips(transcript_segments, summary):
    vect = TfidfVectorizer().fit(transcript_segments + [summary])
    tfidf_matrix = vect.transform(transcript_segments + [summary])
    sim_scores = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[-1:])
    ranked = sorted(zip(sim_scores, transcript_segments), reverse=True)
    return ranked[:3]
