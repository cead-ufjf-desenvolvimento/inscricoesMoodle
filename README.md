# Inscrições de alunos na plataforma Moodle Cead
O sistema em questão é responsável pelo preenchimento do formulário do aluno em cursos pré cadastrados na base de dados do CEAD.
## Armazenamento dos dados
Ao fim do seu cadastro são gerados arquivos de inserção em banco de dados nos modelos MySQL e SQL, além de um modelo NoSQL, em .json, para controle interno, e um arquivo .csv contendo os dados necessários para cadastro no sistema pela equipe de suporte do CEAD.
## Envio das informações
O sistema cria e encaminha via e-mail uma senha de 8 caracteres contendo, no mínimo, um caracter em letra maiúscula, um caracter em letra minúscula, um dígito numérico e um símbolo, conforme a recomendação do Moodle para criação de senhas.
Os detalhes para acesso à plataforma são enviados ao aluno via e-mail.
### Aparência do Formulário
![Aparência do formulário](docs/print1.png)