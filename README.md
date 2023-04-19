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

## Próximos passos

Por enquanto temos um monitor bem simples, mas ainda há muito o que melhorar, segue aqui algumas das melhorias futuras:

* Armazenar os dados em um Banco de Dados para análises.
* Enviar uma notificação no celular quando a temperatura ou humidade estiverem fora dos padrões.
* Enviar um email quando a temperatura ou humidade estiverem fora dos padrões.
* Ligar o ar-condicionado para controlar a temperatura e a humidade.
* Medir o gasto de energia com ar-condicionado. 

## Como testar o projeto

Para essa finalidade será necessário montar o circuito descrito no tópico de desenvolvimento, fora isso será necessário criar uma conta no site thingspeak que é será utilizado como servidor MQTT.

Com a conta criada, crie um canal com seguinte configuração:
![image](https://user-images.githubusercontent.com/49599535/232954222-c677f72e-2f5b-4814-b832-9fcd47b1920e.png)

Agora faça o clone do projeto com o seguinte comando:

```bash
git clone https://github.com/choco-tech/choco-monitor.git
```
Ou simplemente faça o download dos arquivos em zip.

Agora será necessário fazer upload do código no ESP-32, uma das formas mais simples de se fazer isso é utilizando uma IDE como o Thonny.
[Clique aqui](https://thonny.org/) para fazer o download do Thonny. 

Basta abrir a pasta no Thonny e clicar com o botão direito nos arquivos e pastas, selecione a opção 'Uplaod to /' ilustrado na imagem abaixo:
![image](https://user-images.githubusercontent.com/49599535/232955977-d1d1014b-8514-4119-8291-02049461e3a9.png)

Será necessário também criar um arquivo secret.py, onde será configurado os dados de acesso ao Wifi e outras informações:

O arquivo secret.py deve ter a seguinte estrutura:
```python
wifi = {
    'SSID': '',
    'PASSWORD': ''
}

thingspeak = {
    'WRITE_KEY': ''
}

sensors = {
    'DHT11_PORT': 4
}
```

Obs: </br>
A 'WRITE_KEY' serve para enviar dados para o servidor MQTT, poderá encontrar essa chave no seu canal do Thingspeak.</br>
O campo 'DHT11_PORT' deve conter a porta utilizada pelo sensor DHT11 na sua instalação do circuito.

Crie o arquivo, insira os dados necessários e faça upload da para a pasta / do ESP-32.
 
