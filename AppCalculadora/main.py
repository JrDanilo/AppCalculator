import kivy
from kivy.app import App
from kivy.app import Widget
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition #importando funcoes do kivy

Window.size = (400,600) #Definindo tamanho da tela do app

class TelaInicial(Screen): #classe da tela inicial
    pass

class FuncaoAfim(Screen): #classe da funcao afim
    pass

class FuncaoQuadratica(Screen): #classe da funcao Quadratica
    pass

class FuncaoExponencial(Screen): #classe da funcao Exponencial
    pass

class FuncaoLogaritmica(Screen): #classe da funcao Logaritmica
    pass

class FuncaoSeno(Screen): #classe da funcao Seno
    pass

class FuncaoCosseno(Screen): #classe da funcao Cosseno
    pass

class TelaAjuda(Screen): #classe da tela ajuda
    pass

class MudancaDeTelas(ScreenManager): #classe que muda as telas
    def mudar_para_telaInicial(self): #metodo que muda para pagina inicial
        self.current = 'telaInicial'

    def mudar_para_funcaoAfim(self): #metodo que muda para o label secundario
        self.current = 'funcaoAfim'

    def mudar_para_funcaoQuadratica(self):
        self.current = 'funcaoQuadratica'

    def mudar_para_funcaoExponencial(self):
        self.current = 'funcaoExponencial'

    def mudar_para_funcaoLogaritmica(self):
        self.current = 'funcaoLogaritmica'

    def mudar_para_funcaoSeno(self):
        self.current = 'funcaoSeno'

    def mudar_para_funcaoCosseno(self):
        self.current = 'funcaoCosseno'

    def mudar_para_ajuda(self): #metodo que muda para a tela ajuda
        self.current = 'telaAjuda'

class calculadoraApp(App): #construindo classe do app
    def build(self):
        self.title = 'Calculadora da Area sob Curva'
        self.root = MudancaDeTelas()
        return self.root

meuApp = calculadoraApp() 

meuApp.run() #rodando app
