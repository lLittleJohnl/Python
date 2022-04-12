import pyautogui as pyg

def login_check():
    
    pyg.hotkey('ctrl', 'a')
    pyg.hotkey('ctrl', 'c')
    check1 = pyg.hotkey('ctrl','v')
    if check1 != 0:
        pass
    else:
        print('O erro ocorreu no preenchimento das informações')

pyg.PAUSE = 1.5
pyg.alert("Entrando no sistema")
pyg.press('winleft')
pyg.typewrite('chrome')
pyg.press('enter')
pyg.typewrite('https//www.google.com')
pyg.press('enter')
pyg.click(x=1021, y=137)
pyg.click(x=393, y=447)
pyg.typewrite('joaovitorpessoa10@gmail.com')
login_check()
pyg.press('enter')
pyg.typewrite('jvcp74128581')
pyg.press('enter')
print('Login realizado com sucesso')
