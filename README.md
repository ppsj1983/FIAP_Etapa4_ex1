# FIAP - Faculdade de Informática e Administração Paulista

<br>

# Cap 1 - Memorizando e Aprendendo com os Dados da Farm Tech Solutions

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/paulo-pereira-de-souza-junior-mba-msc-0b497825/">Paulo Pereira de Souza Junior</a>

## 👨‍🎓 Apresentacao: 
- <a href="https://youtu.be/N-Xd0hJ8vtQ">Video Apresentação - YOUTUBE</a>

## 📜 Descrição

*Integração de ML com Scikit-Learn e Streamlit em dashboard estática e online para gestores agrícolas*

*Implementação de algoritmos preditivos para sugerir ações futuras de irrigação e manejo agrícola*


## 📁 Resultado do Trabalho

- Utilização do algoritmo randow forest para predição de tipo de cultura para plantação e tipo de ação para cultivo. O algoritmo randow forest apresentou 96% de acuracia para definição do tipo de cultura e 100% de acuracia para tipo de ação para manejo.
- Para simulação utiliza-se como referencia 4 variaveis, sendo, 'temperature', 'humidity', 'ph', 'rainfall', imagem a seguir demonstra o ambiente de simulação desenvolvido na plataforma Streamlit.
<p align="center">
<img width="1009" height="481" alt="Image" src="https://github.com/user-attachments/assets/ee8f3fcb-1d36-4562-b183-a4398cc89164" /></a>
</p>

- Para ilustração, utilizamos histogramas para avaliar as distribuições quantitativas das variáveis 'temperature', 'humidity', 'ph' e 'rainfall'.
<p align="center">
<img width="919" height="819" alt="Image" src="https://github.com/user-attachments/assets/276852e8-37ac-4bed-acd1-c7abb9b39852" /></a>
</p>

- Para definição definição do tipo de cultura variavel "label", as variais mais relevantes foram 'humidity' e 'rainfall'
<p align="center">
<img width="954" height="525" alt="Image" src="https://github.com/user-attachments/assets/352d199f-5e5f-4c10-88f9-3cac9e8f22cc" /></a>
</p>

- Para definição do tipo de ação de manejo, as variaveis mais relevantes foram 'temperature' e 'rainfall'
<p align="center">
<img width="911" height="566" alt="Image" src="https://github.com/user-attachments/assets/e0fbb920-65f7-4a3c-b61b-4601d992e88a" /></a>
</p>



## 🔧 Como executar o código

*Executar o codigo FIAP_03_01.ipynb para visualização das informações da tabela DADOS_SENSORES*


## 🗃 Histórico de lançamentos

* 0.1.0 - 10/11/2025
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
