class Resourse:
    def __init__(self, name, manufacturer, total, allocated, available):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated
        self._available = available
        self._category = None

    @property
    def name(self):
        return self._name
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def available(self):
        return self._available
    
    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Name: {self.name} - Manufacturer: {self.manufacturer} - Total: {self.total} - Allocated: {self.allocated} - Available: {self.available}'

    def claim(self, n):
        if not isinstance(n, int) or n <= 0:
            print('Not possible claim, it must be an integer more than cero.')
            return NotImplemented
        
        if self.available < n:
            print('Not possible claim, not enought in inventory available.')
            return NotImplemented

        self._available -= n
        self._allocated += n
        print(f'Total {str(self)} decreased {n} resulting on {self.available} available.')

    def freeup(self, n):
        if not isinstance(n, int) or n <= 0:
            print('Not possible freeup, it must be an integer more than cero.')
            return NotImplemented

        if self._allocated < n:
            return ValueError('Not possible, total inventory is less than elements to freeup.')

        self._available += n
        self._allocated -= n
        print(f'Total {str(self)} increased {n} resulting on {self.available} available.')

    def died(self, n, status='allocated'):
        if not isinstance(n, int) or n <= 0:
            print('Not possible died, it must be an integer more than cero.')
            return NotImplemented

        if status == 'allocated':
            if self._allocated < n:
                return ValueError('Not possible, total inventory is less than elements to died.')
            
            self._allocated -= n
            print(f'{str(self)} decreased {self.allocated} allocated.')

        if status == 'available':
            if self._available < n:
                return ValueError('Not possible, total inventory is less than elements to died.')
            
            self._available -= n
            print(f'{str(self)} decreased {self.available} available.')

        self._total -= n
        print(f'Total {str(self)} decreased {n} resulting on {self.total} total (available and allocated).')

    def purchase(self, n):
        if not isinstance(n, int) or n <= 0:
            print('Not possible purchase, it must be an integer more than cero.')
            return NotImplemented
        
        self._total += n
        self._available += n
        print(f'Total {str(self)} increased by purchase {n} resulting on {self.available} available.')

    @property
    def category(self):
        if self._category is None:
            self._category = self.__class__.__name__.lower()
            return self._category
        
        return self._category


class Cpu(Resourse):
    def __init__(self, name, manufacturer, total, allocated, available, cores, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated, available)
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts
    
    def __str__(self):
        return f'{self.name} // {self.__class__.__name__}'

    def __repr__(self):
        return f'Name: {self.name} - Manufacturer: {self.manufacturer} - Total: {self.total} - Allocated: {self.allocated} - Available: {self.available} - Cores: {self.cores} - Socket: {self.socket} - Power Watts: {self.power_watts}'


class Storage(Resourse):
    def __init__(self, name, manufacturer, total, allocated, available, capacity_GB):
        super().__init__(name, manufacturer, total, allocated, available)
        self._capacity_GB = capacity_GB
    
    @property
    def capacity_GB(self):
        return self._capacity_GB
    

class Ssd(Storage):
    def __init__(self, name, manufacturer, total, allocated, available, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, available, capacity_GB)
        self._interface = interface

    @property
    def interface(self):
        return self._interface
    
    def __str__(self):
        return f'{self.name} // {self.__class__.__name__}'

    def __repr__(self):
        return f'Name: {self.name} - Manufacturer: {self.manufacturer} - Total: {self.total} - Allocated: {self.allocated} - Available: {self.available} - Capacity Gb: {self.capacity_GB} - Inteface: {self.interface}'


########################################################################################

test = Resourse('Intel Core i9-9900K', 'Nvidia', 100, 25, 75)

print(test.__dict__)

print(test.name, '//', test.manufacturer, '//', test.total, '//', test.allocated)

try:
    test.name = 'Other'
except:
    print('Not possible changes test.name')

try:
    test.manufacturer = 'Other'
except:
    print('Not possible changes test.manufacturer')

try:
    test.total = 'Other'
except:
    print('Not possible changes test.total')

try:
    test.allocated = 'Other'
except:
    print('Not possible changes test.allocated')

print(str(test))
print(repr(test))

test.claim(150)
test.claim(0)
test.claim(10)
print(test.__dict__)

test.freeup(-30)
test.freeup(30)
print(test.__dict__)

test.died(0, 'available')
test.died(5, 'allocated')
print(test.__dict__)

test.purchase(0)
test.purchase(50)
print(test.__dict__)

print(test.category)
print(test.__dict__)

test = Resourse('Intel Core i7', 'Nvidia', 100, 25, 75)

print(test.__dict__)
print(test.category)


test = Cpu('Intel Core', 'Nvidia', 100, 25, 75, 8 , 'AM4', 94)

print(test.__dict__)
print(str(test))
print(repr(test))
print(test.category)


test = Ssd('Intel Core', 'Nvidia', 100, 25, 75, 120, 'PCIe NVMe 3.0 x4')

print(test.__dict__)
print(str(test))
print(repr(test))
print(test.category)
