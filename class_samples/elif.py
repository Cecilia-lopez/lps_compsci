print("Hi! How old are you?")
age = int(input())


if age >= 18:
  print("Sorry, you're too old to use the swingset!")
else:
  if age < 5:
    print("Welcome to the park! Use the baby swings.")
  elif age < 10:
    print("Welcome to the park! Use the big swings.")
  else:
    print("Welcome to the park! Push a little kid on the swings.")

