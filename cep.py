import urllib.request as req
import json

cep = input('CEP: ')
res = req.urlopen('http://viacep.com.br/ws/%s/json' %cep)
res_json = res.read().decode('utf-8')
end = json.loads(res_json)

print ('Logradouro: %s' %end['logradouro'])
print ('Bairro: %s' %end['bairro'])
print ('Cidade: %s' %end['localidade'])
print ('UF: %s' %end['uf'])
