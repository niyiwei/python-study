import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = "Oeoykatuibs if Countries in North America"
wm.add("North Americs", {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.add("Asia", {'cn': 1312345678})

wm.render_to_file('na_populations.svg')
