class Grafo:
  def __init__(self,V):
    self.V = V
    self.infinito=10000
    self.rotulado=[]
    self.nrotulado=[]
    self.d=[]
    self.p=[]
    self.custo=[]
    i=0
    j=0

    for i in range(V+1):
      self.custo.append([])	
      self.rotulado.append(-2)
      self.nrotulado.append(i)
      self.p.append(V+2);
      self.d.append(self.infinito)
      for j in range(V+1):
        self.custo[i].append(self.infinito)
        if(i==j):
          self.custo[i].append(0)
         



  def addAresta(self,v1, v2, c, tipo):
    if(v1!=0 or v2!=0): 
      if(tipo==1):
        self.custo[v1-1][v2-1]=c
        self.custo[v2-1][v1-1]=c
      else:
        self.custo[v1-1][v2-1]=c

  def dijkstra(self,orig,dest):

      orig=orig-1
      dest=dest-1
      n=self.V
      k=0
      contador=0
      #Passo 1:	
      self.rotulado[orig]=orig
      self.d[orig]=0
      self.p[orig]=0
      self.ultimo=orig
      t=0
      for t in range(n):
        if(self.nrotulado[t]==self.ultimo):
          if(t!=0):
            self.nrotulado[t]=-t
          else:
            self.nrotulado[t]=-1
        
        if (self.nrotulado[t]==t):
          self.d[t]=self.infinito
          self.p[t]=int(n)+1

     #Passo 2:
      while(k!=self.V):
        candidato=0 
        cand=100000
        t=0
        for t in range(n):
          if( t== self.nrotulado[t] ):
            if( int(self.d[t]) <= (int(self.d[self.ultimo]) + int(self.custo[int(self.ultimo)][t])) ):
              print("d("+str(t+1)+") <- "+str(self.d[t])+"")
              #print("")
            else:
              self.d[t]=int(self.d[+self.ultimo]) + int(self.custo[+self.ultimo][t])
              print("d("+str(t+1)+") <- "+str(self.d[t])+"")
              if(self.d[t]<self.infinito):
                self.p[t]=int(self.ultimo)+1
              
            
            if(self.d[t]<=cand):
              cand=+self.d[t]
              candidato=t
            
            if(self.d[t]==self.infinito):
              contador+=1

        k+=1
        if(candidato!=0):
          self.nrotulado[candidato]=-candidato
          self.rotulado[candidato]=candidato
        else:
            self.nrotulado[candidato]=-1
            self.rotulado[candidato]=0
        
        self.d[candidato]=cand
        self.ultimo = candidato


      #Passo 3
      self.element=""
      self.cm=0
      if(self.nrotulado[dest]==-dest):
        i=dest
        self.element1="C = {"
        while(i!=orig):
          if((self.p[i]-1)==orig):
            self.element="("+str(self.p[i])+","+str(i+1)+")"+self.element
          else:
            self.element="("+str(self.p[i])+","+str(i+1)+")"+self.element
          i=self.p[i]-1		
        
        self.element=self.element1+self.element+"}"
        self.cm=self.d[dest]
      else:
        self.element="Caminho indisponível!"


  def retornaValorCusto(self):
      return self.cm


  def retornaValorRota(self):
      return self.element
