import numpy as np
from gensim.models import KeyedVectors
word_vectors = KeyedVectors.load("models/vectors_bog.kv", mmap='r')


def preprocess_supply(supply):
    available_skills = []
    weightage_skills = []
    for skill, weightage in supply:
        # model.word_vec(skill, use_norm=True)
        # word_vectors.get_vector(skill
        available_skills.append(word_vectors.get_vector(skill))
        weightage_skills.append(int(weightage))

    available_skills = np.asarray(available_skills, dtype=np.float32)
    weightage_skills = np.asarray(weightage_skills, dtype=np.float32)

    weightage_skills /= 5.
    return available_skills, weightage_skills


def match_skill(demand, supply):
    '''
    Sample usage:
    match_skill("ArtificialIntelligence" ,[("MachineLearning", 4), ("Fashion", 3)])
    '''
    try:
        required_skill = np.array(word_vectors.get_vector(demand))
        available_skills, weightage_skills = preprocess_supply(supply)   
        similarities = word_vectors.cosine_similarities(required_skill, available_skills)
    except:
        return 0
    # Normalizing
    similarities = (similarities + 1) / 2.

    score = similarities * weightage_skills

    return max(score)