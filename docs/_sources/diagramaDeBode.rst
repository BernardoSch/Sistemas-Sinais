============================================================
Resposta de Sistemas a Entradas Senoidais e Diagrama de Bode
============================================================

Resposta de Sistemas a Entradas Senoidais
=========================================

Considerando um sistema descrito pela função de transferência 

.. math::
	H(s)=\frac{P(s)}{Q(s)}=\frac{P(s)}{(s-\lambda_1)\dots(s-\lambda_n)},

a resposta :math:`y(t)` desse sistema, para uma entrada exponencial complexa

.. math::
	x(t)=e^{jwt}u(t) ,

pode ser obtida utilizando a transformada de Laplace de :math:`X(s)` de :math:`x(t)`, calculando a transformada inversa de 

.. math::
	Y(s)=H(s)X(s).

A transformada de Laplace unilateral, :math:`X(s)`, de :math:`x(t)` é

.. math::
	X(s)=\frac{1}{s-j\omega},
	
com isso 

.. math::
	Y(s)=H(s)X(s)=\frac{P(s)}{(s-\lambda_1)\dots(s-\lambda_n)(s-j\omega)}.
	
Obtendo a expansão de :math:`Y(s)` por frações parciais, obtemos

.. math::
	Y(s)=\sum_{i=1}^{n}\frac{k_i}{s-\lambda_i}+\frac{P(s)}{Q(s)}\Bigg|_{s=j\omega} \frac{1}{s-j\omega}=\sum_{i=1}^{n}\frac{k_i}{s-\lambda_i}+H(j\omega)\frac{1}{s-j\omega}.
	
A saída do sistema para essa entrada exponencial é

.. math::
	y(t)=\sum_{i=1}^{n}k_i e^{\lambda_i t}+H(j\omega)e^{j\omega t}, \hspace{1cm} t\ge 0.
	
a qual é composta por dois termos.

O primeiro termo é a componente que define o regime transitório da resposta, a qual tende a zero quando o tempo tende a infinito, já que

.. math::
	\lim_{t\rightarrow  \infty}\sum_{i=1}^{n}k_i e^{\lambda_i t}=0 ,
	
considerando que o sistema é BIBO estável. 

Já a segunda parcela é o componente que define o comportamento durante o regime permanente de :math:`y(t)`, pois

.. math::
	\lim_{t\rightarrow  \infty}y(t)=\lim_{t\rightarrow  \infty}\sum_{i=1}^{n}k_i e^{\lambda_i t}+\lim_{t\rightarrow  \infty}H(j\omega)e^{j\omega t}, \hspace{1cm} t\ge 0.

e :math:`\lim_{t\rightarrow  \infty}\sum_{i=1}^{n}k_i e^{\lambda_i t}=0`, fazendo com que, em regime permanente, a saída seja definida por

.. math::
	y_{ss}(t)=H(j\omega)e^{j\omega t}, \hspace{1cm} t\ge 0.

Dessa forma, se aplicarmos uma entrada exponencial complexa em um sistema LTI, a saída, em regime permanente, será uma exponencial complexa. Da mesma forma, se aplicarmos um sinal periódico senoidal como entrada de um sistema dinâmico, podemos mostrar que a saída do sistema terá também uma forma periódica senoidal. Considerando 

.. math::
	x(t)=Acos(\omega t + \theta)u(t)=A \operatorname{Re} [e^{j\omega t}e^{j\theta}]u(t) ,
	
onde :math:`A>0` representa a amplitude do sinal, :math:`\omega\geq 0` representa a frequência angular (em rad/s), e :math:`\delta` representa a fase do sinal (em rad).	
	
Considerando que :math:`h(s)` é representado na forma polar como

.. math::
	H(s)=|H(h)| e^{j\angle H(j\omega)}, 
	
a saída :math:`y(t)` do sistema, em regime permanente, pode ser representada como

.. math:: 
	y_{ss}(t)=A|H(j\omega)| cos(\omega t + \theta + \angle H(j\omega)).
	
Com isso, a resposta de um sistema dinâmico à uma entrada senoidal, em regime permanente, pode ser interpretada como o sinal senoidal de entrada escalado por um ganho :math:`|H(j\omega)|`, e deslocado por uma fase :math:`\angle H(j\omega)`. 

