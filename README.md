# Biolab-Simulator (BLSIM)
Esse projeto consiste no Trabalho de Conclusão de Curso (TCC) do aluno Gabriel Salateo Rosin - RA 172436 para o curso de Engenharia Química da UNICAMP.

## O projeto
Com o intuito de desenvolver um software para predição de propriedades de ésteres e biodiesel, o estudo consiste em uma análise das principais especificações para comercialização do Biodiesel no Brasil, além da avaliação e seleção de modelos preditivos referentes às propriedades listadas nessas especificações para incorporação à ferramenta.

## Tecnologias
Este software foi desenvolvido utilizando o Framework Django (4.1.2) seguindo arquitetura MVC, com utilização da linguagem Python (3.8) para o back-end e HTML, CSS e JavaScript para o front-end. Para o banco de dados, foi utilizado o ORM original do Django conectado a um banco de dados relacional SQLite.

## Deploy
O sistema está em produção através da plataforma Heroku por meio deste [link](https://blsim.herokuapp.com/).

## Colaboração
Para colaboração à ferramenta, crie um Pull Request ou entre em contato com o autor do projeto através do email gabriel.s.rosin@gmail.com.

## Como executar o projeto localmente
Para rodar o projeto localmente em sua máquina, é necessário ter o Python com o pip instalado em sua máquina. Feito isso, siga os passos abaixo:

1. Clone o repositório:

```
    $ git clone https://github.com/gabao55/Biolab-Simulator.git
```

2. Acesse a pasta do projeto:


```
    $ cd Biolab-Simulator
```

3. Instale as dependências do projeto (Se preferir crie um ambiente virtual para o projeto):

```
    $ pip install -r requirements.txt
```

4. Na pasta "biolab_simulator" crie um arquivo .env de acordo com o modelo .env.example
5. Assim que todas as dependências estiverem instaladas, execute o projeto localmente:

```
    $ python manage.py runserver
```

6. Com isso, o projeto estará sendo executado localmente, então acesse o endereço http://127.0.0.1:8000/ para acompanhar a execução.