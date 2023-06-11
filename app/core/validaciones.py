

class validaciones():

    imput:any
    patrones={
        'parrafos': "/^([aA-zZñÑáÁéÉíÍóÓúÚ@\!\#\&\.\-\_\s\d])+$/i",
        'textoslargos': '/([aA-zZñÑáÁéÉíÍóÓúÚ@\!\#\&\.\-\_\s\d\n\,])+/i'
        }

    def validar_str(imput:str,pre=True, always=True)->str:
        result=re.math(self.patrones[0],imput)
        if(result==true):
            return "Datos validos"
        else:
            return 'Datos introducdos no validos caracteres validos alphanumericos y (@,!,#,&,.,-,_)'