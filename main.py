import requests
import base64
import sys

# Configurações
token = "##Fornecido pela empresa que aplicou a avaliação"
image_url = "##URL fornecida pela empresa para download da imagem"
api_inference_url = "##URL fornecida pela empresa para envio da inferência"
api_submit_url = "##URL fornecida pela empresa para submissão da resposta"
image_file = "imagem_scrape.jpg"

# Baixar imagem
print("Baixando a imagem...")
response = requests.get(image_url)
if response.status_code == 200:
    with open(image_file, "wb") as f:
        f.write(response.content)
    print("Imagem salva:", image_file)
else:
    print("Erro ao baixar a imagem:", response.status_code)
    sys.exit(1)

# Converter imagem para base64
with open(image_file, "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode("utf-8")

# Enviar para inferência
print("Enviando imagem para inferência...")
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}
payload = {
    "model": "microsoft-florence-2-large",
    "messages": [{"role": "user", "content": "<DETAILED_CAPTION>"}],
    "files": [{"name": image_file, "data": img_base64}]
}
infer_response = requests.post(api_inference_url, headers=headers, json=payload)

if infer_response.status_code == 200:
    resposta_json = infer_response.json()
    print("Inferência concluída")
else:
    print("Erro na inferência:", infer_response.status_code)
    print(infer_response.text)
    sys.exit(1)

# Enviar resposta para submissão
print("Enviando resposta para submissão...")
submit_headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}
submit_response = requests.post(api_submit_url, headers=submit_headers, json=resposta_json)

if submit_response.status_code == 200:
    print("Resposta enviada com sucesso! Atualize a página para liberar o envio do script.")
else:
    print("Erro ao enviar resposta:", submit_response.status_code)
    print(submit_response.text)
    sys.exit(1)
