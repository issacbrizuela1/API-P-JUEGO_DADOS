
import re

class validaciones():

    imput:any
    patrones={
        'parrafos': "/^([aA-zZñÑáÁéÉíÍóÓúÚ@\!\#\&\.\-\_\s\d])+$/i",
        'textoslargos': '/([aA-zZñÑáÁéÉíÍóÓúÚ@\!\#\&\.\-\_\s\d\n\,])+/i'
        }

    def validar_str(self,input:str):
        for datos in input:
            result=re.math(self.patrones[0],datos)
            if(datos.len>100):
                return f"El input {datos} debe contener menos de 100 caracteres"
            if(result==False):
                return f"El input {datos} debe contener los caracteres validos alphanumericos y (@,!,#,&,.,-,_)"
        return input
                