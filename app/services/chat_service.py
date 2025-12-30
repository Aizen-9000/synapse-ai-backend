from app.memory.memory_manager import MemoryManager
from app.services.arbitration_service import ArbitrationService

class ChatService:
    def __init__(self, model_adapter, memory_store):
        self.models = model_adapter
        self.memory = MemoryManager(memory_store)
        self.arbiter = ArbitrationService(model_adapter)

    def generate_reply(self, user_id, workspace_id, message):
        context = self.memory.retrieve_context(user_id, workspace_id)
        responses = self.arbiter.collect(message, context)
        final = self.arbiter.decide(responses)
        self.memory.store_message(user_id, workspace_id, message)
        self.memory.store_message(user_id, workspace_id, final)
        return final