
Para visualizar o VRML é necessário um plug in no 
navegador ou algum aplicativo, um exemplo é o
freeWRL
http://freewrl.sourceforge.net/
Outras referências
https://www.inf.pucrs.br/manssour/VRML/index.html
http://sim.di.uminho.pt/vrmltut/frmintex.htm

Instalação OpenGL/Dev C/C++ (32 bits)

Baixe uma versão do Dev C/C++

Atualize os pacotes do Dev incluindo o
freeglut (ferramentas / Atualizações)

Incluir os seguintes argumentos no linker

lglut32 lmingw32 lopengl32 lglu32 lgdi32
lwinmm (Ferramentas / opções do compilador)

Instalação OpenGL/Python 3

	No Python 3.7 (32 bits)

Windows

	pip install PyOpenGL PyOpenGL_accelerate

Linux e mac

	sudo apt get install python3 opengl

No Python 3.5 ou superior precisa baixar

https ://support.microsoft.com/ptbr/help/2977003/ 
the latest supported visual c downloads

Por fim, para que o programa rode, será necessario que o 
arquivo glut32.dll esteja na mesma pasta do programa.