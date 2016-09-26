#O README eu ainda nao alterei - copiei de outro apenas

# tchelinuxcx2015


PDF
==
No diretório PDF está o PDF da apresentação, além de um PDF com as fontes utilizadas

INSTALL
==
Caso optar por visualizar os HTMLs e até editá-los, eles estão na pasta Templates.<br>
Para iniciar a aplicação (testado em Centos7):<br>
yum -y install epel-release<br>
yum -y install wget python python-pip zip unzip<br>

---O Django precisa ser instalado via PIP. Se for via Yum<br>
---vai baixar versão menor que a 1.8, aí não vai funcionar.<br>
---Depois não diga que eu não avisei<br>

pip install Django<br>
wget https://github.com/caparisotto/tchelinuxcx2015/archive/master.zip   <ou>  baixar pelo Github<br>
unzip master.zip<br>
cd tchelinuxcx2015-master<br>
./manage.py runserver 0.0.0.0:8000<br>

ACESSO
==
Via Browser em localhost:8000<br> 
Caso esteja em máquina diferente,<br>
Liberar no Firewall:<br>
iptables -I INPUT -p tcp --dport 8000 -j ACCEPT<br>
E acessar com o IP, ex.:<br>
10.1.1.1:8000<br>
