#!/usr/bin/env python3
def greetings(name="noble stranger"):
  if isinstance(name,str):
    print(f"Heloo,{name}.")
  else:
    print("Error! It was not a name.")
greetings('Alexandra')
greetings('wil')
greetings()
greetings(42)
