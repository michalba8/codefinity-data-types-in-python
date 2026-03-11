string = "It can be painful to learn from mistakes"

# Extract necessary words
learn = string[string.index('learn'):string.index('learn') + len("lesrn")]
painful = string[string.index("painful"):string.index("painful") + len("painful")]
mistakes = string[32:]


print("The variable learn equals:", learn)
print("The variable painful equals:", painful)
print("The variable mistakes equals:", mistakes)