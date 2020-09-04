from gensim.models import KeyedVectors
from gensim.models import Word2Vec 
import ast

# Reads out.txt’ file 
sample = open("out.txt", "r") 
s = sample.read() 

# Preprocessing
f = s.lower().replace('"', '').replace(" ","").replace(',',' ').strip().split("\n")
data = [] 
for line in f:
    data.append(line.split())

print("Data done!")

# Create CBOW model 
print("Training!")
model1 = Word2Vec(data, min_count = 1,  
                              size = 100, window = 50, workers=10) 

print("Training done!")
word_vectors = model1.wv
word_vectors.save("../models/vectors_bog.kv")
# model1.save("../models/gensim_bog.bin")
      
# Create Skip Gram model
print("Training again!") 
model2 = Word2Vec(data, min_count = 1, size = 100, 
                                             window = 50, sg = 1, workers=10) 

print("Done again!")
word_vectors2 = model2.wv
word_vectors2.save("../models/vectors_sg.kv")
# model2.save("../models/gensim_sg.bin")