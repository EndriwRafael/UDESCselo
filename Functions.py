from PIL import Image, ImageDraw, ImageFont
import base64


def imgSELO(root_imagem, root_selo):
    imagem_sem_SELO = Image.open(root_imagem)
    imagem_SELO = Image.open(root_selo)

    # Define a posição onde deseja adicionar o selo
    posicao = (0, 0)

    # Cola o selo na imagem de perfil
    imagem_sem_SELO.paste(imagem_SELO, posicao, imagem_SELO)

    # Salva a imagem com o selo
    imagem_com_selo = imagem_sem_SELO.save(root_imagem)


def circularIMG(root, dimension):
    imagem_original = Image.open(root)
    largura_original, altura_original = imagem_original.size[0], imagem_original.size[1]

    # Verificar se a imagem_original precisa ser redimensionada
    if largura_original != altura_original:
        min_len = min(largura_original, altura_original)

        # Calcular as coordenadas de corte para ajustar a imagem_normal
        left = (imagem_original.width - min_len) // 2
        top = (imagem_original.height - min_len) // 2
        right = left + min_len
        bottom = top + min_len

        # Cortar a imagem_normal para corresponder ao tamanho da imagem_circular
        imagem_original = imagem_original.crop((left, top, right, bottom))
        new_image = imagem_original.resize(dimension)
    else:
        new_image = imagem_original.resize(dimension)

    # Desenha um circulo na imagem, onde será recortado
    mascara = Image.new('L', new_image.size, 0)
    draw = ImageDraw.Draw(mascara)
    draw.ellipse((0, 0, new_image.size[0], new_image.size[1]), fill=255)

    imagem_circular = Image.new('RGBA', new_image.size)
    imagem_circular.paste(new_image, (0, 0), mascara)
    imagem_circular.save(root)

    imgSELO('temp_image.png', 'Selo - modelo 01.png')


# Função para criar um link de download
def get_binary_file_downloader_html(bin_file, file_label='Arquivo'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}">Clique aqui para baixar</a>'
    return href