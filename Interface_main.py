import streamlit as st
import base64
import Functions


st.title("Upload e Download de Imagem")

# Upload da imagem
uploaded_image = st.file_uploader("Faça o upload da sua imagem", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Exibir a imagem carregada
    # st.image(uploaded_image, caption="Imagem Carregada", use_column_width=True)

    # Botão para baixar a imagem
    if st.button("Baixar Imagem com selo da UDESC"):
        # Salvar a imagem em um arquivo temporário
        with open("temp_image.png", "wb") as f:
            f.write(uploaded_image.read())

        Functions.circularIMG('temp_image.png', (944, 944))

        # Criar um link para o download da imagem
        st.markdown(Functions.get_binary_file_downloader_html("temp_image.png", "Imagem baixada.png"),
                    unsafe_allow_html=True)