-----------------------------------------------
Exemplo: Resposta de sistema a entrada senoidal
-----------------------------------------------

Considerando o sistema representado pela função de transferência

.. math:: 
	H(s)=\frac{(s+1)}{(s+10)}
		
sujeito à uma entrada :math:`x(t)=cos(3t)`, determine a resposta :math:`y(t)` em regime permanente.
	
Solução:

.. container:: toggle, toggle-hidden
	
	Considerando que
		
	.. math::
		H(j\omega)=\frac{j\omega +1}{j\omega +10},
			
	podemos obter o módulo e a fase de :math:`H(j\omega)` por meio de
		
	.. math::
		|H(j\omega)|=\frac{\sqrt{\omega^2 + 1^2}}{\sqrt{\omega^2 + 10^2}}
			
	e
		
	.. math:: 
		\angle H(j\omega)=tan^{-1}\Big(\frac{\omega}{1}\Big)-tan^{-1}\Big(\frac{\omega}{10}\Big)

	Dessa forma, podemos obter o valor do módulo e da fase de :math:`H(j\omega)` para qualquer valor de :math:`\omega`. Para a entrada :math:`x(t)=cos(3t)`, temos :math:`\omega=2` e^
	
	.. math::
		|H(j3)|=\frac{\sqrt{3^2 + 1^2}}{\sqrt{3^2 + 10^2}}=\frac{\sqrt{10}}{\sqrt{109}}=0,3
	
	e
	
	.. math:: 
		\angle H(j3)=tan^{-1}\Big(\frac{3}{1}\Big)-tan^{-1}\Big(\frac{3}{10}\Big)=54,87^o
		
	Dessa forma, :math:`y_{ss}(t)`, para a entrada :math:`x(t)=cos(3t)`, é
	
	.. math::
		y_{ss}(t)=A|H(h)| cos(\omega t + \theta + \angle H(j\omega))=0,3cos(2t+54,87^o).
			
Diagrama de Bode
================

Como apresentado na seção anterior, a resposta de um sistema dinâmico, quando excitado por uma entrada senoidal, será uma senóide com a mesma frequência, porém, com amplitude e fase alteradas pelo sistema dinâmico. Cada sistema dinâmico se comportará diferente para valores diferentes de frequência, dessa forma, é útil saber qual sera o comportamento de um sistema para todo o espectro de frequências. Isso é alcançado usando o diagrama de Bode, o qual consiste em uma representação gráfica do módulo e fase de :math:`H(j\omega)`.

No diagrama de Bode, são apresentados separadamente :math:`|H(j\omega)|` e :math:`\angle H(j\omega)`, para todos valores de :math:`\omega`. Esses gráficos são apresentados considerando escala logarítmica, o que facilita a interpretação e traçado dos mesmos. 

Considerando uma função de transferência

.. math::
	H(j\omega)=\frac{K\prod_{i=1}^{m} (j\omega+z_i)}{\prod_{j=1}^{n} (j\omega+p_j)}

a qual é constituída por um produto de polos dividido por um produto de zeros e é uma grandeza complexa, podemos representar seu módulo e sua fase como

.. math::
	|H(j\omega)|=\frac{K\prod_{i=1}^{m} \mid(j\omega+z_i)\mid}{\prod_{j=1}^{n} \mid(j\omega+p_j)\mid}
	
e

.. math::
	\angle H(j\omega)=\sum_{i=1}^{m} \angle(j\omega+z_i)-\sum_{j=1}^{n} \angle(j\omega+p_j).

O traçado da fase de :math:`\angle H(j\omega)` é direto, já que podemos obter a fase de cada elemento da função de transferência e somar os espectros de fase dos mesmos. Porém, para o módulo, esse traçado não é direto, pois :math:`|H(j\omega)|` é a multiplicação dos módulos individuais de cada elemento da função de transferência. 

Uma forma de simplificar a obtenção do diagrama de Bode é o traçado do logarítmo do módulo :math:`|H(j\omega)|`, fazendo com que seja possível somar os espectros de módulo das componentes individuais da função de transferência. Isso porque, ao aplicarmos o logarítmo em :math:`|H(j\omega)|`, obtemos

