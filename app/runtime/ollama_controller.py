import subprocess


class OllamaController:
    def start(self):
        subprocess.Popen(["ollama", "serve"])

    def stop(self):
        subprocess.call(["pkill", "ollama"])