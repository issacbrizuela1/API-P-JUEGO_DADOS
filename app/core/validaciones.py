from pydantic import BaseModel, validator,root_validator
import re

class validaciones():

    imput:any
    patrones={
        'parrafos': "/^([aA-zZñÑáÁéÉíÍóÓúÚ@\!\#\&\.\-\_\s\d])+$/i",
        'textoslargos': '/([aA-zZñÑáÁéÉíÍóÓúÚ@\!\#\&\.\-\_\s\d\n\,])+/i'
        }

    def validar_str(self,input:BaseModel,fieldsToValidate):#fieldsToevaluate
        FIELDS=input
        for datos in fieldsToValidate:
            result=re.match(self.patrones['parrafos'], FIELDS[datos])
            if(FIELDS[datos]=="" or FIELDS[datos]==None):
                raise ValueError(f"El input {datos} es requerido") 
            if(len(FIELDS[datos])>100):
                raise ValueError(f"El input {datos} debe contener menos de 100 caracteres")
            if(result==False):
                raise ValueError(f"El input {datos} debe contener los caracteres validos alphanumericos y (@,!,#,&,.,-,_)")
            return input