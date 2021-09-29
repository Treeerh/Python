#   6. Продолжить работу над вторым заданием.
#   Реализуйте механизм валидации вводимых пользователем данных.
#   Например, для указания количества принтеров, отправленных на склад,
#   нельзя использовать строковый тип данных.
#   Подсказка: постарайтесь реализовать в проекте
#   «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

# Разбор
from abc import ABC, abstractmethod
import json


class Warehouse:
    devices_in_warehouse = {'Printer': [], 'Scanner': [], 'Copier': []}
    user_devices = {'Printer': [], 'Scanner': [], 'Copier': []}

    @classmethod
    def to_warehouse(cls, *devices, from_user=False):
        if not from_user:
            for device in devices:
                cls.devices_in_warehouse[str(device.__class__.__name__)].append(device)
                print(device, 'Принято на склад.')
        else:
            for device in devices:
                cls.user_devices[str(device.__class__.__name__)].remove(device)
                cls.devices_in_warehouse[str(device.__class__.__name__)].append(device)
                print(device, 'Принято на склад.')

    @classmethod
    def from_warehouse(cls, device):
        cls.devices_in_warehouse[str(device.__class__.__name__)].remove(device)
        cls.user_devices[str(device.__class__.__name__)].append(device)
        print(device, 'Передано со склада.')

    @staticmethod
    def json_export():
        ware_dev_for_exp = {}
        ware_list_for_exp = []
        for key in Warehouse.devices_in_warehouse.keys():
            ware_list = []
            for value in Warehouse.devices_in_warehouse[key]:
                if value:
                    ware_list.append(value.get_info())
            if ware_list:
                ware_list.append({'Количество': len(ware_list)})
            ware_dev_for_exp = {key: ware_list} if ware_list else None
            if ware_dev_for_exp:
                ware_list_for_exp.append(ware_dev_for_exp)
        ware_dev_for_exp = {'Устройства на складе': ware_list_for_exp}

        user_dev_for_exp = {}
        user_list_for_exp = []

        for key in Warehouse.user_devices.keys():
            ware_list = []
            for value in Warehouse.user_devices[key]:
                if value:
                    ware_list.append(value.get_info())
            if ware_list:
                ware_list.append({'Количество': len(ware_list)})
            user_dev_for_exp = {key: ware_list} if ware_list else None
            if user_dev_for_exp:
                user_list_for_exp.append(user_dev_for_exp)
        user_dev_for_exp = {'Устройства у пользователей': user_list_for_exp}
        with open('l8_task6.json', 'w', encoding='utf-8') as out_file:
            json.dump([ware_dev_for_exp, user_dev_for_exp], out_file, indent=4, ensure_ascii=False)

    def __str__(self):
        string_warehouse = '\n'.join(map(str, (sum(self.devices_in_warehouse.values(), []))))
        string_warehouse = 'Устройства на складе:\n' + string_warehouse if string_warehouse else 'На складе нет устройств'
        string_user = '\n'.join(map(str, (sum(self.user_devices.values(), []))))
        string_user = 'Устройства у пользователей:\n' + string_user if string_user else 'У пользователей устройств'
        return string_warehouse + '\n' + string_user


