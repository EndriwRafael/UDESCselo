import streamlit as st
import base64
import Functions

# Adicione sua logo como um elemento de imagem
st.image("Udesc_LOGO.png", use_column_width=True)  # Substitua "caminho_para_sua_logo.png" pelo caminho real da sua logo
st.title("Insira abaixo o selo da UDESC na sua foto de perfil")

# Upload da imagem
uploaded_image = st.file_uploader("Faça o upload da sua imagem", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Exibir a imagem carregada
    # st.image(uploaded_image, caption="Imagem Carregada", use_column_width=True)

    # Botão para baixar a imagem
    if st.button("Clique aqui para gerar sua nova imagem!"):
        # Salvar a imagem em um arquivo temporário
        with open("temp_image.png", "wb") as f:
            f.write(uploaded_image.read())

        Functions.circularIMG('temp_image.png', (944, 944))

        # Criar um link para o download da imagem
        st.markdown(Functions.get_binary_file_downloader_html("temp_image.png", "Imagem baixada.png"),
                    unsafe_allow_html=True)
