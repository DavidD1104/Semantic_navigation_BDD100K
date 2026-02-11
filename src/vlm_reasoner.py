from ollama import chat

MODEL_NAME = "llava"

class VLMReasoner:

    def encode_image(self, image_path):
        with open(image_path, "rb") as f:
            return f.read()

    def query(self, image_path):

        prompt = """
        You are a perception module for a mobile ground robot.

        Analyze the image and answer:

        1. Is it safe to move forward?
        2. Are there pedestrians directly ahead?
        3. Are there obstacles blocking the path?

        Respond strictly in this format:

        Decision: SAFE / CAUTION / STOP
        Reason: <short explanation>
        """

        image_bytes = self.encode_image(image_path)

        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    "images": [image_bytes],
                }
            ],
        )

        return response.message.content
