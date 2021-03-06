import webbrowser

class Gmap:

    def __init__(self):
        pass

    @staticmethod
    def open(place1, place2=''):
        if place2 == '':
            webbrowser.open('https://www.google.co.in/maps/place/'+place1)
        else:
            webbrowser.open('https://www.google.co.in/maps/dir/'+place1+'/'+place2)
    
    def restaurants(place=''):
        if place == '':
            webbrowser.open('https://www.google.co.in/maps/search/restaurants+nearby')
        else:
            webbrowser.open('https://www.google.co.in/maps/place/restaurants+near+'+place)