.. math::
	log_{10}(|H(j\omega)|)&=log_{10}\Big(\frac{K\prod_{i=1}^{m} |(j\omega+z_i)|}{\prod_{j=1}^{n}|(j\omega+p_j)|}\Big)
	
	log_{10}(|H(j\omega)|)&=log_{10}(K)+\sum_{i=1}^{m} log_{10} (|(j\omega+z_i)|) - \sum_{j=1}^{n}log_{10}(|(j\omega+p_j)|).

Ou seja, após aplicarmos o logarítmo na base 10 em :math:`|H(j\omega)|`, podemos somar a contribuição de cada elemento de :math:`H(j\omega)` para obter :math:`log_{10}(|H(j\omega)|)`. Por convenção, sempre é usado o valor de :math:`log_{10}(|H(j\omega)|)` multiplicado por 20, resultado na unidade decibél. Com isso, o diagrama de Bode é a representação do módulo e fase de :math:`H(j\omega)`, para todo :math:`\omega`, sendo que o módulo é apresentado por meio de :math:`20log_{10}(|H(j\omega)|)` e a fase diretamente como  :math:`\angle H(j\omega)`. Um exemplo de diagrama de Bode, para o sistema :math:`H(s)=\frac{(s+2)}{s^2+0,5s+1}` é apresentado na figura a seguir.

.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G = 0.2*control.tf([1,2],[1,0.5,1])
		plt.clf()
		ag,phase,omega = control.bode(G,Hz=True,dB=True,color='k') 
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBode.png')
		
.. figure:: /figures/exemploBode.png
	:figwidth: 80%
	:align: center

	**Exemplo de um diagrama de Bode.**
	
O traçado do diagrama de Bode pode ser esboçado se conhecermos o comportamento de cada tipo de elemento de uma função de transferência. Esboçando o comportamento de cada elemento, e somando os espectros de módulo e fase, obtemos o diagrama de Bode de qualquer função de transferência. A seguir são apresentados os espectros de módulo e fase dos componentes básicos de uma função de transferência (ganho, zeros e polos).

------------------------
Diagrama de Bode - Ganho
------------------------

Uma função de transferência definida como apenas um ganho :math:`H(s)=K` tem seu valor independente de :math:`\omega`. Dessa forma, tanto o módulo quanto a fase serão linhas horizontais, com o módulo tendo valor :math:`20log_{10}(K)` e fase :math:`0`, quando o ganho tem sinal positivo, e fase :math:`-180^o` quando o ganho tem sinal negativo. O diagrama para uma constante :math:`K=1` é apresentado a seguir.   

.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G = control.tf([1],[1])
		plt.clf()
		ag,phase,omega = control.bode(G,Hz=False,dB=True,color='k')
		ag,phase,omega = control.bode(-1*G,Hz=False,dB=True,color='k',linestyle='dotted')		
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBodeConstante.png')		
		
.. figure:: /figures/exemploBodeConstante.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para uma constante positiva (linha sólida) e negativa (linha pontilhada), ambas com ganho unitário.**


-----------------------------------------
Diagrama de Bode - Polo ou Zero na origem
-----------------------------------------

Quando existe um polo na origem, o qual implementa um integrador, cuja função de transferência é :math:`G(j\omega)=\frac{1}{j\omega}`, temos 

.. math:: 
	20log_{10}|G(j\omega)|=\Big|\frac{1}{j\omega}\Big|=-20log_{10}|j\omega|
	
o que corresponde à uma reta com inclinação :math:`-20`, a qual cruza o eixo :math:`x` em :math:`0` quando :math:`\omega=1`, pois :math:`log_{10}\omega=0`. A fase é constante, sendo :math:`\angle G(j\omega)=\angle \frac{1}{j\omega}=- \angle (j\omega)=-90^o`.

De forma análoga, quando temos um derivador, representado pela função de transferência :math:`G(j\omega)=j\omega`, o módulo será dado por 

.. math:: 
	20log_{10}|G(j\omega)|=j\omega|=20log_{10}|j\omega|
	
representando uma reta com inclinação 20, e a fase será :math:`\angle G(j\omega)=\angle j\omega=90^o`. O diagrama de Bode para sistemas integradores e derivadores é apresentado a seguir.

