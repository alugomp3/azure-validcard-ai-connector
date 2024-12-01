import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from src.utils.config import config

def uploadBlob(file,fileName):
    try:
        blobServiceClient = BlobServiceClient.from_connection_string(config.AZURE_STORAGE_CONNECTION_STRING)
        blobClient = blobServiceClient.get_blob_client(container=config.CONTAINER_NAME,blob=fileName)
        blobClient.upload_blob(file, overwrite=True)

        return blobClient.url
    except Exception as ex:
        st.error(f"Erro ao enviar arquivo ao Storage: {ex}")
        return None