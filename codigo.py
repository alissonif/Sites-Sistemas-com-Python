import flet as ft


def main(pagina):
    texto = ft.Text('up')

    chat = ft.Column()

    nome_usuario = ft.TextField(label='Nome usuario')

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem['tipo']
        if tipo == 'mensagem':
            texto_mensagem = mensagem['texto']
            usuario_mensagem = mensagem['usuario']
            chat.controls.append(
                ft.Text(f'{usuario_mensagem}:{texto_mensagem}'))
            pagina.update()
        else:
            usuario_mensagem = mensagem['usuario']
            chat.controls.append(ft.Text(
                f'{usuario_mensagem} entrou no site', size=12, italic=True, color=ft.colors.BLUE_800))
            pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(
            {'texto': campo_mensagem.value, 'usuario': nome_usuario.value, 'tipo': 'mensagem'})
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = ft.TextField(
        label='Campo mensagem', on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton(
        'Enviar', on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all(
            {'usuario': nome_usuario.value, 'tipo': 'entrada'})
        pagina.add(chat)

        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)

        pagina.add(ft.Row([
            campo_mensagem, botao_enviar_mensagem
        ]))

        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text('Bem vindo ao Haszap'),
        content=nome_usuario,
        actions=[ft.ElevatedButton('Entrar', on_click=entrar_popup)],
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        # texto_entrou = ft.Text('Entrou no chat')
        # pagina.add(texto_entrou)

    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

    pagina.background_color = ft.colors.RED


# ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
