tower =  {'A':set(['B','C','D']),
         'B':set(['E','F','C']),
         'C':set(['B','F','D']),
         'D':set(['C','F','G']),
         'E':set(['J','H','F']),
         'F':set(['E','H','K','I','G','B','C','D']),
         'G':set(['F','I','L']),
         'H':set(['E','F','K','J']),
         'I':set(['F','G','L','K']),
         'J':set(['E','H','K','M','N']),
         'K':set(['F','I','L','O','N','M','J','H']),
         'L':set(['G','I','K','N','O']),
         'M':set(['J','K','N','P','R']),
         'N':set(['J','K','L','O','Q','S','P','M']),
         'O':set(['L','K','N','Q','T']),
         'P':set(['M','N','S','R']),
         'Q':set(['N','O','T','S']),
         'R':set(['M','P','S','U']),
         'S':set(['R','P','N','Q','T','W','V','U']),
         'T':set(['O','Q','S','W']),
         'U':set(['R','S','V']),
         'V':set(['U','S','W']),
         'W':set(['T','S','V'])}
    

def courier(tower, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
        jalur = queue.pop(0)
        state = jalur[-1]

        if state == tujuan:
            return jalur
        elif state not in visited:
            for cabang in tower.get(state, []):
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                queue.append(jalur_baru) 
            visited.add(state)

        isi = len(queue)
        if isi == 0:
            print("Tidak bisa dilewati courier")
