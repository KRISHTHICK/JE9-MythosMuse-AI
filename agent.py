import subprocess

def talk_to_muse(prompt):
    command = f"Design advice based on myth: {prompt}"
    result = subprocess.run(["ollama", "run", "tinyllama", command], capture_output=True, text=True)
    return result.stdout.strip()
