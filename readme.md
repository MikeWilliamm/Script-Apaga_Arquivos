## Objetivo
Desenvolver um script que se conecta a um banco de dados, e por uma consulta extrai a informações de diretórios de arquivos, com todos esses diretórios extraídos, o programa deve tentar acessar todos os diretórios e deletar o arquivo em questão, ao final um e-mail deve ser enviado informando quantos arquivos foram deletados e quantos falharam ao serem deletados, essa falha pode ocorrer por conta do arquivo ou diretório já não existir mais.

## Solução proposta
<b>Stacks:</b> 
- Python (psycopg2, os, MIMEMultipart, MIMEText, smtplib)
- Postgres

<b>Arquitetura:</b>  Primeiramente o script se conectara ao banco de dados PostgreSQL, lá ocorrerá uma consulta SQL que retornara um dataframe composto por diretórios de arquivos, em seguido, o programa ira tentar acessar e apagar esses arquivos, também nessa etapa ocorre o armazenando da quantidade que foi apagar e a quantidade que não foi possível  apagar, finalizando é enviado um e-mail informando a quantidade de arquivos apagados e quantidade de arquivos que não foi possível apagar.


## Resultados
<b>Problemas resolvidos:</b> Programa desenvolvido utilizando logica de programação com bibliotecas já conhecidas, não tive grandes dificuldades para realizar o desenvolvimento.


<b>Exemplo de resultado enviado por e-mail:</b>
```
>> ARQUIVOS APAGADOS COM SUCESSO: 4000 
<< ERROS - ARQUIVO OU DIRETORIO NÃO ENCONTRADO: 3634
```
