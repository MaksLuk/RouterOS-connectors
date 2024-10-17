import netmiko
from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type='mikrotik_routeros',
    host='localhost',
    port='2222',
    username='admin',
    password='admin'
)

output = sshCli.send_command('/system/resource/print')
print('='*30)
print('ИНФОРМАЦИЯ О СИСТЕМЕ')
print('='*30)
print('/system/resource/print')
print('='*30)
print(output, end='\n\n\n')

output = sshCli.send_command('/system/package/print')
print('='*30)
print('УСТАНОВЛЕННЫЕ ПАКЕТЫ RouterOS')
print('='*30)
print('/system/package/print')
print('='*30)
print(output, end='\n\n\n')

output = sshCli.send_command('/user/print')
print('='*30)
print('ПОЛЬЗОВАТЕЛИ')
print('='*30)
print('/user/print')
print('='*30)
print(output, end='\n\n\n')

output = sshCli.send_command('/interface/print')
print('='*30)
print('ПОЛУЧЕНИЕ ВСЕХ ИНТЕРФЕЙСОВ')
print('='*30)
print('/interface/print')
print('='*30)
print(output, end='\n\n\n')

output = sshCli.send_command('/ip/route/print')
print('='*30)
print('ПОЛУЧЕНИЕ IP-АДРЕСОВ')
print('='*30)
print('/ip/route/print')
print('='*30)
print(output)

sshCli.disconnect()
