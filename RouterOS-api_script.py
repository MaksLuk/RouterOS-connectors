from routeros_api import RouterOsApiPool

connection = RouterOsApiPool('localhost', username='admin', password='admin', port=8728, plaintext_login=True)
api = connection.get_api()

# при использовании get_resource /print добавляется автоматически. если написать /print самому - будет ошибка
output = api.get_resource('/system/resource').get()
print('='*30)
print('ИНФОРМАЦИЯ О СИСТЕМЕ')
print('='*30)
print('/system/resource/print')
print('='*30)
print(output, end='\n\n\n')

# ещё можно отправлять команды таким способом
output = api.get_binary_resource('/').call('system/package/print')
print('='*30)
print('УСТАНОВЛЕННЫЕ ПАКЕТЫ RouterOS')
print('='*30)
print('/system/package/print')
print('='*30)
print(output, end='\n\n\n')

# какой-то бред творится со знаком / в методе .call(). то без него ошибка была, то с ним
# на пустом месте усложнили библиотеку, ни с одной другой столько проблем не было
output = api.get_binary_resource('/').call('user/print')
print('='*30)
print('ПОЛЬЗОВАТЕЛИ')
print('='*30)
print('/user/print')
print('='*30)
print(output, end='\n\n\n')

output = api.get_binary_resource('/').call('interface/print')
print('='*30)
print('ПОЛУЧЕНИЕ ВСЕХ ИНТЕРФЕЙСОВ')
print('='*30)
print('/interface/print')
print('='*30)
print(output, end='\n\n\n')

output = api.get_binary_resource('/').call('ip/route/print')
print('='*30)
print('ПОЛУЧЕНИЕ IP-АДРЕСОВ')
print('='*30)
print('/ip/route/print')
print('='*30)
print(output)

connection.disconnect()
