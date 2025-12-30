class FileGenerator:
    def generate_text(self, content: str) -> bytes:
        return content.encode()

    def generate_markdown(self, content: str) -> bytes:
        return f"# Generated File\n\n{content}".encode()