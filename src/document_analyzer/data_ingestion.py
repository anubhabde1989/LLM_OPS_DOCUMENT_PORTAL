import os 
import sys
import fitz
import uuid
from datetime import datetime 
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentHandler:
    """
    Handles PDF saving and reading operations.
    Automatically logs all actions and creates session-based organization.
    """
    def __init__(self, data_dir=None, session_id=None):
        try:
            self.log = CustomLogger().get_logger(__name__)
            self.data_dir = data_dir or os.getenv("DATA_STORAGE_PATH",os.path.join(os.getcwd(),"data","document_analysis"))
            self.session_id = session_id or f"session_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
            self.session_path = os.path.join(self.data_dir, self.session_id)
            os.makedirs(self.session_path, exist_ok=True)
            self.log.info("PDFHandler initialized", session_id=self.session_id, session_path=self.session_path)
        except Exception as e:
            raise DocumentPortalException("Error initializing DocumentHandler", sys) from e

    def save_pdf(self, pdf_data):
        try:
            pass
        except Exception as e:
            self.log.error(f"Error saving PDF: {e}")
            raise DocumentPortalException("Error saving PDF", sys) from e 
                
    def read_pdf(self):
        try:
            pass
        except Exception as e:
            self.log.error(f"Error reading PDF: {e}")
            raise DocumentPortalException("Error reading PDF", sys) from e

if __name__ == "__main__":
    handler = DocumentHandler()
    print(f"Session ID: {handler.session_id}")
    print(f"Session path: {handler.session_path}")