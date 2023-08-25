from PIL import Image, ImageDraw, ImageFont
import base64


def circularIMG(root, dimension):
    imagem_normal = Image.open(root)
    largura, altura = (dimension[0], dimension[1])
    imagem_redimensionada = imagem_normal.resize((largura, altura))

    mascara = Image.new('L', (largura, altura), 0)
    draw = ImageDraw.Draw(mascara)
    draw.ellipse((0, 0, largura, altura), fill=255)

    imagem_circular = Image.new('RGBA', (largura, altura))
    imagem_circular.paste(imagem_redimensionada, (0, 0), mascara)
    imagem_circular.save(root)
    imgSELO('temp_image.png', 'Selo - modelo 01.png')


def imgSELO(root_imagem, root_selo):
    imagem_sem_SELO = Image.open(root_imagem)
    imagem_SELO = Image.open(root_selo)

    # Defina a posição onde deseja adicionar o selo
    posicao = (0, 0)

    # Cole o selo na imagem de perfil
    imagem_sem_SELO.paste(imagem_SELO, posicao, imagem_SELO)

    # Salve a imagem com o selo
    imagem_com_selo = imagem_sem_SELO.save(root_imagem)

    # Mostrar a imagem resultante (opcional)
    # imagem_sem_SELO.show()


# Função para criar um link de download
def get_binary_file_downloader_html(bin_file, file_label='Arquivo'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}">Clique aqui para baixar</a>'
    return href