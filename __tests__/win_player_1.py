
import subprocess

input_sequence = "B\n1\n4\n2\n5\n3\n"

expected = "CONGRATULATIONS!!! Player 1 is the winner!\n"

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

print("PASSED")
