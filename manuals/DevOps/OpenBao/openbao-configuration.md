# Конфигурация OpenBao

<div>![OpenBao](images/openbao_color_logo.svg){: width=500 height=300}</div>


bao operator init - только в основном ноде<br/>
sudo export BAO_ADDR="http://NODE_IP:8200" - Во всех нодах<br/>
bao operator raft list-peers<br/>
echo 'BAO_ADDR="http://NODE_IP:8200"' > /etc/environment<br/>

Для настройки OpenBao в продакшен среде, нужен следущие компоненты:

1. 2 сервера для HaProxy
2. 5 серверов для OpenBao 

<div>![OpenBao Arcitecture](images/openbao_architecture.png){: width=800 height=500}</div>
