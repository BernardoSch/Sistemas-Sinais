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
		ag,phase,omega = control.bode(G) 
		plt.xlabel("Frequência (rad/s)")
		plt.savefig('source/figures/exemploBode.png')
		
.. figure:: /figures/exemploBode.png
	:figwidth: 80%
	:align: center

	**Exemplo de um diagrama de Bode.**



Projeto de Filtros
------------------