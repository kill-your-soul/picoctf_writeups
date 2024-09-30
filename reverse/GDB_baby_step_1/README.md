# vault-door-training

### Given:
1. `debugger0_a` file

### Solution
1. Open file in IDA 
2. Examine the main function in the assembly code: 
```asm 
; Attributes: bp-based frame

; int __cdecl main(int argc, const char **argv, const char **envp)
public main
main proc near

var_10= qword ptr -10h
var_4= dword ptr -4

; __unwind {
endbr64
push    rbp
mov     rbp, rsp
mov     [rbp+var_4], edi
mov     [rbp+var_10], rsi
mov     eax, 549698
pop     rbp
retn
; } // starts at 1129
main endp
```
3. The function moves the value `549698` into the eax register, meaning this is the important result after the execution of main