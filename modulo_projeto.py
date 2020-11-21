from tkinter import *

class Frameinicial(Frame):

	def __init__(self, parent):
		'''Função construtora da classe, cria o frame inicial
		   aonde o úsuario pode definir o nome da equipe e
		   quantos jogadores ela terá

		   param parent: master da frame'''

		super().__init__()

		self['bg'] = 'white'
		
		def cadastroequipe():
			if nomeequipe.get().replace(' ', '').isalpha():
				self.destroy()
				Framejogadores(parent = self,
					           nomeequipe = nomeequipe.get(),
					           qtdejogadores = qtdejogadores.get()).place(x = 240, y = 130)
			else:
				label_aviso['text'] = 'Erro!! nome da equipe ínvalido'
		
		
		nomeequipe = StringVar() #Nome da equipe
		qtdejogadores = IntVar() #Quantidade de jogadores que ela terá
		qtdejogadores.set(11)

		#Label para nome da equipe
		label_nome = Label(master = self,
	 		               text = 'Nome da equipe: ',
	 		               font = 'Times 20',
	 		               width = 30,
	 		               bg = 'white')

		#Label para quantidade de jogadores
		label_qtde = Label(master = self,
	 		               text = 'Quantidade de jogadores: ',
	 		               font = 'Times 20',
	 		               width = 30,
	 		               bg = 'white')

		#Label para avisar sobre erros cometidos pelo úsurio
		label_aviso = Label(master = self,
							font = 'Times 20',
							bg = 'white')

		#Digite o nome da equipe
		nome_equipe = Entry(master = self,
			                font = 'Times 15',
			                width = 40,
			                textvariable = nomeequipe)

		#Defina a quantidade de jogadores que serão cadastrados
		qtde_jogadores = Scale(master = self,
	 		                   from_= 11,
	 		                   to = 20,
	 		                   orient= HORIZONTAL,
	 		                   bg = 'white',
	 		                   variable = qtdejogadores)
		
		#Siga para a frame de cadastro dos jogadores
		btn_cadastrar = Button(master = self,
			                   text = 'Cadastro de Jogadores',
			                   font = 'Times 20',
			                   bd = 5,
			                   relief = 'raised',
			                   command = lambda: cadastroequipe())

		label_nome.grid(row = 0, column = 0)
		nome_equipe.grid(row = 0, column = 1)
		label_qtde.grid(row= 1, column = 0)
		qtde_jogadores.grid(row = 1, column = 1, sticky = 'WE')
		label_aviso.grid(row = 2 , columnspan = 2, sticky = 'WE')
		btn_cadastrar.grid(row = 3, column = 1, sticky = 'WE')



