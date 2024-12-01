from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from src.utils.config import config

def analizeCreditCardUrl(cardUrl):
    try:
        credential = AzureKeyCredential(config.KEY)
        documentAnalysisClient = DocumentIntelligenceClient(config.ENDPOINT,credential)

        cardInfo = documentAnalysisClient.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=cardUrl)
        )
        result = cardInfo.result()
        for document in result.documents:
            fields = document.get('fields', {})

            return {
                "card_name": fields.get('CardHolderName',{}).get('content'),
                "card_number": fields.get('CardNumber',{}).get('content'),
                "expiry_date": fields.get('ExpirationDate', {}).get('content'),
                "bank_name": fields.get('IssuingBank',{}).get('content'),
            }

    except Exception as ex:
        return None

def analizeCreditCardFile(file):
    try:
        credential = AzureKeyCredential(config.KEY)
        documentAnalysisClient = DocumentAnalysisClient(config.ENDPOINT,credential)

        with open(file, "rb") as f:
            analyzeDocumentRequest = AnalyzeDocumentRequest(file=f, content_type="application/pdf")
            result = documentAnalysisClient.begin_analyze_document(analize_document_request).result()
        
        return result
    except Exception as ex:
        return None