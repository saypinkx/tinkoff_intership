
class Bands:
    def __init__(self):
        self.bands = []

    def add_band(self, band):
        self.bands.append(band)

    def remove_band(self, band):
        self.bands.remove(band)

    def is_spirits_in_one_band(self, x, y):
        for band in self.bands:
            if band.is_spirit_in_band(x):
                band1 = band
            if band.is_spirit_in_band(y):
                band2 = band
        if band1 == band2:
            return 'YES'
        return 'NO'

    def union(self, x, y):
        for band in self.bands:
            if band.is_spirit_in_band(x):
                band1 = band
            if band.is_spirit_in_band(y):
                band2 = band

        if band1 != band2:
            self.remove_band(band1)
            self.remove_band(band2)
            band = BandObj()
            band.union_band(band1, band2)
            self.add_band(band)

    def count_band(self, x):
        for band in self.bands:
            for spirit in band.members:
                if spirit.value == x:
                    return spirit.count_bands


class BandObj:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        member.count_bands += 1

    def remove_member(self, member):
        self.members.remove(member)

    def is_spirit_in_band(self, value):
        if Spirit(value) in self.members:
            return True
        return False

    def union_band(self, band1, band2):
        self.members.extend(band1.members)
        self.members.extend(band2.members)
        for member in self.members:
            member.count_bands += 1


class Spirit:
    def __init__(self, value):
        self.value = value
        self.count_bands = 0

    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False

    def __hash__(self):
        return hash(self.value)

    def count(self):
        return self.count_bands


bands = Bands()

n, m = str(input()).split()
n = int(n)
m = int(m)

for i in range(1, n + 1):
    spirit = Spirit(i)
    band = BandObj()
    band.add_member(spirit)
    bands.add_band(band)

dictionary = {
    '1':    bands.union,
    '2':    bands.is_spirits_in_one_band,
    '3':    bands.count_band,
}


for i in range(m):
    s = str(input()).split()
    comand = dictionary[s[0]]
    x = int(s[1])
    if len(s) > 2:
        y = int(s[2])
        if s[0] == '1':
            comand(x, y)
        else:
            print(comand(x, y))
    else:
        print(comand(x))
