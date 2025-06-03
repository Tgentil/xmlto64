# 📄 Loteador de XMLs em Base64

Este script processa arquivos XML localizados em uma pasta (`./data`), converte o conteúdo de cada arquivo para base64 e agrupa os resultados em arquivos `.txt` contendo arrays de strings. Cada arquivo `.txt` representa um lote com quantidade fixa de XMLs codificados.

---

## 🚀 Como funciona

1. O script busca todos os arquivos `.xml` na pasta `./data`.
2. Cada XML é lido e convertido para **base64**.
3. A cada lote de 3 arquivos (configurável), é criado um arquivo `.txt` na pasta `./out`, no formato:

   ```json
   [
     "BASE64_XML_1",
     "BASE64_XML_2",
     "BASE64_XML_3"
   ]
   ```
4. Ao final, os arquivos restantes (caso não completem um lote) também são salvos em um último arquivo.

---

## 🛠️ Pré-requisitos

* Python 3.11
* A pasta `./data` deve conter arquivos `.xml` válidos.
* A pasta `./out` será criada automaticamente (se não existir).

---

## 📁 Estrutura de diretórios esperada

```
seu_projeto/
├── data/
│   ├── arquivo1.xml
│   ├── arquivo2.xml
│   └── ...
├── out/
│   └── lote_001.txt (gerado automaticamente)
└── script.py
```

---

## 🔧 Configurações

No início do código, você pode ajustar:

```python
PASTA_XML = './data'        # Caminho da pasta de entrada
LOTE_TAMANHO = 10            # Tamanho de cada lote
PASTA_SAIDA = './out'       # Caminho da pasta de saída
```

---

## ▶️ Como executar

No terminal, dentro do diretório do script:

```bash
python script.py
```
---

## 📝 Licença

Este projeto é livre para uso acadêmico e pessoal. Sinta-se à vontade para modificar conforme necessário.
