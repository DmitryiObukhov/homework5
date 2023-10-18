def jaccard(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    jaccard_result = intersection / union
    return jaccard_result


set_input = input("Enter your elements separated by a space: ")
input_elemets = set_input.split()
sett1 = set(input_elemets)

set_input2 = input("Enter your elements separated by a space: ")
input_elemets2 = set_input2.split()
sett2 = set(input_elemets2)

similarity = jaccard(sett1, sett2)
similarity = round(similarity, 3)
print(f'Jaccard similarity: {similarity}')
