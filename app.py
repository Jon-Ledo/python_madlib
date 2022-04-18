# Variables
# input(prompt) allows user input
adj = input("Adjective: ")
celebrity1 = input("Famous Celebrity: ")
celebrity2 = input("Famous Celebrity: ")
job1 = input("Job title: ")
job2 = input("Job title: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
noun3 = input("Noun: ")
noun4 = input("Noun: ")
noun5 = input("Noun: ")
drink = input("Drink: ")
body_part = input("Body Part: ")

madlib = f"In 356 B.C., Phillip of Macedonia, the ruler of a province in northern Greece, became the father of a bouncing baby {noun1} named Alexander. Alexander's teacher was Aristotle, the famous {job1}. When he was twenty years old, his father was murdered by {celebrity1}, after which he became {job2} of all Macedonia. In 334, he invaded Persia and defeated {celebrity2} at the battle of {noun2}. Later, at Arbela, he won his most important victory, over Darius the Third. This made him {adj} {noun3} over all Persians. Then he marched to India, and many of his {noun4} died. After that, Alexander began drinking too much {drink}, and at the age of 33, he died of an infection in the {body_part}. His last words are reported to have been, 'There are no more {noun5} to conquer.'"

print(madlib)