.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G_d = control.tf([1,0],[1])
		G_i = control.tf([1],[1,0])
		plt.clf()
		ag,phase,omega = control.bode(G_i,Hz=False,dB=True,color='k')
		ag,phase,omega = control.bode(G_d,Hz=False,dB=True,color='k',linestyle='dotted') 

		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBodeIntegrador.png')
		
.. figure:: /figures/exemploBodeIntegrador.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para um integrador (linha sólida) e um derivador (linha pontilhada).**


-------------------------------------------------
Diagrama de Bode - Polo ou Zero de primeira ordem
-------------------------------------------------

Uma função de transferência pode ser composta de polos ou zeros únicos. Para o caso com polo único, temos a função de transferência na forma

.. math:: 
	H(j\omega)=\frac{1}{(j\omega+a)}.

O módulo, :math:`|H(j\omega)|`, é definido como

.. math::
	|H(j\omega)|=-20log_{10}\Big| 1+\frac{j\omega}{a} \Big|.
	
Quando :math:`\omega` é muito pequeno em relação à :math:`a`, o módulo se aproxima à :math:`-20log_{10}\Big| 1\Big|=0`. Já para :math:`\omega>>a`, o módulo é

.. math::
	|H(j\omega)|=-20log_{10}\Big| 1+\frac{j\omega}{a} \Big|\approx -20log_{10}\omega + 20log_{10}a.

Na escala logarítmica, a aproximação da expressão :math:`-20log_{10}\omega + 20log_{10}`  equivale à uma reta, iniciando em :math:`\omega=a` e com decaimento de -20~dB por década. Dessa forma, uma aproximação da magnitude do diagrama de Bode para um sistema com polo único consiste em uma reta constante entre :math:`\omega=-\infty` e :math:`\omega=a`, e uma reta decrescente, partindo de :math:`\omega=a` até :math:`\omega=\infty`, com decaimento de 20dB/Década. Essa aproximação é válida, resultando em uma diferença menor que 3~dB. 

A fase de :math:`H(j\omega)` é dada por

.. math::
	\angle H(j\omega)=-\angle\Big(1+\frac{j\omega}{a} \Big)=-tan^{-1}\Big(\frac{\omega}{a} \Big).

Se avaliarmos o comportamento da fase para :math:`\omega<<a`, temos

.. math::
	-tan^{-1}\Big(\frac{\omega}{a} \Big)\approx 0.

De forma similar, para para :math:`\omega<<a`, temos

.. math::
	-tan^{-1}\Big(\frac{\omega}{a} \Big)\approx -90^o.

A fase é composta, então, por duas assíntotas em :math:`0^o` e :math:`-90^o`, ligadas por uma reta iniciando em :math:`0,1a` e terminando em :math:`10a`. Dessa forma, a fase é :math:`-45^o` quando :math:`\omega=a`.

Para um sistema 

.. math::
	H(s)=\frac{1}{s+a}

o seu diagrama de Bode pode ser traçado como
	
.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G_d = control.tf([1,1],[1])
		G_i = control.tf([1],[1,1])
		plt.clf()
		ag,phase,omega = control.bode(G_i,Hz=False,dB=True,color='k')

		ax1,ax2 = plt.gcf().axes     # get subplot axes
		plt.sca(ax1)                 # magnitude plot
		plt.plot([0,1],[0,0],'k--')
		plt.plot([1,10],[0,-20],'k--')
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBodePoloOrdem1.png')
		
		
.. figure:: /figures/exemploBodePoloOrdem1.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para um polo em s-a (linha sólida) e suas assíntotas (linha pontilhada).**
	
*Explicar sobre zeros*

.. math::
	H(j\omega)=(j\omega+a)

.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G_d = control.tf([1,1],[1])
		G_i = control.tf([1],[1,1])
		plt.clf()
		ag,phase,omega = control.bode(G_d,Hz=False,dB=True,color='k')
		
		ax1,ax2 = plt.gcf().axes     # get subplot axes
		plt.sca(ax1)                 # magnitude plot
		plt.plot([0,1],[0,0],'k--')
		plt.plot([1,10],[0,20],'k--')
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBodeZeroOrdem1.png')
		
		
.. figure:: /figures/exemploBodeZeroOrdem1.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para um zero em s-a (linha sólida) e suas assíntotas (linha pontilhada).**

