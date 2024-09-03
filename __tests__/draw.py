
import subprocess

input_sequence = "B\n1\n2\n3\n4\n5\n7\n6\n9\n8\n"

expected = "DRAW! How about another game?\n"

result = subprocess.run(
    ['python3', '../tictactoe.py'],
    input=input_sequence,
    text=True,
    capture_output=True
)

res = result.stdout.splitlines()
last_line = res[-1] + "\n"

assert last_line == expected, (
    f"FAILED: Expected({expected.strip()}), Got({last_line.strip()})"
)

print("PASSED!")
