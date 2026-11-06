from .crucible_ingestor import CrucibleDatasetIngestor

import logging

import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class AttolightCLIngestor(CrucibleDatasetIngestor):
    '''Ingestor for parsing a full fileset from a SPECTRE cathodoluminescence run'''
    '''Ingests .xml and .txt file contents, triggers separate ingestions for individual .sur files'''

    supported_filetypes: ClassVar[list[str]] = ['.xml']

    def is_file_supported(self):
        """Check if the file to upload is a supported xml file based on its extension and content."""
        file_extension = Path(self.file_to_upload).suffix.lower()
        return file_extension in self.supported_filetypes

    def setup_data(self):
        try:
            tree = ET.parse(self.file_to_upload)
        except Exception as e:
            logger.error(f"Failed to parse file {e}")