# Use a imagem oficial do Python
FROM python:3.8-slim

# Define a variável de ambiente para não escrever os arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Define a variável de ambiente para não bufferizar a saída stdout e stderr
ENV PYTHONUNBUFFERED 1

# Cria e define o diretório de trabalho no container
WORKDIR /app

RUN apt-get update && apt-get install default-libmysqlclient-dev pkg-config build-essential python3-dev -y \
    && apt-get clean

# Instala as dependências
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o projeto para o diretório de trabalho (todos os arquivos e diretórios na raiz do projeto)
COPY . /app/
COPY start-django.sh /app/

# Tornar o script executável
RUN chmod +x /app/start-django.sh

# Porta que o servidor Django rodará
EXPOSE 8000

# Comando para executar quando o container iniciar. Neste caso, executa o script start-django.sh
CMD ["/app/start-django.sh"]


