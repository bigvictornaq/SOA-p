@echo off

goto  :main
:main
          
          echo                                      ---PELIGRO---
          echo.
          echo -----------------------------------------------Entrada de DATAIN a R0-----------------------------------
          echo selecione la tecla (y)
          set /p Input=Enter Yes:
          :prueba
             If /I "%Input%"=="y" (
                echo -----------------------------------------Salida de R1 A DATAOUT-------------------------------
                echo -------------------------------------INgresastes A %Input%------------------------------------
                goto yes
                )
             goto no
          :yes
          echo apagar......
          echo ....
          exit
          :no
          echo -----------------------------------------------Entrada de DATAIN a R0-----------------------------------
          echo -----------------------------------------Debes selecionar  (y)--------------------
          echo.
          goto main
          