-------------------------------------------------
Diagrama de Bode - Polos e zeros de segunda ordem
-------------------------------------------------

Função de transferência com polos de segunda ordem.

.. math::
	H(s)=\frac{1}{s^2+2\xi \omega_n s + \omega_n^2}

.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G2 = control.tf([1],[1,4,1])
		G1 = control.tf([1],[1,2,1])
		G07 = control.tf([1],[1,1.4,1])
		G05 = control.tf([1],[1,1,1])
		G03 = control.tf([1],[1,0.6,1])
		plt.clf()
		ag,phase,omega = control.bode(G2,Hz=False,dB=True,color='y',label=r'$\xi=2$')
		ag,phase,omega = control.bode(G1,Hz=False,dB=True,color='k',label=r'$\xi=1$')
		ag,phase,omega = control.bode(G07,Hz=False,dB=True,color='r',label=r'$\xi=0,7$')
		ag,phase,omega = control.bode(G05,Hz=False,dB=True,color='g',label=r'$\xi=0,5$')
		ag,phase,omega = control.bode(G03,Hz=False,dB=True,color='b',label=r'$\xi=0,3$')
		
		ax1,ax2 = plt.gcf().axes     # get subplot axes
		plt.sca(ax1)                 # magnitude plot
		plt.plot([0,1],[0,0],'k--')
		plt.plot([1,100],[0,-80],'k--')
		plt.xlabel("Frequência (rad/s)")

		plt.legend()
		plt.savefig('source/figures/exemploBodePoloOrdem2.png')
		
		
.. figure:: /figures/exemploBodePoloOrdem2.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para um polos de segunda ordem (linha sólida) e suas assíntotas (linha pontilhada).**


Função de transferência com polos de segunda ordem.

.. math::
	H(s)=s^2+2\xi \omega_n s + \omega_n^2

.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G2 = control.tf([1,4,1],[1])
		G1 = control.tf([1,2,1],[1])
		G07 = control.tf([1,1.4,1],[1])
		G05 = control.tf([1,1,1],[1])
		G03 = control.tf([1,0.6,1],[1])
		plt.clf()
		ag,phase,omega = control.bode(G2,Hz=False,dB=True,color='y',label=r'$\xi=2$')
		ag,phase,omega = control.bode(G1,Hz=False,dB=True,color='k',label=r'$\xi=1$')
		ag,phase,omega = control.bode(G07,Hz=False,dB=True,color='r',label=r'$\xi=0,7$')
		ag,phase,omega = control.bode(G05,Hz=False,dB=True,color='g',label=r'$\xi=0,5$')
		ag,phase,omega = control.bode(G03,Hz=False,dB=True,color='b',label=r'$\xi=0,3$')
		
		ax1,ax2 = plt.gcf().axes     # get subplot axes
		plt.sca(ax1)                 # magnitude plot
		plt.plot([0,1],[0,0],'k--')
		plt.plot([1,100],[0,80],'k--')
		plt.xlabel("Frequência (rad/s)")

		plt.legend()
		plt.savefig('source/figures/exemploBodeZeroOrdem2.png')
		
		
.. figure:: /figures/exemploBodeZeroOrdem2.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para zeros de segunda ordem (linha sólida) e suas assíntotas (linha pontilhada).**

---------
Exemplo 1
---------

Diagrama de bode para a função de trasnferência

.. math::
	H(s)=\frac{100(s+1)}{s(s+10)}.

.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G = control.tf([100,100],[1,10,0])
		plt.clf()
		ag,phase,omega = control.bode(G,Hz=False,dB=True,color='k')
	
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBode2.png')
		
		
.. figure:: /figures/exemploBode2.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para a FT do exemplo 1.**

---------
Exemplo 2
---------

Diagrama de bode para a função de trasnferência

.. math::
	H(s)=0,01\frac{(s+10)}{(s+0,1)(s+1)}.

.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G = control.tf([0.01,0.1],[1,1.1,0.1])
		plt.clf()
		ag,phase,omega = control.bode(G,Hz=False,dB=True,color='k')
	
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBode3.png')
		
		
.. figure:: /figures/exemploBode3.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para o a FT do exemplo 2.**

		
Projeto de Filtros
==================

--------------
Filtros ideais
--------------

