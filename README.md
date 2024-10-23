# Organizador de Arquivos Python

Este projeto é um script em Python que organiza arquivos em uma pasta específica, classificando-os em categorias baseadas em suas extensões. É uma ferramenta prática para manter sua pasta organizada, evitando a desordem de arquivos variados.

## Funcionalidades

- **Organização Automática:** O script percorre a pasta onde está localizado e organiza os arquivos em subpastas de acordo com suas categorias.
- **Prevenção de Sobrescrição:** Se um arquivo com o mesmo nome já existir na pasta de destino, o script renomeia automaticamente para evitar perda de dados.
- **Tratamento de Erros:** Inclui tratamento de exceções para gerenciar possíveis erros durante o processo de movimentação de arquivos e diretórios.

## Categorias de Arquivos

Os arquivos são organizados nas seguintes categorias:

- **Compactados:** ZIP, RAR, 7Z, etc.
- **Documentos:** PDF, DOCX, XLSX, TXT, etc.
- **Imagens:** JPG, PNG, GIF, BMP, etc.
- **ISOs:** Arquivos de imagem ISO.
- **Programas:** EXE, DEB, MSI, etc.
- **Torrent:** Arquivos .torrent.
- **Vídeos:** MP4, AVI, MKV, etc.
- **Músicas:** MP3, WAV, FLAC, etc.
- **Outros:** Diretórios e arquivos não classificados.

## Como Usar

## Windows
1 Verificar se o Python está instalado:
- Abra o Prompt de Comando ou o PowerShell e digite:
  python --version
  - Se o Python não estiver instalado, baixe-o no site oficial do Python: https://www.python.org/downloads/ e siga as instruções de instalação. Não se esqueça de marcar a opção "Add Python to PATH" durante a instalação.

2 Navegar até a pasta onde o arquivo .py está localizado:
- No Prompt de Comando, use o comando cd para mudar para o diretório onde está o arquivo Python.
  cd C:\caminho\da\pasta
  
3 Executar o arquivo .py: 
- Após estar no diretório correto, digite o seguinte comando para executar o arquivo:
  python organizador.py

## Linux
1 Verificar se o Python está instalado
- Abra o terminal e digite:
```bater
  python3 --version
```

- Se o Python não estiver instalado, você poderá usá-lo usando o gerenciador de pacotes de sua distribuição. Para Ubuntu ou Debian, use:
```bater
  sudo apt update
  sudo apt install python3
 ```
2 Navegue até a pasta onde o arquivo .py está localizado:
- No terminal, use o comando cdpara mudar para o diretório onde está o arquivo Python:
  cd /caminho/da/pasta

3 Execute o arquivo .py:
- Após estar no diretório correto, digite o seguinte comando para executar o arquivo:
  python3 organizador.py


## Essas instruções abrangem tanto o Windows quanto o Linux, fornecendo orientações claras para os usuários. Sinta-se à vontade para fazer ajustes ou adições conforme necessário! Se precisar de mais alguma coisa, é só avisar.
