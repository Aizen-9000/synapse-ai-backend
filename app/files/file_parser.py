from PIL import Image
import csv
import io

class FileParser:
    def parse_text(self, content: bytes) -> str:
        return content.decode(errors="ignore")

    def parse_csv(self, content: bytes) -> list:
        reader = csv.reader(io.StringIO(content.decode()))
        return list(reader)

    def parse_image(self, content: bytes) -> Image.Image:
        return Image.open(io.BytesIO(content))