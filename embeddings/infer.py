import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Loading vectors
word_vectors = KeyedVectors.load("../models/vectors_sg.kv", mmap='r')

# model = Word2Vec.load("../models/gensim_sg.bin")
# print(word_vectors.n_similarity(["artificialintelligence"], ["machinelearning"]))
# print(word_vectors.most_similar(positive=['machinelearning', 'fashion'], negative=['machinelearning']))
# print(word_vectors.most_similar(positive=["machinelearning"], topn=20))

required_skill = np.array(word_vectors.get_vector("machinelearning"))
available_skill = np.array([word_vectors.get_vector("artificialintelligence"),
                            word_vectors.get_vector("naturallanguageprocessing"),
                            word_vectors.get_vector("neuralnetworks"),
                            word_vectors.get_vector("microsoftoffice"),
                            word_vectors.get_vector("softwareengineering"),
                            word_vectors.get_vector("teamleadership"),
                            word_vectors.get_vector("fashion"),
							word_vectors.get_vector("java"),
							word_vectors.get_vector("augmentedreality"),
							word_vectors.get_vector("teamplay")])

similarities = word_vectors.cosine_similarities(required_skill, available_skill)
print("Similarities:", similarities)

check_dict = ["javascript", "webdevelopment", "fashion", "photoshop", "machinelearning", "artificialintelligence", "virtualreality"]
X = word_vectors[check_dict]

# Running PCA to annotate few skills on 2D space
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# Scatter plot of the projection
plt.scatter(result[:, 0], result[:, 1])

# Annotating skills
for i, word in enumerate(check_dict):
	plt.annotate(word, xy=(result[i, 0], result[i, 1]))
plt.show()