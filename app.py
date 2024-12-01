##poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-document", docUrl)

##result = poller.result()
import streamlit as st
from src.services.blob_service import uploadBlob
from src.services.credit_card_service import analizeCreditCardUrl

def configure_interface():
    st.title("Upload arquivo DIO desafio 1 - Python Azure - Fake Docs")
    uploadedFile = st.file_uploader("Escolha um arquivo", type=["png","jpg","jpeg"])

    if uploadedFile is not None:
        fileName = uploadedFile.name
        ## Load Blob to storage
        blobUrl = uploadBlob(uploadedFile, fileName)
        if blobUrl:
            st.write(f"Arquivo {fileName} enviado com sucesso ao Azure Storage")
            creditCardInfo = analizeCreditCardUrl(blobUrl)
            showImageValidation(blobUrl,creditCardInfo)
        else:
            st.write(f"Erro ao enviar arquivo {fileName}")

def showImageValidation(blobUrl, creditCardInfo):
    st.image(blobUrl, caption="Imagem Enviada", use_column_width=True)
    st.write("Verificando informações do cartão:")
    if creditCardInfo and creditCardInfo["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {creditCardInfo['card_name']}")
        st.write(f"Banco Emissor: {creditCardInfo['bank_name']}")
        st.write(f"Data de Validade: {creditCardInfo['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Cartão de Crédito inválido")

if __name__ == "__main__":
    configure_interface()