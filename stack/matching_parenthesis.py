# Algorithm to match valid parenthesis
from stack import ArrayStack

def is_matched(expression):
   
  bracket_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
   
  S = ArrayStack()
  for bracket in expression:
    if bracket in bracket_pairs.values():
      S.push(bracket)
    elif bracket in bracket_pairs.keys():
      if S.is_empty():
        return False
      if bracket_pairs[bracket] != S.pop():
        return False
  return S.is_empty()

# Test case

expression1 = "((( )(( )){([( )])}))"

expression2 = " ({[])}"

print(is_matched(expression1))  
