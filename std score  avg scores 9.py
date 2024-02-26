import numpy as np
scores=np.array([
    [85, 90, 88, 92],  # Std 1 scores (Math, Science, English, History)
    [78, 85, 80, 88],  # Std 2 scores
    [92, 88, 90, 94],  # Std 3 scores
    [75, 82, 79, 85],  # Std 4 scores
    [80, 88, 85, 90],  # Std 5 scores
    [85, 90, 88, 92],  # Std 6 scores
    [78, 85, 80, 88],  # Std 7 scores
    [92, 88, 90, 94],  # Std 8 scores
    [75, 82, 79, 85],  # Std 9 scores
    [80, 88, 85, 90]   # Std 10 scores
])

avg=np.mean(scores,axis=0) # avg is an array that contains average per subject
print(avg)

max_avg_sub_idx=np.argmax(avg) # arg max returns the index if the largest value
print(max_avg_sub_idx)

for i, sub in enumerate(["math","sci","eng","hist"]):
    print(f"{sub} : {avg[i]}")

print(f"highest avg score subject is : {['math', 'sci', 'eng', 'hist'][max_avg_sub_idx]}")





