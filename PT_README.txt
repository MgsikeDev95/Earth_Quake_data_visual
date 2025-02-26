# Visualização de Mapa de Terremotos

Este projeto utiliza dados de terremotos do USGS (United States Geological Survey) para criar um mapa interativo com a biblioteca Plotly.

## Como Usar

1. **Baixe os arquivos**:
   - No repositório do GitHub, clique no botão "Code" e depois em "Download ZIP".
   - Extraia o arquivo ZIP em uma pasta no seu computador.

2. **Instale as dependências**:
   - O script usa a biblioteca `plotly` para criar o mapa. Para instalá-la, abra o terminal ou prompt de comando e execute:
     ```bash
     pip install plotly
     ```

3. **Execute o script**:
   - Certifique-se de que o arquivo `readable_allmonth_earthquakes.geojson` está na mesma pasta que o script `all_month.py`.
   - No terminal, navegue até a pasta onde o script está localizado e execute:
     ```bash
     python all_month.py
     ```

4. **Visualize o mapa**:
   - O script abrirá automaticamente uma janela no navegador com o mapa interativo dos terremotos.

## Detalhes do Projeto

### Criação do Gráfico com Plotly
- Os dados foram baixados do [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) no dia 26/02/2025, contendo todos os terremotos registrados no último mês.
- O arquivo foi formatado para usar codificação UTF-8.
- O script lê os dados do arquivo `.geojson` e os transforma em objetos Python.
- Uma variável examina todos os terremotos no conjunto de dados.
- Listas vazias são criadas para armazenar informações como latitude, longitude, magnitude e título do terremoto (`eq_title`), que é usado para criar o texto flutuante com `hover_name`.
- Um loop `for` extrai essas informações do arquivo JSON.
- O mapa de dispersão geográfica é criado usando `px.scatter_geo` do Plotly Express.
- A projeção do mapa é definida como `natural earth`.
- O mapa é exibido com `fig.show()`.

### Formatação dos Dados
- O código abaixo foi usado para formatar os dados:
  ```python
  from pathlib import Path
  import json

  path = Path('eq_data/all_month.geojson')
  contents = path.read_bytes()

  all_eq_data = json.loads(contents)

  path = Path('eq_data/readable_allmonth_earthquakes.geojson')
  readable_contents = json.dumps(all_eq_data, indent=4)
  path.write_text(readable_contents, encoding='utf-8')