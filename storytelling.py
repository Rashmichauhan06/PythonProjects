import random
sentence_starter= ['Once upon a time', 'About 100 years ago', 'In the 20 BC']
character=[' there was a man named jack', ' there lived a king', ' there was a old man']
time =[' one day', ' one night']
story_plot=[' he was going to the',' he was visiting to her sister who lived in the ']
place=[' market',' city named Venice']
second_character= [' he saw a young lady', ' he saw a lion']
work=[' digging a hole in the ground.',' searching for something.']

print(random.choice(sentence_starter) + random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(place)+random.choice(second_character)+ random.choice(work))