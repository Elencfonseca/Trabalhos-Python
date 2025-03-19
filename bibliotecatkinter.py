from plyer import notification
#Função para exibir a notificação

def lembrete(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        app_name='lembrete',
        timeout=10 #Duração da notificação em segundos
    )
lembrete("beba água, o rim pede socorro!!", "tem que tomar agua para evitar pedras no rim") #Exibindo o lembrete