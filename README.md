Script de Python e corpus resultante da raspagem do subreddit da [Fraternidade São Pio X](https://www.reddit.com/r/sspx/).  

Saída em JSON, mas também estão disponíveis arquivos .csv e .docx com o corpus. O código foi parcialmente criado com auxílio do GPT 5 e usa a biblioteca [Praw](https://github.com/praw-dev/praw) para raspar até 1000 tópicos e os correspondentes comentários. 

A raspagem resultou na colheita de 739 tópicos e 5885 comentários, feitos de 14 de maio de 2022 até 1 de outubro de 2025 (compreendendo todo o conteúdo da r/sspx até a data da raspagem).

**Estrutura do arquivo JSON**

Para cada tópico, os seguintes campos:

id → identificador único do post.  
title → título do tópico.  
author → usuário que fez o post.  
score → votos recebidos (upvotes - downvotes).  
created_utc → data e hora da criação em segundos UTC.  
url → link associado (imagem, vídeo, artigo ou o link do próprio Reddit).  
num_comments → número de comentários no tópico.  
selftext → corpo do post (se houver texto além do título).  
comments → lista de objetos representando os comentários do tópico.  

Dentro dos tópicos, cada comentário carrega as seguintes informações:

id → identificador único do comentário.  
author → autor do comentário.  
score → votos recebidos no comentário.  
body → texto do comentário.  

