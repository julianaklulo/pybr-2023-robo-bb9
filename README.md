# Programando um robô IoT com MicroPython e Raspberry Pi Pico

Repositório com o código do Robô BB9, apresentado na minha [palestra](https://pretalx.com/python-brasil-2023/talk/RRWP87/) na Python Brasil 2023.

O robô BB9 foi adquirido na [Maker Hero](https://www.makerhero.com/produto/kit-robo-bb9/).

Junto com o kit para a montagem do robô, é disponibilizado um curso para programá-lo usando a IDE do `Arduino`.

O objetivo desse projeto é portar o código para `MicroPython` e executá-lo na placa Raspberry Pi Pico W.

# Lista de Componentes
* Raspberry Pi Pico W + Barra de Pinos
* Led RGB Difuso
* Buzzer Ativo 5 V
* Micro Servo 9g SG90 TowerPro
* 2 Motores DC com Caixa de Redução e Eixo Duplo + Ponte H L298n
* 2 Rodas para Robô
* Bateria Li-Po 450 mAh + Módulo de Carga TP4056
* Chave Liga-Desliga 10 A
* Case impresso em 3D


# Diagrama do Circuito
![esquematico_bb9](https://github.com/julianaklulo/pybr-2023-robo-bb9/assets/8601883/00f54bc4-6c32-4bae-a7a2-b8a79f9533b7)


## Hardware
O código foi escrito para ser executado na placa `Raspberry Pi Pico W`.

Para executá-lo em outra placa que possua suporte ao `MicroPython`, verifique o range de escrita do PWM, pois pode ser necessário ajustar os
valores para a faixa esperada pela placa.

## Software

### Instalação do MicroPython
Para instalar o `MicroPython` na placa `Raspberry Pi Pico W`, siga as instruções no [site oficial do MicroPython](https://micropython.org/download/RPI_PICO_W/).

### Configuração do Blynk
O robô é controlado através de um aplicativo no celular, utilizando a plataforma [Blynk](https://blynk.io/).

1. Configure a sua conta no Blynk, seguindo as instruções no [site oficial do Blynk](https://blynk.io/en/getting-started).

2. Crie um template com datastreams para cada componente do projeto.

3. Crie um dispositivo, copie o `auth_token` do dispositivo e cole no arquivo `main.py`.

4. Baixe o aplicativo do Blynk e crie um dashboard para controlar o robô, utilizando os datastreams criados no passo 2.

5. Baixe a biblioteca do Blynk para MicroPython no [GitHub do Blynk](https://github.com/blynkkk/lib-python/blob/master/blynklib_mp.py) e renomeie o arquivo para `BlynkLib.py`.

### Configuração do WiFi
O kit do robô vem a com a placa `Raspberry Pi Pico`, porém como ela não possui WiFi integrado,
o robô originalmente se comunicava com a internet através do módulo `ESP8266-01`.

Esse módulo não possui biblioteca para o `MicroPython`, portanto foi necessário substituir a placa pela versão `Raspberry Pi Pico W`,
que possui WiFi integrado.

Para se conectar à internet, é necessário configurar o SSID e a senha da rede WiFi no arquivo `boot.py`.

### Copiando os arquivos para a placa
Para copiar os arquivos para a placa, é possível utilizar a IDE do `Thonny` ou a CLI `ampy` da Adafruit.

Para instalar o `ampy`, execute o comando abaixo:
```bash
pip install adafruit-ampy
```

Para copiar os arquivos para a placa, execute os comandos abaixo:
```bash
ampy --port /dev/ttyACM0 mkdir lib
ampy --port /dev/ttyACM0 put BlynkLib.py lib/BlynkLib_mp.py
ampy --port /dev/ttyACM0 put boot.py
ampy --port /dev/ttyACM0 put main.py
ampy --port /dev/ttyACM0 put robot.py
ampy --port /dev/ttyACM0 put servo.py
ampy --port /dev/ttyACM0 put motor.py
ampy --port /dev/ttyACM0 put rgb_led.py
ampy --port /dev/ttyACM0 put buzzer.py
```

### Executando o código
Após copiar os arquivos para a placa, reinicie a placa e o código será executado automaticamente.
