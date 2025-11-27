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


## 📁 Documentação do projeto

Descrição das etapas para análise das informações do banco de dados:

- <b>.Importação do arquivo</b>: Como exercicio de importação de dados, utilizamos como referencia o arquivo Smart Farming Sensor Data for Yield Prediction, extração do site KAGGLE, imagem a seguir demonstra a primeira etata do projeto, carga do arquivo .csv no banco de dados Oracle
<p align="center">
<img width="903" height="581" alt="Image" src="https://github.com/user-attachments/assets/b9ca973c-4138-497a-a8f4-7818b608877b" /></a>
</p>

- <b>.Metodo de Importacao</b>: seleção do método "inserir" para criação de uma nova tabela e importação de dados.
<p align="center">
<img width="913" height="581" alt="Image" src="https://github.com/user-attachments/assets/83c06682-60ea-4251-ad9b-bff592919a6d" /></a>
</p>

- <b>.Colunas ou Variaveis</b>: seleção de todas as colunas.
<p align="center">
<img width="913" height="594" alt="Image" src="https://github.com/user-attachments/assets/6bf82370-39b9-47ea-89e3-32f07772c496" /></a>
</p>

- <b>.Erro de Importacao</b>: identificação de duas colunas com nomes contendo caracteres especiais, gerando uma crítica com necessidade de correção.
<p align="center">
<img width="913" height="594" alt="Image" src="https://github.com/user-attachments/assets/a54160c3-ee6a-4df5-83f8-1c441354ddf4" /></a>
</p>

- <b>.Correção nome das colunas</b>: correções efetuadas retirada dos caracteres especiais.
<p align="center">
<img width="913" height="594" alt="Image" src="https://github.com/user-attachments/assets/9b3b2466-1546-4def-b929-5e242c563e28" /></a>
</p>

- <b>.Finalizacao</b>: finalização da etapa de importação.
<p align="center">
<img width="913" height="594" alt="Image" src="https://github.com/user-attachments/assets/cf31a73e-e7e9-4638-9882-723466530305" /></a>
</p>

- <b>.Nova Tabela - Dados Sensores</b>: criação da nova tabela DADOS SENSORES.
<p align="center">
<img width="913" height="594" alt="Image" src="https://github.com/user-attachments/assets/375d740a-b294-4e84-80e8-42e1a56732d6" /></a>
</p>

- <b>.Tabelas do Banco de Dados</b>: Podemos visualizar 4 tabelas no banco de dados, 3 tabelas pertendentes ao projeto desenvolvido na etapa 2, sendo PLANO_PRODUCAO, PREV_CLIMA e RESUMO, a tabela DADOS_SENSORES contempla a etapa 3.
<p align="center">
<img width="305" height="266" alt="Image" src="https://github.com/user-attachments/assets/7f6cb123-d7c4-4f8d-9c43-b5edb8985f7b" /></a>
</p>

- <b>.Tabela DADOS_SENSORES</b>: Consulta para visualização dos dados, dados de sensores humidade, temperatura, pH, tipo de irrigação, tipo de cultura agropecuaria e demais informações.
<p align="center">
<img width="1920" height="988" alt="Image" src="https://github.com/user-attachments/assets/7137da69-a8e2-4cf1-a676-4bdaba061b1a" /></a>
</p>

- <b>.Tabela PLANO_PRODUCAO</b>: Consulta informações utilizadas na etapa 2, nesta tabela podemos visualizar quantidade de colheitadeiras planejadas e metas de colheita por hequitare.
<p align="center">
<img width="1286" height="988" alt="Image" src="https://github.com/user-attachments/assets/c635f236-d330-49f0-b137-722a0419bda5" /></a>
</p>

- <b>.Tabela PREV_CLIMA</b>: Consulta informações utilizadas na etapa 2, nesta tabela podemos consultar informações de previsão climatologia, chuva, nuvens e temperatura, tambem podemos avaliar o impacto na produtividade nas maquinas colheitadeiras considerando previsão de chuva para os dias avalaidos .
<p align="center">
<img width="1930" height="1164" alt="Image" src="https://github.com/user-attachments/assets/83e8cf26-7c8d-466f-b359-67d0b65c9d1b" /></a>
</p>

- <b>.Tabela RESUMO</b>: Tabela RESUMO esta sem informação, não foi utilizada no projeto desenvolvido na etapa 2.
<p align="center">
<img width="1126" height="900" alt="Image" src="https://github.com/user-attachments/assets/b3e7efeb-2726-4ede-a33b-d6a61cff7f54" /></a>
</p>

- <b>.Consulta Tabela DADOS SENSORES IDE Jupyter</b>: Exibição de todos os dados da tabela.
<p align="center">
<img width="1920" height="988" alt="Image" src="https://github.com/user-attachments/assets/950420ef-6bff-4555-99ea-ba070ad32f36" /></a>
</p>

- <b>.Consulta Tabela DADOS SENSORES IDE Jupyter</b>: consulta plantação de trigo, select com utilização de um critério para filtro, utilizando operador logico ‘=’.
<p align="center">
<img width="1930" height="1164" alt="Image" src="https://github.com/user-attachments/assets/ed085228-b31a-471e-a93d-54147c4cca22" /></a>
</p>

- <b>.Consulta Tabela DADOS SENSORES IDE Jupyter</b>:  consulta plantação de trigo com tipo de irrigação gotejamento select com utilização de dois critério para filtro, utilizando operador logico ‘=’.
<p align="center">
<img width="1930" height="1164" alt="Image" src="https://github.com/user-attachments/assets/cf95256e-be69-43a0-96d4-097408e99e77" /></a>
</p>

- <b>.Consulta Tabela DADOS SENSORES IDE Jupyter</b>: consulta plantação diferente de trigo com nivel de pH superior a 700 utilização os operadores logicos diferente '<>' e maior '>'.
<p align="center">
<img width="1930" height="1164" alt="Image" src="https://github.com/user-attachments/assets/7fb44498-9ed1-476f-9287-e04d22c97f1b" /></a>
</p>

- <b>.Consulta Tabela DADOS SENSORES IDE Jupyter</b>: utilização de 3 critérios para consulta, utilizando variavel data como criterio de seleção, consulta colheitas diferentes de trigo com pH maior que 700 e previsão de colheita entre 01/ma/24 e 30/jul/24.
<p align="center">
<img width="1930" height="1164" alt="Image" src="https://github.com/user-attachments/assets/4c0a4fcd-d252-488a-9c0f-37062486605a" /></a>
</p>



## 🔧 Como executar o código

*Executar o codigo FIAP_03_01.ipynb para visualização das informações da tabela DADOS_SENSORES*


## 🗃 Histórico de lançamentos

* 0.1.0 - 10/11/2025
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
