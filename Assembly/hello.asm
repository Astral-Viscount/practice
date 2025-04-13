section .data
    hello db 'Hello, World!', 0     ; Null-terminated string
    newline db 0x0A, 0              ; Newline character

section .text
    global _start

_start:
    ; Print the "Hello, World!" message
    mov eax, 4                     ; Syscall number for sys_write
    mov ebx, 1                     ; File descriptor 1 (stdout)
    mov ecx, hello                 ; Pointer to the "Hello, World!" string
    mov edx, 13                    ; Length of the string
    int 0x80                       ; Call kernel

    ; Print the newline character
    mov eax, 4                     ; Syscall number for sys_write
    mov ebx, 1                     ; File descriptor 1 (stdout)
    mov ecx, newline               ; Pointer to the newline character
    mov edx, 1                     ; Length of the newline character (1 byte)
    int 0x80                       ; Call kernel

    ; Exit the program
    mov eax, 1                     ; Syscall number for sys_exit
    xor ebx, ebx                   ; Exit code 0
    int 0x80                       ; Call kernel
