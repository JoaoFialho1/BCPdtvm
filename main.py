from scr.functions import api_anbima_register, read_internal_register, divergences


#==============Inputs==============#
stock = "BCPSA4"
start = "2025/04/30"
end = "2025/05/16"


#============Read-Datas============#
internal_register = read_internal_register('inputs/Registros_BCPSA4.csv')
anbima_registers = api_anbima_register(stock, start, end)

#==========Compare-datas============#
divergents = divergences(internal_register, anbima_registers)


#=============Outputs=======+======#
anbima_registers.to_csv('outputs/Negociacoes_BCPSA4.csv', sep=';')
divergents.to_csv('outputs/Divergencias_Negociacoes_BCPSA4.csv', sep=';')