Um filtro consiste em uma entidade capaz de atenuar seletivamente um conjunto de frequências do seu sinal de entrada, retornando em sua saída o sinal filtrado. Uma representação geral de um processo de filtragem é apresentado na figura a seguir.

.. figure:: /figures/blocosFiltro.png
	:figwidth: 40%
	:align: center

	**Diagrama de blocos de um filtro. O filtro atenua um conjunto de frequências do espectro do sinal de entrada, retornando um sinal filtrado.**	
	
O resultado ideal de um processo de filtagem consistem em atenuar perfeitamente o conjunto de frequências desejado da banda fitrada (*stopband*), e não modificar o conjunto de frequências da banda passante (*passband*), a qual se deseja-se manter. Os quatro tipos básicos de filtros são:

- **Filtro passa-baixas ideal.** Todas as frequências abaixo da frequência de corte, :math:`w_c`, são mantidas, enquanto todas frequência acima de :math:`w_c` são definidas como zero. O comportamento desse filtro passa-baixas ideal é representado por

.. math::
    H(j\omega) = 	\begin{cases}
						1 &: \omega\leq\omega_c\\
						0 &: \text{caso contrário}
					\end{cases}

- **Filtro passa-altas ideal.** O filtro passa-altas tem o comportamento inverso do passa-baixas, mantendo as frequências acima de :math:`w_c`, e atenuando completamente as frequências abaixo de :math:`w_c`. Ele é descrito pela equação

.. math::
    H(j\omega) = 	\begin{cases}
						1 &: \omega>\omega_c\\
						0 &: \text{caso contrário}
					\end{cases}
     

- **Filtro passa-bandas ideal.** Um filtro passa-bandas mantém as frequências entre $\omega_L$ e $\omega_H$ atenuando todas as demais frequências. A equação que descreve ele é

.. math::
    H(j\omega) = 	\begin{cases}
						1 &: \omega_L\leq\omega\leq\omega_H\\
						0 &: \text{caso contrário}
					\end{cases}
  
- **Filtro rejeita-bandas ideal.** O filtro rejeita-bandas tem o comportamento oposto do filtro passa-bandas, já que ele define um conjunto de frequências, entre $\omega_L$ e $\omega_H$, que será rejeitado, com as demais frequências sendo mantidas. Um tipo específico de filtro rejeita-bandas é o filtro *Notch*, projetado para rejeitar uma frequência bem específica (em sistemas de áudio é geralmente a frequência da rede de alimentação). Esse filtro é definido por

.. math::
    H(j\omega) = 	\begin{cases}
						0 &: \omega_L\leq\omega\leq\omega_H\\
						1 &: \text{caso contrário}
					\end{cases}

A amplitude de :math:`H(j\omega)` desses filtro ideais é apresentada a seguir.
  
.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import locale
		locale.setlocale(locale.LC_NUMERIC, "pt_BR")
		
		import numpy as np
		import matplotlib.pyplot as plt
		plt.rcdefaults()
		plt.rcParams['axes.formatter.use_locale'] = True
      
		w = np.logspace(1,5);
		FPb = w<1000
		plt.subplot(2,2,1)
		plt.semilogx(w, FPb,'k')
		plt.grid()
		plt.xlabel(r'$\omega$')
		plt.ylabel("Magnitude")
		plt.ylim(-0.1, 1.1)
		plt.title("Passa baixas")
		#axis('off')
		
		w = np.logspace(1,5);
		Fpa = w>1000
		plt.subplot(2,2,2)
		plt.semilogx(w, Fpa,'k')
		plt.grid()
		plt.xlabel(r'$\omega$')
		plt.ylabel("Magnitude")
		plt.ylim(-0.1, 1.1)
		plt.title("Passa altas")	

		w = np.logspace(1,5);
		Fpf = np.logical_and(w>500, w<5000)
		plt.subplot(2,2,3)
		plt.semilogx(w, Fpf,'k')
		plt.grid()
		plt.xlabel(r'$\omega$')
		plt.ylabel("Magnitude")
		plt.ylim(-0.1, 1.1)
		plt.title("Passa faixas")
	

		w = np.logspace(1,5);
		Frf = np.logical_or(w<500, w>5000)
		plt.subplot(2,2,4)
		plt.semilogx(w, Frf,'k')
		plt.grid()
		plt.xlabel(r'$\omega$')
		plt.ylabel("Magnitude")
		plt.ylim(-0.1, 1.1)
		plt.title("Rejeita faixas")			
		plt.tight_layout()
		plt.savefig('source/figures/filtrosIdeais.png')
		
