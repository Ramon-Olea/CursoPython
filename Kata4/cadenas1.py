text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

print(text.split('. '))

Claves = ["average", "temperature", "distance"]

for sentence in text:
    for key_word in Claves:
        if key_word in sentence:
            print(sentence)
            break

        
for sentence in text:
    for key_word in Claves:
        if key_word in sentence:
            print(sentence.replace(' C', ' Celsius'))
            break

