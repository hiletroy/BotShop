from telegrambot.bot_views.generic import TemplateCommandView

class StartCommandView(TemplateCommandView):
    template_text = "messages/command_start_text.txt"

class HelpCommandView(TemplateCommandView):
    template_text = "messages/command_help_text.txt"

class UnknownCommandView(TemplateCommandView):
    template_text = "messages/command_unknown_text.txt"