.. figure:: /figures/filtrosIdeais.png
	:figwidth: 80%
	:align: center

	**Representação do espectro de frequência ideal de filtros.**
  
----------------  
Filtros práticos
----------------

O comportamento apresentado pelos filtros ideais não é atingível na prática. Um sistema com ganho zero em alguma frequência é não realizável. Dessa forma, um filtro prático é um sistema dinâmico que aproxima o comportamento do filtro ideal. Ao invés de termos uma transição abrupta entre a banda passante e a filtrada, temos uma banda de transição. Existem várias arquiteturas de filtros práticos, as quais são diferenciadas por algumas características como: a linearidade da banda passante; a largura da banda de trasição; a implementação eletrônica; entre outros.

A arquitetura de filtro mais comum são os filtros *Butterworth*. 

.. math::
	H(s)=\frac{1}{(s+a)}

*Continuação*

---------------------
Exemplos de filtragem
---------------------

Considere um sinal senoidal puro, com frequência angular :math:`\omega=0,5`, definido como

.. math::
	x(t)=cos(\omega t).
	
Esse sinal é corrompido por um ruído branco, representado por :math:`r(t)`, que é um sinal com componentes em todo o espectro de potência. O sinal ruidoso é representado por

.. math::
	x_r(t)=x(t)+r(t).
	


