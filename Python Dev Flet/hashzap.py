# Tela inicial:
    # Titulo: Hashzap
    # Botão: Iniciar chat
        # quando clicar no botão: 
            # abrir um popup
                #Titulo: Bem vindo ao Hashzap
                # Caixa de testo: Escreva seu nome no chat
                # Botão: Entrar no chat
                    # quando clicar no botao
                    # fechar o popup
                    # sumir com o titulo
                    # sumir com o botao
                        # carregar o chat
                        # carregar o campo de enviar mensagem: "Digite sua mensagem"
                        # botao enviar
                            # quando clicar o botao enviar
                            # enviar a mensagem
                            # limpar a caixa de mensagem

# Flet
# importar o flet
import flet as ft

# criar uma funcao principal para rodar o seu app
def main(pagina):
    # titulo
    titulo = ft.Text("Hashzap")

    def enviar_mensagem_tunel(mensagem):
        # executar tudo o que eu quero que aconteca para
        # todos os usuarios que receberem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        # limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(evento):
        # fechar o popup
        popup.open = False

        # sumir com o titulo
        pagina.remove(titulo)

        # sumir com o botao
        pagina.remove(botao)

        # carregar o chat
        pagina.add(chat)

        # carregar o campo de enviar mensagem
        # carregar o botao enviar
        pagina.add(linha_enviar)

        # adicionar no chat "alguem entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()


    # criar o popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,
                           actions=[botao_popup])

    # botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # colocar os elementos na página
    pagina.add(titulo)
    pagina.add(botao)


# executar essa funcao com o flet
# ft.app(main, view=ft.WEB_BROWSER) não funciona mais, solução nova:
ft.app(main, view=ft.AppView.WEB_BROWSER)