class Framejogadores(Frame):
	def __init__(self, parent, nomeequipe, qtdejogadores):
		'''Função Construtora da Classe, cria o frame para o
		   úsuario cadastrar os jogadores da equipe

		   param parent: master da frame

		   param nomeequipe: nome da equipe

		   param qtdejogadores: quantidade de jogadores que serão cadastrados'''
		
		super().__init__()

		self['bg'] = 'white'

		self.posicoes = ['GOL','ZAG','LTE','LTD','MEI','ATQ'] #Posição dos jogadores 
		self.pos = 0 #Variável que navegara na lista de posicoes
		
		self.nome_jogador = StringVar()#Nome do jogador
		self.pos_jogador = StringVar() #Posição do jogador
		self.pos_jogador.set('GOL')

		self.cadastrados = IntVar() #Quantidade de jogadores cadastrados
		
		#Label para nome da equipe
		label_equipe = Label(master = self,
							 text = f'Nome da equipe: ',
							 font = 'Times 15',
							 bg = 'white',
							 width = 30)
		label_nomeequipe = Label(master = self,
								text = nomeequipe,
								font = 'Times 15',
								bg = 'white',
								width = 20)

		#Label para jogadores cadastrados
		label_cadastrados = Label(master = self,
								  text = f'Jogadores cadastrados: ',
								  font = 'Times 15',
								  bg = 'white')
		
		#Quantidade de jogadores cadastrados
		label_cadastros = Label(master = self,
			   	                textvariable = self.cadastrados,
			   	                bg = 'white')

		#Label para nome do jogador
		label_nome = Label(master = self,
			               text = 'Nome do jogador: ',
			               font = 'Times 15',
			               bg = 'white')
		
		#Digite o nome do jogador
		text_nome = Entry(master = self,
			     	  	  font = 'Times 12',
			     	  	  bg = 'white',
			     	  	  textvariable = self.nome_jogador)

		#Posição selecionada pelo úsuario
		self.label_pos = Label(master = self,
			    	      text = self.posicoes[0],
			    	      font = 'Times 15',
			    	      bd = 5,
			    	      width = 15,
			    	      relief = 'raised')

		#Voltar para a posição anterior
		pos_anterior = Button(master = self,
			     	          text = '<',
			     	          bd = 5,
			     	          relief = 'raised',
			     	          width = 5,
			     	          command = lambda: self.posicao('-'))
	    #Próxima posição
		pos_proxima = Button(master = self,
			    	         text = '>',
			    	         bd = 5,
			    	         width = 5,
			    	         relief = 'raised',
			    	         command = lambda: self.posicao('+'))
		
		#Usado para ajuda na apresentação do dados da listbox
		label_info = Label(master = self,
			   	    	   text = f'{"Nome":<30}{"Posição":>30}',
			   	    	   bd = 1,
			   	    	   font = 'Times 15',
			   	    	   relief = 'solid')
		
		#Mostra os jogadores cadastrados
		self.listbox = Listbox(master = self,
			    	      bd = 1,
			    	      relief = 'solid',
			    	      font = 'Times 12')

		#Adicionar dado a Listbox
		btn_adicionar = Button(master = self,
			   	   	    	   text = 'ADD',
			   	   	    	   font = 'Times 12',
			   	   	    	   bd = 5,
			   	   	    	   relief = 'raised',
			   	   	    	   command = lambda: self.adicionar(qtdejogadores))
		
		#Remover dado da Listbox
		btn_apagar = Button(master = self,
			   	   	        text = 'DEL',
			   	   	        font = 'Times 12',
			   	   	        bd = 5,
			   	   	        relief = 'raised',
			   	   	        command = lambda: self.apagar())

		#Cadastrar equipe
		btn_cadastrar = Button(master = self,
			  	   	           text = 'SALVAR',
			  	   	           font = 'Times 12',
			  	   	           bd = 5,
			  	   	           relief = 'raised',
			  	   	           command = lambda: self.cadastrar(qtdejogadores))
		
        #Voltar para o inicio
		btn_voltar = Button(master = self,
							text = 'VOLTAR',
							font = 'Times 12',
							bd = 5,
							relief = 'raised',
							command = lambda: self.voltar())

		self.label_aviso = Label(master = self,
								 font = 'Times 12',
								 bd = 5,
								 relief = 'raised')						                 			                 
        
        #Dados da equipe
		label_equipe.grid(row = 0,column = 0)
		label_nomeequipe.grid(row = 0, column = 1)
		label_cadastrados.grid(row = 1, column = 0, sticky = 'WE')
		label_cadastros.grid(row = 1,  column = 1, sticky = 'WE')
        
        #Definição do nome
		label_nome.grid(row = 2, column = 0)
		text_nome.grid(row = 2, column = 1, sticky = 'WE')
        
        #Definição da Posição
		pos_anterior.grid(row = 2, column = 2, sticky = E)
		self.label_pos.grid(row = 2, column = 3)
		pos_proxima.grid(row = 2, column = 4)
		
		#Adicionar e apagar dados da listbox
		btn_adicionar.grid(row = 3, column = 3, columnspan = 2, sticky = 'WE')
		btn_apagar.grid(row = 4, column = 3, columnspan = 2, sticky = 'WE')
		
		#Apresentação dos dados
		label_info.grid(row = 5, columnspan = 5, sticky = 'WE')
		self.listbox.grid(row = 6, columnspan =  5, sticky = 'WE')

		#Avisos sobre erros ou operações concluídas
		self.label_aviso.grid(row = 7, columnspan = 5, sticky = 'WE')

		#Volta para o inicio e salvar dados dos jogadores
		btn_voltar.grid(row = 8, column = 0, sticky = 'W')
		btn_cadastrar.grid(row = 8, column = 3, columnspan = 2, sticky = 'WE')

	
	#Funções utilizadas na classe
	def posicao(self, sentido):
			'''Função utilizada para definir a posição do jogador
			   que será cadastrado

			   param sentido: se for igual a + vai a próxima posição

			                  se for igual a - volta para a posição anterior'''
			
			if sentido == '+':
				if not self.pos == len(self.posicoes) - 1:
					self.pos += 1
				else:
					self.pos = 0
			
			elif sentido == '-':
				if self.pos == 0:
					self.pos = len(self.posicoes) - 1
				else:
					self.pos -= 1	
			self.label_pos['text'] = self.posicoes[self.pos]
			self.pos_jogador.set(self.posicoes[self.pos])

	
	def formatar(self, nome, posicao):
			'''Formata os dados digitados pelo úsuario,
			   para que sejam melhor apresentados na Listbox

			   param nome: nome do jogador

			   param posicao: posicao do jogador'''
			
			return f'{nome:>65}\t{posicao:>68}'

			
	def adicionar(self, qtdejogadores):
			'''Função utilizada para adicionar o nome do jogador e
			   sua posição ao Listbox Widget'''

			if not self.cadastrados.get() == qtdejogadores:
				
				if self.nome_jogador.get().isalpha(): #Se o nome do jogador só tiver letras
					jogador = self.formatar(self.nome_jogador.get(), self.pos_jogador.get())
					jogadores = self.listbox.get(0, END)
					if not jogador in jogadores:
						self.listbox.insert(END, jogador)
						self.nome_jogador.set('')
						self.cadastrados.set(self.cadastrados.get() + 1)
				
					else:
						self.label_aviso['text'] = 'Erro!! este jogador já foi cadastrado'

			
				else: #Se o nome do jogador não tiver somente letras
					self.label_aviso['text'] = 'Erro!! o nome do jogador deve ter apenas letras'

			else:
				self.label_aviso['text'] = 'Erro!! a quantidade de jogadores definida já foi cadastrada'		

	
	def apagar(self):
			'''Funçao utilizada para remover o dado selecionado pelo úsuario
			   da Listbox Widget'''
			
            #Separa o dado que será apagado para pega a posição do jogador
			dado = self.listbox.get(ACTIVE).split()
			
			if not len(dado) == 0: #Se o úsuario selecionar um dado para apagar
				
				#Pega a posição do jogador que será apagado e a define como posição para o próximo jogador
				self.pos = self.posicoes.index(dado[1])
				self.label_pos['text'] = self.posicoes[self.pos]
			
				self.pos_jogador.set(self.posicoes[self.pos])
				
				#Apaga o jogador da Listbox Widget
				self.listbox.delete(ACTIVE)
				self.cadastrados.set(self.cadastrados.get() - 1)
			
			else: #Se o úsuario selecionar um dado vazio
				self.label_aviso['text'] = 'Erro!! Não a nada para apagar'

	

	def validacao(self, jogadores):
			'''Função utilizada para verificar se o time tem a quantidade de jogadores
			   necessária para cada posição

			   param jogadores: jogadores cadastrados

			   return: True se sim, e False se não'''
			
			posicoes = (('GOL', 1), ('ZAG', 2), ('LTE', 1), ('LTD', 1), ('MEI', 3), ('ATQ', 3))#posicoes e quantidades necessárias
			for p in posicoes:
				cont = 0 #contador de posições
				valida = False #Validação da quantidade para cada posição
				
				for jogador in jogadores:
					jogador = jogador.split()
					if jogador[1] == p[0]:
						cont += 1
					if cont == p[1]:
						valida = True
						break
				
				if valida == False:
					return f'Erro!! adicione {p[1]-cont} jogador(es) na posição {p[0]}'

			return True

	
	def cadastrar(self, qtdejogadores, nomeequipe):
			'''Função utilizada para fazer o cadastro de todos os jogadores,
			   de acordo com a quantidade de jogadores que serão cadastrados'''
			
			#Cadastro de jogadores
			jogadores = self.listbox.get(0,END)
			valida = self.validacao(jogadores) #Validação para ver se o time tem a quantidade de jogadores necessária para cada posição
			
			if len(jogadores) == qtdejogadores and valida == True:
				
				with open('equipe.txt', 'w') as equipe:
					equipe.write(f'Nome da eqipe: {nomeequipe}')
					equipe.write(f'Jogadores cadastrados: {qtdejogadores}')
					
					for i,j in enumerate(jogadores):
						equipe.write(f'{i} - {j}' + '\n')
				
				#Limpa a ListBox Widget
				self.listbox.delete(0, END)
			
			else:
				self.label_aviso['text'] = valida

	def voltar(self):
			'''Função utilizada para voltar ao ínicio do programa'''
			self.destroy()
			Frameinicial(parent = self).place(x = 240, y = 130)			