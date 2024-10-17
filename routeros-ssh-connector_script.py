from routeros_ssh_connector import MikrotikDevice

router = MikrotikDevice()
router.connect('localhost', 'admin', 'admin', '2222')

output = router.send_command('/system/resource/print')
print('='*30)
print('ИНФОРМАЦИЯ О СИСТЕМЕ')
print('='*30)
print('/system/resource/print')
print('='*30)
print(output, end='\n\n\n')

output = router.send_command('/system/package/print')
print('='*30)
print('УСТАНОВЛЕННЫЕ ПАКЕТЫ RouterOS')
print('='*30)
print('/system/package/print')
print('='*30)
print(output, end='\n\n\n')

output = router.send_command('/user/print')
print('='*30)
print('ПОЛЬЗОВАТЕЛИ')
print('='*30)
print('/user/print')
print('='*30)
print(output, end='\n\n\n')

output = router.send_command('/interface/print')
print('='*30)
print('ПОЛУЧЕНИЕ ВСЕХ ИНТЕРФЕЙСОВ')
print('='*30)
print('/interface/print')
print('='*30)
print(output, end='\n\n\n')

output = router.send_command('/ip/route/print')
print('='*30)
print('ПОЛУЧЕНИЕ IP-АДРЕСОВ')
print('='*30)
print('/ip/route/print')
print('='*30)
print(output)

router.disconnect()
