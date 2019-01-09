import mlab
from river import River
mlab.connect()

# Ex2
africa_river_list = River.objects(continent__icontains="Africa")
for a in africa_river_list:
    print(a.name, end=', ')

print()

# Ex3
america_river_list = River.objects(continent__icontains="S. America", length__lt=1000)
for a in america_river_list:
    print(a.name, end=', ')

print()