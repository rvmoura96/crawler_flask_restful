# API
Simples API para contagem no número de ocorrências de determinada palavra em um site.


Modo para utilização:
 - Via Postman: enviar uma solicitação através através do método POST para o endereço "localhost:5000/search", no Body de tal requisição inserir duas Keys, uma com o nome "url" seu valor será o site que será verificado e outra key com o nome de "word" seu valor será a palavra a ser pesquisada.
 
 A resposta será um Objeto JSON com os seguintes dados:
   {
    "Ocorrencias": Número de vezes que "word" aparece em "url".
   }
