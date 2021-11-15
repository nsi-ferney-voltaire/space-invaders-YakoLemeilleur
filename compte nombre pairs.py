    def trouver_pair (tableau):
        nombre_pair = 0
        for k in tableau:
            if k % 2 == 0:
                return True
            else:
                print(''ceci nest pas un nombre pair'')
        return False
        
    trouve = trouver_pair ([1, 3, 6])
    print(trouve)
            