from httplib2 import Http
from json import dumps
import os

def lambda_handler(event, context):
    # Obtém a URL do webhook a partir das variáveis de ambiente
    url = os.environ.get('webhook_url')

    # Cria a mensagem do bot em formato JSON a partir da mensagem do evento SNS
    bot_message = {'text': event['Records'][0]['Sns']['Message']}
    
    # Define os cabeçalhos da mensagem
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    
    # Cria uma instância do objeto Http
    http_obj = Http()
    
    # Envia a requisição POST para a URL do webhook com a mensagem do bot em JSON
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    
    # Retorna a resposta da requisição
    return response