class Device(ABC):
    def __init__(self, brand, serial):
        self._owner = 'зав.складом'
        if Device.valid_device(brand, serial, self._owner):
            self._brand = brand
            self._serial = serial
            Warehouse.to_warehouse(self)

    def __str__(self):
        return 'Устройство {}, номер {}, ответственный {}.'.format(self._brand, self._serial, self._owner)

    def get_info(self):
        return {'Модель': self._brand, 'Ответственный': self._owner, 'Инвентарный номер': self._serial}

    def change_owner(self, owner='зав.складом'):
        if Device.valid_owner(owner):
            print('Устройство {} переписано с {} на {}.'.format(self._brand, self._owner, owner))
            self._owner = owner
            if self._owner == 'зав.складом':
                Warehouse.to_warehouse(self, from_user=True)
            else:
                Warehouse.from_warehouse(self)

    @classmethod
    def how_mush_devices(cls, device='All'):
        if str(device) == 'All':
            string_warehouse = {key: len(value) for key, value in Warehouse.devices_in_warehouse.items()}
            string_user = {key: len(value) for key, value in Warehouse.user_devices.items()}
        else:
            string_warehouse = {device: len(Warehouse.devices_in_warehouse[device])}
            string_user = {device: len(Warehouse.user_devices[device])}
        string_warehouse = 'Устройства на складе:\n' + '\n'.join(
            '{}: {}'.format(key, value) for key, value in string_warehouse.items()) + '\nИтого: ' + str(
            sum(string_warehouse.values()))
        string_user = 'Устройства у пользователей:\n' + '\n'.join(
            '{}: {}'.format(key, value) for key, value in string_user.items()) + '\nИтого: ' + str(
            sum(string_user.values()))
        return string_warehouse + '\n' + string_user

    @abstractmethod
    def work(self):
        print('Устройство {}, номер {} находится на складе.'.format(self._brand, self._serial))

    @staticmethod
    def valid_owner(owner):
        try:
            with open('l8_task6_workers.txt', encoding='utf-8') as f:
                flag = 0
                for line in f.readlines():
                    if owner in line:
                        flag = 1
                        return True
                if not flag:
                    raise ValueError(f'Ошибка! Сотрудника {owner} нет на предприятии.')
        except ValueError as ex:
            print(ex)
            return False

    @staticmethod
    def valid_device(brand, serial, owner):
        if not Device.valid_owner(owner):
            return False
        try:
            with open('l8_task6_brands.txt', encoding='utf-8') as f:
                flag = 0
                for line in f.readlines():
                    if brand in line:
                        flag = 1
                        break
                if not flag:
                    raise ValueError(f'Ошибка! Марки устройства {brand} нет в перечне.')
            for value in sum(Warehouse.devices_in_warehouse.values(), []):
                if serial == value._serial:
                    raise ValueError(f'Ошибка! Устройство с инвентарным номером {serial} уже есть в БД.')
            for value in sum(Warehouse.user_devices.values(), []):
                if serial == value._serial:
                    raise ValueError(f'Ошибка! Устройство с инвентарным номером {serial} уже есть в БД.')
        except ValueError as ex:
            print(ex)
            return False
        else:
            return True


class Printer(Device):
    def work(self):
        if self._owner == 'зав.складом':
            super().work()
        else:
            print('Устройство печатает.')

    @classmethod
    def how_mush_devices(cls, device='Printer'):
        return super().how_mush_devices(device)


class Scanner(Device):
    def work(self):
        if self._owner == 'зав.складом':
            super().work()
        else:
            print('Устройство сканрует.')

    @classmethod
    def how_mush_devices(cls, device='Scanner'):
        return super().how_mush_devices(device)


class Copier(Device):
    def work(self):
        if self._owner == 'зав.складом':
            super().work()
        else:
            print('Устройство копирует.')

    @classmethod
    def how_mush_devices(cls, device='Copier'):
        return super().how_mush_devices(device)


def main():
    print(Warehouse())
    printer = Printer('Kyocera', 101)
    scanner = Scanner('НР', 102)
    copier = Copier('Xerox', 103)
    Printer('Canon', 104)
    Printer('Printer', 105)
    Printer('Canon', 102)
    print('******************************')
    copier.work()
    print('******************************')
    print(Warehouse())
    print('******************************')
    printer.change_owner('Валентин Валентинов')
    print('******************************')
    print(Warehouse())
    print('******************************')
    copier.change_owner('Людвиг Ваныч')
    print('******************************')
    copier.work()
    print('******************************')
    scanner.change_owner('Кузнец Вакула')
    print('******************************')
    printer.change_owner()
    print('******************************')
    print(Warehouse())
    print('******************************')
    print(Device.how_mush_devices())
    print('******************************')
    print(printer.how_mush_devices())
    Warehouse.json_export()


if __name__ == '__main__':
    main()
