#
# Proto
#
#
import json
import nano_ioc

env = 'local'

with open('config-{}.json'.format(env)) as file:
    json_configuration = file.read()
configuration = json.loads(json_configuration)
container = nano_ioc.Container(configuration)

storage = container.getService('Storage')

res = storage.hasDocument('test', 'fichier1.txt')
print(res)
storage.writeDocument('test', 'fichier1.txt', 'Blabla')
res = storage.hasDocument('test', 'fichier1.txt')
print(res)

res = storage.readDocument('test', 'fichier1.txt')
print(res)

storage.removeDocument('test', 'fichier1.txt')
res = storage.hasDocument('test', 'fichier1.txt')
print(res)


def printHook(data, argv):
    print(data)
    print(argv)

hook = container.getService('Hook')

hook.add_action('test', printHook, [42])

hook.do_action('test', 12)

