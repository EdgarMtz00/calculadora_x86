global signo:function
global suma:function
global resta:function
global multi:function
global divi:function
global senox:function
global cosenox:function
global tangx:function
global arcoTan:function
global arcoSeno:function
global convRaG:function
global convGaR:function
global logarcm:function
global dosalan:function
global raizdos:function

section .data
ciento80:   dq 180.0

section .bss
resp:	resq 2
expo:   resq 2
arg1:   resq 2
seno: resq 2
coseno: resq 2
tngte: resq 2
sign: resq 2
sumaR: resq 2
restaR: resq 2
mulR: resq 2
divR: resq 2

section .text
signo:
    push rbp
	mov rbp,rsp
	sub rsp,48

       fld qword[rdi]
       fchs
       fstp qword[rel sign]
       movsd xmm0,qword[rel sign]

	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

suma:
	push rbx
	push r12
	push r13
	push r14
	push r15
	
	addsd xmm0, xmm1

	pop r15
	pop r14
	pop r13
	pop r12
	pop rbx
	ret

resta:
    push rbp
	mov rbp,rsp
	sub rsp,48

    subsd xmm0, xmm1
	
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

multi:
    push rbp
	mov rbp,rsp
	sub rsp,48

	mulsd xmm0, xmm1

	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

divi:
    push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
	push r15

    divsd xmm0, xmm1
	
    pop r15
	pop r14
	pop r13
	pop r12
	pop rbx
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

senox:
    push rbp
	mov rbp,rsp
	sub rsp,48

       fld qword[rdi]
       fsin
       fstp qword[rel seno]
       movsd xmm0,qword[rel seno]

	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

cosenox:
    push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
	push r15


       fld qword[rdi]
       fcos
       fstp qword[rel coseno]
       movsd xmm0,qword[rel coseno]

    pop r15
	pop r14
	pop r13
	pop r12
	pop rbx
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

tangx:
    push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
	push r15

    fld1
     ;angulo en radianes
    fld qword[rdi]
    fptan
    mov rbx,tngte
    fstp qword[rbx]
    movsd xmm0,qword[rbx]

    pop r15
	pop r14
	pop r13
	pop r12
	pop rbx
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

arcoTan:
    push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
	push r15

    fld qword[rdi] ; param. por refe. la tangente
    fld1
    fpatan     ; valor del arco  0<= ang <= 45  45 -> 90 compl
    mov rbx,arg1
    fstp qword[rbx]
    movsd xmm0,qword[rbx]

    pop r15
	pop r14
	pop r13
	pop r12
	pop rbx
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

arcoSeno:
    push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
	push r15

    fld qword[rdi] ; param. por refe. el seno
    fld qword[rdi] ; param. por refe. el seno
    fmul
    fld1
    fsubr
    fsqrt
    fpatan
    mov rbx, resp
    fstp qword[rbx]
    movsd xmm0,qword[rbx]

    pop r15
	pop r14
	pop r13
	pop r12
	pop rbx
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

convRaG:
    push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
    push r15

    fld qword[rdi]
    fld qword[rel ciento80]
    fmul
    fldpi
    fdiv
    fstp qword[rel arg1]
    movsd xmm0,qword[rel arg1]

    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx
    add rsp,48
    mov rsp,rbp
    pop rbp
    ret

convGaR:
   	push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
	push r15

	fldpi	;pi->st0
	fld qword[rdi] ;angulo->st0   pi->st1
	fmul		;pi*angulo ->st0
    mov rbx,ciento80
	fld qword[rbx] ;cargar 180.0->st0...pi*ang->st1
	fdiv		;div 180.0 st1/st0
	mov rbx,resp
	fstp qword[rbx]
	movsd xmm0, qword[rbx]

	pop r15
	pop r14
	pop r13
	pop r12
	pop rbx
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

logarcm:
    push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
	push r15

    fld1     ;1.0 -> st0
    fldl2t   ;log210->st0...pero 1.0 ->st1
    fdiv     ;el resultado ->st0
    fld qword[rdi] ;n->st0
    ;el resultado anterior ->st1
    fyl2x
    mov rbx,resp
    fstp qword[rbx]
    movsd xmm0,qword[rbx]

    pop r15
	pop r14
	pop r13
	pop r12
	pop rbx
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

dosalan:
    push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
	push r15

    fld1     ;1.0 -> st0
    fld qword[rdi] ;n->st0
    ;el resultado anterior ->st1
    f2xm1
    mov rbx,expo
    fstp qword[rbx]
    movsd xmm0,qword[rbx]

    pop r15
    pop r14
	pop r13
	pop r12
	pop rbx
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret

raizdos:
    push rbp
	mov rbp,rsp
	sub rsp,48
	push rbx
	push r12
	push r13
	push r14
	push r15

        fld qword[rdi]
        fsqrt
        fstp qword[rel resp]
        movsd xmm0,qword[rel resp]

    pop r15
	pop r14
	pop r13
	pop r12
	pop rbx
	add rsp,48
	mov rsp,rbp
	pop rbp
	ret