# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the
# number of letters in each word.

# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
print(sentence_list)
# result = {key:val for item in list}
result = {item:len(item) for item in sentence_list}
print(result)
# result = {key:val for (key,val) in dict.item() if condition}


