Resposta de Sistemas à Entradas Senoidais e Diagrama de Bode
============================================================

Resposta de Sistemas à Entradas Senoidais
-----------------------------------------

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
	y_{ss}(t)=A|H(h)| cos(\omega t + \theta + \angle H(j\omega)).
	
Com isso, a resposta de um sistema dinâmico à uma entrada senoidal, em regime permanente, pode ser interpretada como o sinal senoidal de entrada escalado por um ganho :math:`|H(j\omega)|`, e deslocado por uma fase :math:`\angle H(j\omega)`. 


Exemplo: Resposta de sistema a entrada senoidal

.. container:: toggle, toggle-hidden

	Considerando o sistema apresentado a seguir
	
	.. image:: figures/sistema.png	
		:width: 200
		:alt: Alternative text	
		
	sujeito à uma entrada
		
Diagrama de Bode
----------------

Consider a CT signal :math:`x(t)`. A real valued CT signal is plotted using
the standard ways to plot a function $x: \setR \rightarrow
\setR$. Consider the sinusoidal signal $x(t)=325 \sin(2\pi 50 t)$ for
a short interval of time we can plot this as:


.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G = 0.2*control.tf([0.5,1],[1.5,0.5,1])
		plt.clf()
		ag,phase,omega = control.bode(G,Hz=True,dB=True) 
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBode.png')
		
.. figure:: /figures/exemploBode.png
	:figwidth: 80%
	:align: center

	**Exemplo de um diagrama de Bode.**
	
	
.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G = control.tf([1],[1])
		plt.clf()
		ag,phase,omega = control.bode(G,Hz=True,dB=True) 
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBodeConstante.png')
		
.. figure:: /figures/exemploBodeConstante.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para uma constante.**

.. container:: toggle, toggle-hidden

	.. exec_code:: realCTsignals signalplots
		:linenos:
		:hide_output:

		import numpy as np
		import matplotlib.pyplot as plt
		import control

		G = control.tf([1],[1,1])
		plt.clf()
		ag,phase,omega = control.bode(G,Hz=True,dB=True) 
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBodeIntegrador.png')
		
.. figure:: /figures/exemploBodeIntegrador.png
	:figwidth: 80%
	:align: center

	**Diagrama de Bode para um integrador.**


Projeto de Filtros
------------------