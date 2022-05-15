cc=gcc
ens=nasm
arc=ar

libcalculadora.so: calculadora.o
	${cc} -Wall -shared -o libcalculadora.so calculadora.o

calculadora.o: calculadora.s
	${ens} -g -felf64 calculadora.s
