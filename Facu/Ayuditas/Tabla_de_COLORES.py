print("/" + "033[cod_formato;cod_color_texto;cod_color_fondo M")


def construye_tabla_formatos():
    for estilo in range(8):
        for colortexto in range(30, 38):
            cad_cod = ''
            for colorfondo in range(40, 48):
                fmto = ';'.join([str(estilo),
                                 str(colortexto),
                                 str(colorfondo)])
                cad_cod += "\033[" + fmto + "m " + fmto + " \033[0m"
            print(cad_cod)
        print('\n')


construye_tabla_formatos()
input()

print("\033[0;37;40m Normal text\n")
print("\033[2;37;40m Underlined text\033[0;37;40m \n")
print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
print("\033[5;37;40m Negative Colour\033[0;37;40m\n")


