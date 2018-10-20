from mycroft import MycroftSkill, intent_file_handler


class AnyIdeas(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ideas.any.intent')
    def handle_ideas_any(self, message):
        self.speak_dialog('ideas.any')


def create_skill():
    return AnyIdeas()

