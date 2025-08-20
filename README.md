# Laboratórios de Análise de Texto e Fala - Microsoft Learn AI Fundamentals

Este repositório contém os arquivos gerados e utilizados nos laboratórios de Análise de Texto ([Lab 06](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/06-text-analysis.html)) e Análise de Fala ([Lab 09](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/09-speech.html)) do curso Microsoft Learn AI Fundamentals.

## Estrutura de Pastas

```
grafico_sentimentos.py
images/
  Image/
    Fala/
      FalaSlide1.JPG
      FalaSlide2.JPG
      FalaSlide3.JPG
    Sentimento/
      SentimentoSlide1.JPG
      SentimentoSlide2.JPG
      SentimentoSlide3.JPG
      SentimentoSlide4.JPG
      SentimentoSlide5.JPG
      SentimentoSlide6.JPG
      SentimentoSlide7.JPG
      SentimentoSlide8.JPG
      SentimentoSlide9.JPG
      SentimentoSlide10.JPG
json/
  Fala/
    TranscriçãoDaFala.json
  Sentimento/
    resultadoFrase1.json
    resultadoFrase2.json
    resultadoFrase3.json
```

## Descrição dos Arquivos

### Laboratório 06 - Análise de Texto

- [resultadoFrase1.json](json/Sentimento/resultadoFrase1.json): Resultado da análise de sentimento de uma avaliação negativa de hotel.
- [resultadoFrase2.json](json/Sentimento/resultadoFrase2.json): Resultado da análise de sentimento de uma avaliação positiva de hotel.
- [resultadoFrase3.json](json/Sentimento/resultadoFrase3.json): Resultado da análise de sentimento de uma avaliação mista de hotel.
- [Pasta de slides de sentimento](images/Image/Sentimento/): Slides ilustrativos do laboratório de análise de texto.

### Laboratório 09 - Análise de Fala

- [TranscriçãoDaFala.json](json/Fala/TranscriçãoDaFala.json): Transcrição e análise de uma frase falada, incluindo palavras, offsets e duração.
- [Pasta de slides de fala](images/Image/Fala/): Slides ilustrativos do laboratório de análise de fala.


### Visualização dos Resultados

- [grafico_sentimentos.py](grafico_sentimentos.py): Script Python localizado no diretório raiz do projeto. Ele gera um gráfico comparativo dos sentimentos das frases analisadas nos arquivos JSON em `json/Sentimento`.

#### Bibliotecas necessárias

Para executar o script, certifique-se de ter as seguintes bibliotecas instaladas:

- `matplotlib`

Você pode instalar usando o comando:

```powershell
pip install matplotlib
```

#### Como executar

Basta executar o comando abaixo no terminal, a partir do diretório raiz:

```powershell
python grafico_sentimentos.py
```
O gráfico exibirá os valores percentuais de sentimento (positivo, neutro, negativo) para cada frase.

## Referências

- [Lab 06 - Text Analysis](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/06-text-analysis.html)
- [Lab 09 - Speech Analysis](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/09-speech.html)

## Observações

Os arquivos JSON contêm os resultados das APIs de Análise de Sentimento e de Transcrição de Fala, conforme demonstrado nos laboratórios. As imagens servem como apoio visual para os experimentos realizados.

by CBS construido no VScode com auxílio do chatGPT
