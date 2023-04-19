# Choco Monitor

Este é um projeto de IOT elaborado e mantido pelos alunos do curso de Big Data da Fatec Ipiranga. Ele tem como objetivo coletar dados de temperatura e humidade para a Fábrica de Alegrias. 

A Fábrica de Alegrias fabrica chocolates e foi criada por um dos alunos o Gilberto Magalhães.

Visite o site <a href="https://www.fabricadealegrias.com/" target="_blank">fabricadealegrias.com</a> e conheça seu trabalho!

## Motivação do projeto

Durante uma das aulas de IOT, ministrada pelo professor Carlos Menezes, estudávamos sobre a utilização de um sensor de humidade e temperatura (DHT11), nessa ocasião o Giberto nos contou um pouco de como funcionava a confecção dos chocolates e ressaltou como era importante o monitoramento dessas variáveis na produção. A partir daí começamos a elaborar esse projeto de monitor de temperatura e humidade para o Gilberto instalar em sua fábrica. A ideia é tornar esse processo que atuamente é realizado apenas com a experiência e conhecimento do Gilberto, em um processo mais tecnologico e automático, possibilitando um maior controle da produção e melhor qualidade do produto.

## Desenvolvimento

Para esse projeto montamos um pequeno circuito utilizando os seguintes itens:

* ESP-32
* Sensor DHT-11

O ESP-32 lê os dados capturados pelo sensor DHT-11 e envia para um servidor MQTT. A partir disso foi contruido um aplicativo móvel que consome os dados desse servidor, mostrando os dados mais recentes coletados.

Esse é o estado atual do projeto.

## Proximos passos

Por enquanto temos um monitor bem simples, mas ainda há muito o que melhorar, segue aqui algumas das melhorias futuras:

* Armazenar os dados em um Banco de Dados para análises.
* Enviar uma notificação no celular quando a temperatura ou humidade estiverem fora dos padrões.
* Enviar um email quando a temperatura ou humidade estiverem fora dos padrões.
* Ligar o ar-condicionado para controlar a temperatura e a humidade.
* Medir o gasto de energia com ar-condicionado. 