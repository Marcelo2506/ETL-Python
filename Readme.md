# Validação de Dados em Engenharia de Dados

## Descrição do Projeto
Este projeto tem como objetivo validar dados em processos de engenharia de dados utilizando Python e bibliotecas especializadas. A validação de dados é um passo essencial para garantir a integridade, consistência e confiabilidade das informações processadas.

## Tecnologias Utilizadas
- **Python 3.12.5**
- **Pydantic 2.10.6**: Utilizado para a definição e validação de esquemas de dados.
- **Pandas 2.2.3**: Utilizado para manipulação e análise de dados tabulares.
- **Streamlit**: Utilizado para visualização interativa de relatórios.

## Funcionalidades do Projeto
### 1. Validação de Dados com Pydantic
Utiliza-se o **Pydantic** para definir esquemas de dados e garantir que os dados estejam no formato correto antes do processamento. Isso reduz erros e aumenta a segurança da análise.

### 2. Análise Exploratória com Pydantic em HTML
Os dados validados podem ser convertidos para um formato HTML para melhor visualização e inspeção.

### 3. Manipulação de Dados com Pandas
O **Pandas** é utilizado para carregar, limpar e transformar os dados de maneira eficiente, permitindo que sejam validados de forma estruturada.

### 4. Visualização de Relatórios com Streamlit
A ferramenta **Streamlit** permite a criação de dashboards interativos para visualização de relatórios e monitoramento de qualidade dos dados.

## Importância da Validação de Dados no Cotidiano
A validação de dados é essencial para evitar erros em processos de análise e tomada de decisão. Com a crescente quantidade de dados gerados diariamente, garantir sua consistência e conformidade é um diferencial para projetos de engenharia de dados e machine learning.

## Estrutura do Projeto
- **Dashboard.py**: Arquivo responsável por visualizar relatórios com Streamlit.
- **Funcao.py**: Contém funções para validar os dados do arquivo.
- **Validador.py**: Define os dados válidos utilizando Pydantic.
- **main.py**: Responsável pela análise exploratória dos dados.

## Como Executar o Projeto
1. Clone o repositório:
   ```sh
   git clone https://github.com/Marcelo2506/ETL-Python.git
   cd ETL-Python
   ```
2. Crie um ambiente virtual e instale as dependências:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
3. Execute o aplicativo Streamlit:
   ```sh
   streamlit run Dashboard.py
   ```

## Contribuição
Contribuições são bem-vindas! Fique à vontade para abrir um PR ou relatar issues.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