.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control
		from random import gauss
		from random import seed

		# How many time points are needed i,e., Sampling Frequency
		freqAmostragem   = 100;
		# At what intervals time points are sampled

		intervaloAmostragem = 1 / freqAmostragem;
		# Instantes de início e fim
		inicio	= 0
		fim 	= 30
		
		# Frequency of the signals
		freqSinal1     = 0.5
		freqSinal2     = 10
		# Vetor de pontos do tempo
		tempo = np.arange(inicio, fim, intervaloAmostragem)
		# Create two sine waves
		amplitude1 = np.sin(2*np.pi*freqSinal1*tempo)
		amplitude2 = np.sin(2*np.pi*freqSinal2*tempo)
		# Create subplot
		plt.subplot(4,2,1)
		# Senóide com frequência 1
		plt.title('sen(0,5t)')
		plt.plot(tempo, amplitude1,'k')
		plt.xlabel('Tempo (s)')
		plt.ylabel('Amplitude')
		
		fourierTransform1 = np.fft.fft(amplitude1)/len(amplitude1)           # Normalize amplitude
		fourierTransform1 = fourierTransform1[range(int(len(amplitude1)/2))] # Exclude sampling frequency
		tpCount     = len(amplitude1)
		values      = np.arange(int(tpCount/2))
		timePeriod  = tpCount/freqAmostragem
		frequencies = values/timePeriod
		# Frequency domain representation
		plt.subplot(4,2,2)
		plt.yscale("log")
		plt.title('T. de Fourier de sen(0,5t)')
		plt.plot(frequencies, abs(fourierTransform1),'k')
		plt.xlabel('Frequência (rad/s)')
		plt.ylabel('Amplitude')		
	
		# Gera um ruído branco
		seed(1)
		ruidoBranco = [gauss(0, 0.2) for i in range(tempo.size)]
		
		plt.subplot(4,2,3)
		plt.title('Ruído branco r(t)')
		plt.plot(tempo, ruidoBranco,'k')
		plt.xlabel('Tempo (s)')
		plt.ylabel('Amplitude')	
		
		fourierTransform2 = np.fft.fft(ruidoBranco)/len(ruidoBranco)           # Normalize amplitude
		fourierTransform2 = fourierTransform2[range(int(len(ruidoBranco)/2))] # Exclude sampling frequency
		tpCount     = len(ruidoBranco)
		values      = np.arange(int(tpCount/2))
		timePeriod  = tpCount/freqAmostragem
		frequencies = values/timePeriod
		# Frequency domain representation
		plt.subplot(4,2,4)
		plt.yscale("log")
		plt.title('T. de Fourier de r(t)')
		plt.plot(frequencies, abs(fourierTransform2),'k')
		plt.xlabel('Frequência (rad/s)')
		plt.ylabel('Amplitude')
					
		# Obtendo x(t)=sen(t)+RuidoBranco
		x = amplitude1 + ruidoBranco
		# Time domain representation of the resultant sine wave
		plt.subplot(4,2,5)
		plt.title('x(t)=sen(t)+r(t)')
		plt.plot(tempo, x,'k')
		plt.xlabel('Time')
		plt.ylabel('Amplitude')
		
		# Frequency domain representation
		fourierTransform = np.fft.fft(x)/len(x)           # Normalize amplitude
		fourierTransform = fourierTransform[range(int(len(x)/2))] # Exclude sampling frequency
		tpCount     = len(x)
		values      = np.arange(int(tpCount/2))
		timePeriod  = tpCount/freqAmostragem
		frequencies = values/timePeriod
		# Frequency domain representation
		plt.subplot(4,2,6)
		plt.yscale("log")
		plt.title('T. de Fourier de x(t)')
		plt.plot(frequencies, abs(fourierTransform),'k')
		plt.xlabel('Frequency')
		plt.ylabel('Amplitude')
	
		plt.tight_layout()
		plt.savefig('source/figures/exemploSenos.png')

		
		# Criando o filtro
		G = control.tf([1],[1,1.414214,1])
		plt.clf()
		ag,phase,omega = control.bode(G,Hz=False,dB=True,color='k')		
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBodeSenos.png')
		
		# Filtrando e plotando o sinal filtrado
		T, yout = control.forced_response(G, tempo, x, 0)

		plt.subplot(2,2,1)
		# Senóide com frequência 1
		plt.title('x_r(t)=sen(0,5t)+r(t)')
		plt.plot(tempo, x,'k')
		plt.xlabel('Tempo (s)')
		plt.ylabel('Amplitude')
		
		# Frequency domain representation
		fourierTransform = np.fft.fft(x)/len(x)           # Normalize amplitude
		fourierTransform = fourierTransform[range(int(len(x)/2))] # Exclude sampling frequency
		tpCount     = len(x)
		values      = np.arange(int(tpCount/2))
		timePeriod  = tpCount/freqAmostragem
		frequencies = values/timePeriod
		# Frequency domain representation
		plt.subplot(2,2,2)
		plt.yscale("log")
		plt.title('T. de Fourier de x_r(t)')
		plt.plot(frequencies, abs(fourierTransform),'k')
		plt.xlabel('Frequency')
		plt.ylabel('Amplitude')


		plt.subplot(2,2,3)
		plt.title('y(t)')
		plt.plot(T, yout,'k')
		plt.xlabel('Tempo (s)')
		plt.ylabel('Amplitude')		
		
		# Frequency domain representation
		fourierTransform = np.fft.fft(yout)/len(yout)           # Normalize amplitude
		fourierTransform = fourierTransform[range(int(len(yout)/2))] # Exclude sampling frequency
		tpCount     = len(yout)
		values      = np.arange(int(tpCount/2))
		timePeriod  = tpCount/freqAmostragem
		frequencies = values/timePeriod
		# Frequency domain representation
		plt.subplot(2,2,4)
		plt.yscale("log")
		plt.title('T. de Fourier de y(t)')
		plt.plot(frequencies, abs(fourierTransform),'k')
		plt.xlabel('Frequency')
		plt.ylabel('Amplitude')		
		
		
		plt.tight_layout()
		plt.savefig('source/figures/exemploSenosFiltrado.png')

.. figure:: /figures/exemploSenos.png
	:figwidth: 80%
	:align: center

	**Exemplo do sinal senoidal corrompido por um ruído branco.**
		
.. figure:: /figures/exemploBodeSenos.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para o filtro passa-baixas *Butterworth* de segunda ordem.**
	
.. figure:: /figures/exemploSenosFiltrado.png
	:figwidth: 80%
	:align: center

	**Comparação entre os sinal ruidoso e filtrado, e seus espectros de Fourier.**
	
	
Exercícios
==========

- **Exercício 1** Encontre a magnitude e a fase de :math:`H(j\omega)` para :math:`\omega=2` e para :math:`\omega=10` para a função de transferência

.. math::
		H(s)=\frac{10(s+2)}{(s+1)(s+5)}