# run_all_tests.py

import subprocess

def run_test_script(script_name):

    try:
        result = subprocess.run(
            ['python3', script_name],
            text=True,
            capture_output=True
        )

        # Check if the test passed or failed
        if result.returncode == 0:
            print(f"\n---------- {script_name} ----------")
            print("PASSED\n")
        else:
            print(f"\n---------- {script_name} ----------")
            print("FAILED\n")
            print(f"Error Output:\n{result.stderr}")
    except Exception as e:
        print(f"Error running {script_name}: {e}")

test_scripts = ['win_player_1.py', 'win_player_2.py', 'draw.py']

for script in test_scripts:
    run_test_script(script)
