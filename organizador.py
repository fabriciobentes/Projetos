import os
import shutil

# Caminho correto para a pasta onde o script está sendo executado
folder_path = os.path.dirname(os.path.abspath(__file__))

# Dicionário com as categorias e extensões
categories = {
    "Compactados": ['zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'cab', 'arj'],
    "Documentos": ['pdf', 'pptx', 'rtf', 'docx', 'xlsx', 'txt', 'odt', 'ods', 'xls', 'xlsb', 'xlsm'],
    "Imagens": ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'svg', 'webp', 'heic', 'raw', 'ico', 'psd'],
    "ISOs": ['iso'],
    "Programas": ['exe', 'bat', 'msi', 'deb'],
    "Torrent": ['torrent'],
    "Vídeos": ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm'],
    "Músicas": ['mp3', 'wav', 'flac', 'aac', 'ogg', 'm4a'],
    "Outros": []  # Diretórios irão para "Outros"
}

# Função para encontrar a categoria baseada na extensão do arquivo
def get_category(extension):
    for category, extensions in categories.items():
        if extension in extensions:
            return category
    return "Outros"

# Função para evitar sobreposição de arquivos
def move_file_safely(src, dst):
    dst_path = dst
    counter = 1
    
    # Renomeia o arquivo se já existir um com o mesmo nome
    while os.path.exists(dst_path):
        filename, ext = os.path.splitext(dst)
        dst_path = f"{filename}_{counter}{ext}"
        counter += 1
    
    shutil.move(src, dst_path)

# Itera sobre todos os arquivos e pastas na pasta
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    
    # Verifica se é um diretório
    if os.path.isdir(item_path):
        try:
            folder_to_organize_file = os.path.join(folder_path, "Outros")
            if not os.path.isdir(folder_to_organize_file):
                os.mkdir(folder_to_organize_file)
            
            move_file_safely(item_path, os.path.join(folder_to_organize_file, item))
        except Exception as e:
            print(f"Erro ao mover diretório {item}: {e}")
        continue
    
    # Verifica se é um arquivo
    if os.path.isfile(item_path):
        try:
            filename, file_extension = os.path.splitext(item)
            file_extension = file_extension[1:].lower()
            
            category = get_category(file_extension)
            
            category_folder = os.path.join(folder_path, category)
            if not os.path.isdir(category_folder):
                os.mkdir(category_folder)
            
            subfolder_to_organize_file = os.path.join(category_folder, file_extension)
            if not os.path.isdir(subfolder_to_organize_file):
                os.mkdir(subfolder_to_organize_file)
            
            move_file_safely(item_path, os.path.join(subfolder_to_organize_file, item))
        
        except Exception as e:
            print(f"Erro ao mover arquivo {item}: {e}")
